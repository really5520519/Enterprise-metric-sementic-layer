<div align="center">

# Enterprise Metrics Semantic Layer (EMSL) v3.3
<div align="center">

### The Open Semantic Layer for Enterprise Metric Systems

**From metric chaos to semantic truth — in 8 layers.**

[![EMSL Version](https://img.shields.io/badge/EMSL-v3.3-blue?style=flat-square)](https://github.com/Enterprise-HoloMetrics-EMSL)
[![License](https://img.shields.io/badge/License-Apache2.0--0-green?style=flat-square)](LICENSE)
[![Architecture](https://img.shields.io/badge/Architecture-Progressive_Federation-purple?style=flat-square)](#progressive-federation-architecture)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

*Every enterprise has metrics. Almost none have a metric system.*
*每个企业都有指标，但几乎没有企业拥有指标体系。*

---

**Enterprise-HoloMetrics-EMSL** is a vendor-neutral, AI-native semantic standard that transforms fragmented SaaS metric silos into a governed, federated, dependency-safe metric system. 
It is not a BI tool. It is not a metric store. It is the **missing type system** for enterprise metrics — the layer that sits between your data warehouse and every AI Agent, dashboard, and decision-maker that consumes your numbers.

</div>

---

## Why this exists

The enterprise metric landscape in 2026 looks like this:

| What you have | What it costs you |
|---|---|
| 6+ HR SaaS tools, each defining "attrition rate" differently | AI Agents hallucinate metrics; dashboards contradict each other |
| Metrics buried in dbt models with no semantic contract | One engineer leaves → 40% of metric lineage becomes oral tradition |
| T1/T2/T3 tiering exists on a wiki page no one reads | Finance says ROI is X, Marketing says it's Y — both are "correct" |
| Governance = a Confluence page titled "Metric Standards" last edited 2021 | Shadow metrics multiply faster than governed ones |

**The root cause is not tooling. It is the absence of a shared semantic contract.**

dbt solved the transformation layer. The semantic layer wars (MetricFlow, Cube, Looker) solved query federation. But nobody solved the **metric system itself** — the ontology, the dependency chain, the governance lifecycle, the knowledge graph that tells an AI Agent *which* metric to use, *why*, and *with what caveats*.

**EMSL v3.2 solves this.** It is the first open standard that treats enterprise metrics as a complete, layered, governable system — not just a list of YAML definitions.

---

## Architecture at a glance

> *A senior data engineer should be able to look at this once and know exactly where every concept lives.*

<p align="center">
  <img src="https://github.com/really5520519/Enterprise-Holo-Metrics-osi/blob/main/architecture-before-after.png" alt="Before: SaaS metric chaos → After: osi v3.2 semantic federation" width="100%"/>
</p>
<details>
<summary><strong>Can't see the PNG? Text-based architecture summary</strong></summary>

```

BEFORE                              AFTER
─────────────────────────           ─────────────────────────
Workday  SAP SF  ADP                L0 Ontology (type system)
   ↕  ↗  ↕  ↘  ↕                   L1 Entity + quality
BambooHR  Greenhouse  Lattice       L2 Business object
                                    L3 Shared dimensions
"Attrition rate" × 3 definitions    L4 Metrics (T3→T2→T1)
"Headcount" = FTE? HC? Contractor?  L5 Analytic methods
No lineage. No audit. No truth.     L6 Governance (5 mechanisms)
                                    L7 Knowledge graph
AI Agent: "Which metric do I use?"  ┊
         → 🤷                       Cross-cutting: Identity │ Federation

                                    AI Agent: "attrition_rate = T2, L4, governed ✓"
```

</details>

---

> A semantic interchange protocol for enterprise metrics — dependency-ordered layers, progressive federation, adaptive governance.

## Core pEMSLtioning
**Not a platform, not a BI tool, not an ETL engine — a protocol layer.**
ESML is a **semantic metrics bus** — it sits between data platforms (Snowflake, Databricks, BigQuery) and consumers (AI Agents, BI tools, custom apps). It translates business questions into data operations, pushes operations to the platform where data lives, and attaches quality and governance tags to results.
## Component overview
| Component | Count | Description |
|-----------|-------|-------------|
| Layers | 8 (L0-L7) | Dependency-ordered semantic model layers |
| Metric tiers | 3 (T3-T2-T1) | Atomic - derived - compEMSLte business metrics |
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
| L4 | metrics/ | Metric | L1, L3 | t3_atomic, t2_derived, t1_compEMSLte | T3: SUM/COUNT; T2: formula+depends_on; T1: cross-source+external+methods | - L5 via method_ref; - L7 via metric_ref |
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
| T1 | CompEMSLte | T2+T3 + external + methods | ROI, LTV, CAC, revenue_per_employee |
## RepEMSLtory structure
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
| # | Mechanism | Purpose | # | Mechanism | Purpose |
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

## Legal notice
ESML is an **independent, original work**. It is not derived from, affiliated with, or endorsed by the Open Semantic Interchange (EMSL) initiative. See [NOTICE](NOTICE) for details.
| Scope | License |
|-------|---------|
| Code (`.py`, `.yaml`, `.json`) | [Apache License 2.0](LICENSE) |
| Documentation (`.md`) | [CC BY-SA 4.0](license-docs/LICENSE-docs) |
