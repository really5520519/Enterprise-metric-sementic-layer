#!/usr/bin/env python3
"""ESML Governance Gate — role check + PII masking + RLS injection."""
# Copyright (c) 2026 [YOUR LEGAL ENTITY]
# Licensed under the Apache License, Version 2.0
# This file is an original work and is NOT derived from
# the Open Semantic Interchange (OSI) specification.
#
# Knowledge sources:
# - RBAC model (NIST SP 800-162, public standard)
# - Column masking patterns (Snowflake documentation, public)
# - Row-level security (PostgreSQL RLS documentation, public)
# - Adaptive governance matrix (COSO ERM Framework, public summary)
#
# This file contains NO proprietary information from any employer or client.

import yaml
import os
import json
import sys


class GovernanceGate:
    """Enforces access control, PII masking, and row-level security."""

    def __init__(self, model_dir: str):
        self.model_dir = model_dir
        self.access_rules = {}
        self.pii_rules = []
        self.rls_rules = []
        self.governance_matrix = {}
        self._load_governance()

    def _load_governance(self):
        """Load all governance YAML at setup time."""
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
                if "access_policies" in data or "access_policy" in data:
                    ap = data.get("access_policies", data.get("access_policy", {}))
                    for rp in ap.get("role_permissions", []):
                        self.access_rules[rp["role"]] = rp
                    for pm in ap.get("pii_masking", []):
                        self.pii_rules.append(pm)
                    for rls in ap.get("row_level_security", []):
                        self.rls_rules.append(rls)
                if "governance_matrix" in data:
                    self.governance_matrix = data["governance_matrix"]

    def check_access(self, role: str, metric_name: str) -> dict:
        """Check if role can access this metric."""
        rule = self.access_rules.get(role)
        if not rule:
            return {"allowed": False, "reason": f"role '{role}' not found"}
        allowed = rule.get("allowed_metrics", [])
        if allowed == ["*"] or "*" in allowed or metric_name in allowed:
            return {"allowed": True, "pii_access": rule.get("pii_access", False)}
        return {"allowed": False, "reason": f"metric '{metric_name}' not in allowed list for role '{role}'"}

    def get_pii_masking(self, columns: list, role: str) -> dict:
        """Return masking policies for columns based on role."""
        rule = self.access_rules.get(role, {})
        if rule.get("pii_access", False):
            return {}
        masked = {}
        for pr in self.pii_rules:
            col = pr.get("column", pr.get("field", ""))
            if col in columns:
                masked[col] = pr.get("policy", pr.get("masking", "redact"))
        return masked

    def get_rls_condition(self, entity_name: str) -> str:
        """Return RLS WHERE clause for an entity."""
        for rls in self.rls_rules:
            if rls.get("entity") == entity_name:
                return rls.get("condition", "")
        return ""

    def get_enforcement_mode(self, metric_tier: str, compliance_level: str) -> str:
        """Lookup adaptive governance matrix."""
        tier_key = f"{metric_tier}_{'composite' if metric_tier=='T1' else 'derived' if metric_tier=='T2' else 'atomic'}"
        row = self.governance_matrix.get(tier_key, {})
        if isinstance(row, str):
            return row
        return "advisory"


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(json.dumps({"usage": "python esml_governance_gate.py <model_dir> <role> <metric>"}))
        sys.exit(0)
    gate = GovernanceGate(sys.argv[1])
    result = gate.check_access(sys.argv[2], sys.argv[3])
    print(json.dumps(result, indent=2))
