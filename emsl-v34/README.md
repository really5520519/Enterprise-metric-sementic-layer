# Enterprise Semantic Metrics Layer (ESML) v3.3

> A semantic interchange protocol for enterprise metrics — dependency-ordered layers, progressive federation, adaptive governance.

## Legal notice

ESML is an **independent, original work**. It is not derived from, affiliated with, or endorsed by the Open Semantic Interchange (OSI) initiative. See [NOTICE](NOTICE) for details.

| Scope | License |
|-------|---------|
| Code (`.py`, `.yaml`, `.json`) | [Apache License 2.0](LICENSE) |
| Documentation (`.md`) | [CC BY-SA 4.0](license-docs/LICENSE-docs) |

## Core positioning

**Not a platform, not a BI tool, not an ETL engine — a protocol layer.**

ESML is a **semantic metrics bus** — it sits between data platforms (Snowflake, Databricks, BigQuery) and consumers (AI Agents, BI tools, custom apps). It translates business questions into data operations, pushes operations to the platform where data lives, and attaches quality and governance tags to results.

## Component overview

| Component | Count | Description |
|-----------|-------|-------------|
| Layers | 8 (L0-L7) | Dependency-ordered semantic model layers |
| Metric tiers | 3 (T3-T2-T1) | Atomic - derived - composite business metrics |
| Governance mechanisms | 5 (M1-M5) | Progressive compliance, enablement, degradation, feedback, adaptive |
| Workflows | 14 (W1-W14) | Domain + enterprise + scaffold + contribute + demo query |
| Cross-domain skills | 2+ | Federation-level analytic skills (cost-per-hire ROI, workforce optimization) |

## Layer architecture (dependency-ordered)

Each layer may ONLY reference layers with smaller numbers. Zero circular dependencies.

| Layer | Directory | Name | Depends on | Schema file | Key concepts | Cross-layer refs |
|-------|-----------|------|------------|-------------|-------------|------------------|
| L0 | ontology/ | Ontology | nothing | entity_classes, relationship_types, measurement_types | TransactionEvent, MasterData, FinancialRecord; placed_by, contains; currency, percentage | - L2 objects ref ontology_class |
| L1 | entities/ | Entity (+quality) | L0 | table_catalog, lineage_graph, virtual_views, quality/*.yaml | ODS-DWD-DWS-ADS layers; upstream/downstream; profile, freshness, versioning, provenance | - L2 binds entities; - L3 refs entity_ref; - L4 refs entity |
| L2 | objects/ | Object | L0, L1 | object_template | entity_bindings (primary+enrichments); properties (PII); behaviors (method triggers); relationships | - L4 via metric refs; - L5 via behaviors |
| L3 | dimensions/ | Dimension | L1 | time, org_hierarchy, geo_hierarchy | hierarchy levels; SCD Type 0/1/2; shared=true; join_protocol per domain | - L4 metrics group by dims |
| L4 | metrics/ | Metric | L1, L3 | t3_atomic, t2_derived, t1_composite | T3: SUM/COUNT; T2: formula+depends_on; T1: cross-source+external+methods | - L5 via method_ref; - L7 via metric_ref |
| L5 | analytic_methods/ | Method | L1, L2, L4 | plugin_schema | category; trigger_intents; models (SQL/Python); output format | - L2 triggers via behaviors |
| L6 | governance/ | Governance | L1-L5, Identity | classification, sla, access, audit, M1-M5 | RBAC; column masking; RLS; 5 mechanisms (progressive, enablement, degradation, feedback, adaptive) | Applies rules to ALL lower layers |
| L7 | knowledge/ | Knowledge | L4, L5 | glossary, conflict_registry, golden_definitions | terms+aliases; disambiguation; golden_definition; vector search | - L4 via metric_ref |

### Cross-cutting concerns (no layer number)

| Module | Directory | Consumed by |
|--------|-----------|-------------|
| Identity | identity/ | L2 (owner), L6 (RBAC), Skill (user context) |
| Domain Registry | domain-registry/ | Skill (W8/W9/W10), L3 (shared dims), L4 (cross-domain) |

## Metric tier convention

| Tier | Label | Dependency | Examples |
|------|-------|-----------|----------|
| T3 | Atomic | None | SUM(gmv), COUNT(order_id) |
| T2 | Derived | depends_on T3 | refund_rate, aov, attrition_rate |
| T1 | Composite | T2+T3 + external + methods | ROI, LTV, CAC, revenue_per_employee |

## Repository structure

```
enterprise-semantic-metrics-layer/
+-- architecture/                    Architecture definition
|   +-- progressive-federation.yaml  Three-tier federation model
+-- enterprise/                    Tier 1: Enterprise shared foundation
|   +-- manifest.yaml
|   +-- ontology/                    L0
|   +-- entities/ + quality/         L1
|   +-- objects/                     L2
|   +-- dimensions/                  L3
|   +-- metrics/                     L4 (T3/T2/T1)
|   +-- analytic_methods/            L5
|   +-- governance/                  L6 + 5 mechanisms
|   +-- knowledge/                   L7
|   +-- identity/                    Cross-cutting
+-- domain-registry/                 Cross-cutting: domain pointers
+-- domains/                         Tier 2: Autonomous domains
|   +-- hr/                          (L2 governed, 7-layer)
|   +-- finance/                     (L2 governed, 7-layer)
|   +-- sales/                       (L2 governed, 7-layer)
+-- skills/                          Tier 3: Agent orchestration
|   +-- SKILL.md                     W1-W14 workflows
|   +-- cross-domain/                Federation-level analytic skills
|   +-- scripts/                     Engine + loader + governance
+-- maturity-model/                  L0-L3 maturity definitions
+-- license-docs/                    CC BY-SA 4.0 for documentation
```

## Five governance mechanisms

| # | Mechanism | Purpose |
|---|-----------|---------|
| M1 | Progressive Compliance | L0-L3, each level unlocks capabilities |
| M2 | Domain Enablement | Auto-scaffold + mapping wizard + compliance advisor |
| M3 | Graceful Degradation | warn_and_serve - block_with_alternative |
| M4 | Feedback Loop | Domain patterns - enterprise standard proposals |
| M5 | Adaptive Governance | metric_tier x domain_level - enforcement mode |

## Display hint system (v3.4)

ESML carries optional visualization hints at three granularity levels:

| Level | ESML location | Answers | Example |
|-------|---------------|---------|---------|
| Chart | L4 display_hint | "What shape is this metric?" | attrition_rate: time_series, up_is_bad, benchmark 8% |
| Dashboard | L2 dashboard_hint | "How do metrics compose?" | employee object: 4 scorecards + 2 trends + heatmap + table |
| Storyline | L7 storylines | "How to tell a data story?" | attrition analysis: baseline, trend, segment, root cause, predict, recommend |

These are hints (suggestions), not requirements. A voice assistant ignores chart_type. A CLI prints tables. Each consumer renders according to its own capabilities.

## Quick start

```bash
git clone https://github.com/YOUR_ORG/enterprise-semantic-metrics-layer.git
cd enterprise-semantic-metrics-layer
pip install duckdb pyyaml pytest
pytest tests/ -v
```

## Performance

Below 20 metrics: flat structure wins. Above 20 metrics: layered structure wins — selective loading keeps token cost constant while flat degrades linearly.
