#!/usr/bin/env python3
"""ESML Query Engine — term resolver + metric DAG + SQL builder."""
# Copyright (c) 2026 [YOUR LEGAL ENTITY]
# Licensed under the Apache License, Version 2.0
# This file is an original work and is NOT derived from
# the Open Semantic Interchange (OSI) specification.
#
# Knowledge sources:
# - YAML parsing (PyYAML, MIT license, public)
# - SQL generation patterns (dbt-core, Apache 2.0, public)
# - Term resolution / NLU concepts (Stanford NLP, public academic)
# - DAG traversal algorithms (CLRS Introduction to Algorithms, public textbook)
#
# This file contains NO proprietary information from any employer or client.

import yaml
import os
import json
import sys


class ESMLQueryEngine:
    """Resolves business terms to SQL via ESML semantic model."""

    def __init__(self, model_dir: str):
        self.model_dir = model_dir
        self.glossary = {}
        self.metrics = {}
        self.entities = {}
        self.objects = {}
        self._load_model()

    def _load_model(self):
        """Load and cache all YAML files at initialization (setup-time)."""
        for root, _, files in os.walk(self.model_dir):
            for fname in files:
                if not fname.endswith(".yaml"):
                    continue
                path = os.path.join(root, fname)
                with open(path) as f:
                    try:
                        data = yaml.safe_load(f)
                    except yaml.YAMLError:
                        continue
                if not data:
                    continue
                # Index glossary terms
                if "domain_glossary" in data or "enterprise_glossary" in data:
                    gl = data.get("domain_glossary", data.get("enterprise_glossary", {}))
                    for term in gl.get("terms", []):
                        key = term.get("term", "").lower()
                        self.glossary[key] = term
                        for alias in term.get("aliases", []):
                            self.glossary[alias.lower()] = term
                # Index metrics
                if "metric_group" in data:
                    for tier_key in ["t3_atomic", "t2_derived", "t1_composite"]:
                        for m in data.get(tier_key, []):
                            self.metrics[m["name"]] = {**m, "tier": tier_key.split("_")[0].upper()}
                # Index entities
                if "entity" in data and "name" in data.get("entity", {}):
                    ent = data["entity"]
                    self.entities[ent["name"]] = ent

    def resolve_term(self, term: str) -> dict:
        """Resolve a business term to its metric definition."""
        key = term.lower().strip()
        if key in self.glossary:
            gl_entry = self.glossary[key]
            metric_ref = gl_entry.get("metric_ref", "")
            metric_name = metric_ref.split("#")[-1] if "#" in metric_ref else key
            if metric_name in self.metrics:
                return {"term": term, "metric": self.metrics[metric_name], "glossary": gl_entry}
        if key in self.metrics:
            return {"term": term, "metric": self.metrics[key]}
        return {"term": term, "error": "term_not_found"}

    def resolve_metric_chain(self, metric_name: str) -> list:
        """Resolve T2->T3 dependency chain to get all needed expressions."""
        chain = []
        visited = set()
        def walk(name):
            if name in visited:
                return
            visited.add(name)
            m = self.metrics.get(name)
            if not m:
                return
            for dep in m.get("depends_on", []):
                walk(dep)
            chain.append(m)
        walk(metric_name)
        return chain

    def build_sql(self, metric_name: str, dimensions: list = None,
                  time_filter: str = None, role: str = "analyst") -> str:
        """Build SQL from metric definition."""
        m = self.metrics.get(metric_name)
        if not m:
            return f"-- ERROR: metric '{metric_name}' not found"

        entity_name = m.get("source_entity", "")
        entity = self.entities.get(entity_name, {})
        table = f"{entity.get('database','')}.{entity.get('schema_name','')}.{entity.get('table_name', entity_name)}"

        expr = m.get("aggregation_expression", m.get("formula", metric_name))
        dims_sql = ", ".join(dimensions) if dimensions else ""
        select = f"  {expr} AS {metric_name}"
        if dims_sql:
            select = f"  {dims_sql},\n{select}"

        where_parts = []
        if time_filter:
            where_parts.append(time_filter)

        sql = f"SELECT\n{select}\nFROM {table}"
        if where_parts:
            sql += f"\nWHERE {' AND '.join(where_parts)}"
        if dims_sql:
            sql += f"\nGROUP BY {dims_sql}"

        return sql


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"usage": "python esml_query_engine.py <model_dir> <term>"}))
        sys.exit(0)
    engine = ESMLQueryEngine(sys.argv[1])
    result = engine.resolve_term(sys.argv[2])
    print(json.dumps(result, indent=2, default=str))
