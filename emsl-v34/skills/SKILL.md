---
name: esml-enterprise-semantic
description: >
  ESML v3.3 Enterprise Semantic Metrics Layer skill. L0-L7 dependency-ordered layers,
  2 cross-cutting concerns, T3-T2-T1 metric tiers, 14 workflows, progressive federation.
version: 3.4.0
metadata:
  openclaw: { emoji: "📊", requires: { bins: [python3], pip: [duckdb, pyyaml] } }
---

# ESML Enterprise Semantic Metrics Layer Skill v3.3

## Layer registry (dependency-ordered)

| # | Layer | depends_on |
|---|-------|-----------|
| L0 | Ontology | nothing |
| L1 | Entity (+quality) | L0 |
| L2 | Object | L0, L1 |
| L3 | Dimension | L1 |
| L4 | Metric | L1, L3 |
| L5 | Method | L1, L2, L4 |
| L6 | Governance | L1-L5, Identity |
| L7 | Knowledge | L4, L5 |

Cross-cutting: Identity, Domain Registry

## Workflows

| W# | Name | Scope | Trigger phrases |
|----|------|-------|-----------------|
| W1 | Create | Domain | "create model", "new semantic model" |
| W2 | Validate | Domain | "validate", "lint", "check" |
| W3 | Audit | Domain | "audit", "health check" |
| W4 | Translate | Domain | "convert to Snowflake", "export dbt" |
| W5 | Compare | Domain | "diff", "what changed" |
| W6 | Query | Domain | "what is [metric]", "how much" |
| W7 | Govern | Domain | "data quality", "access" |
| W8 | Enterprise Query | Cross-domain | "revenue per employee", "CAC" |
| W9 | Cross-Domain Audit | Enterprise | "any conflicts?" |
| W10 | Enterprise Governance | Enterprise | "who can see what?" |
| W11 | Compliance Check | Domain | "what level am I?" |
| W12 | Scaffold | Domain | "generate from database" |
| W13 | Contribute | Enterprise | "propose as standard" |
| W14 | Demo Query | Demo | "demo mode", connects Feishu/Sheets MCP + DuckDB |

## W14 Demo Query workflow

When Feishu Sheet or Google Sheets MCP is connected:
1. `esml_feishu_loader.py` reads all sheet tabs → creates DuckDB tables
2. User asks natural language question
3. `esml_query_engine.py` resolves term → metric → SQL
4. `esml_governance_gate.py` checks role + applies masking/RLS
5. DuckDB executes SQL
6. Agent formats response with quality tags

## Display hint system (v3.4)

Three levels of visualization hints, all optional:

| Level | Location | Scope | Field |
|-------|----------|-------|-------|
| Chart | L4 Metric | Single metric output shape | display_hint |
| Dashboard | L2 Object | Multi-metric spatial layout | dashboard_hint |
| Storyline | L7 Knowledge | Multi-step narrative arc | storylines |

When responding to queries, the engine attaches display_metadata to results:
1. Read metric's display_hint (chart_type, alert_direction, benchmark)
2. If query involves an object, check object's dashboard_hint for section layout
3. If user intent matches a storyline trigger, follow the step sequence
4. Auto-infer chart type from result column structure (12 deterministic rules)

## Query resolution

Single-domain: L7→L4(T3→T2→T1)→L2(object)→L1(entity)→L6(governance)→SQL
Cross-domain: glossary→domain-registry→per-domain W6→CTE join→governance merge
