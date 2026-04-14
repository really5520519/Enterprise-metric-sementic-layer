
<div align="center">

# Enterprise-Semantic-Metrics-Layer

### The Open Semantic Protocol for Enterprise Metric Systems

**From metric chaos to semantic truth — in 8 layers.**

[![ESML Version](https://img.shields.io/badge/ESML-v3.4-blue?style=flat-square)](#changelog)
[![License: Code](https://img.shields.io/badge/Code-Apache_2.0-green?style=flat-square)](LICENSE)
[![License: Docs](https://img.shields.io/badge/Docs-CC_BY--SA_4.0-orange?style=flat-square)](license-docs/LICENSE-docs)
[![Architecture](https://img.shields.io/badge/Architecture-Progressive_Federation-purple?style=flat-square)](#three-tier-federation-architecture)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

*Every enterprise has metrics. Almost none have a metric system.*
*每个企业都有指标，但几乎没有企业拥有指标体系。*

---

**ESML** is a vendor-neutral, AI-native semantic protocol that transforms fragmented metric silos into a governed, federated, dependency-safe metric system.
It is not a BI tool. It is not a metric store. It is not an ETL engine. It is the **missing type system** for enterprise metrics — a semantic interchange bus that sits between your data platforms (Snowflake, Databricks, BigQuery) and every AI Agent, dashboard, and decision-maker that consumes your numbers.

The one thing it does: **translate business questions into data operations, push operations to the platform where data lives, attach quality and governance tags to results.**

</div>

---

## Legal notice

ESML is an **independent, original work**. It is not derived from, affiliated with, or endorsed by the Open Semantic Interchange (OSI) initiative or any of its member organizations. See [NOTICE](NOTICE) for details.

| Scope | License |
|---|---|
| Code (`.py`, `.yaml`, `.json`) | [Apache License 2.0](LICENSE) |
| Documentation (`.md`) | [CC BY-SA 4.0](license-docs/LICENSE-docs) |

---

## Why this exists

The enterprise metric landscape in 2026 looks like this:

| What you have | What it costs you |
|---|---|
| 6+ HR SaaS tools, each defining "attrition rate" differently | AI Agents hallucinate metrics; dashboards contradict each other |
| Metrics buried in dbt models with no semantic contract | One engineer leaves → 40% of metric lineage becomes oral tradition |
| T1/T2/T3 tiering exists on a wiki page no one reads | Finance says ROI is X, Marketing says it's Y — both are "correct" |
| Governance = a Confluence page titled "Metric Standards" last edited 2021 | Shadow metrics multiply faster than governed ones |
| No consolidation rules for group-level metrics | Subsidiary revenue is SUM'd without IC elimination — CFO sees fiction |

**The root cause is not tooling. It is the absence of a shared semantic contract.**

dbt solved the transformation layer. The semantic layer wars (MetricFlow, Cube, Looker) solved query federation. But nobody solved the **metric system itself** — the ontology, the dependency chain, the governance lifecycle, the causal metric trees, the knowledge graph that tells an AI Agent *which* metric to use, *why*, and *with what caveats*.

**ESML v3.4 solves this.** It is the first open standard that treats enterprise metrics as a complete, layered, governable system — not just a list of YAML definitions. It adds three levels of visualization hints (chart, dashboard, storyline) so consumers from Claude to Tableau to voice assistants know how to present results.

---

## Component overview

| Component | Count | Description |
|---|---|---|
| Layers | 8 (L0–L7) | Dependency-ordered semantic model layers |
| Metric tiers | 3 (T3→T2→T1) | Atomic → derived → composite business metrics |
| Governance mechanisms | 5 (M1–M5) | Progressive compliance, enablement, degradation, feedback, adaptive |
| Workflows | 14 (W1–W14) | Domain + enterprise + scaffold + contribute + demo query |
| Display hint levels | 3 | Chart (L4) → dashboard (L2) → storyline (L7) |
| Cross-domain skills | 2+ | Federation-level analytic skills (cost-per-hire ROI, workforce optimization) |
| Enterprise files | 82 | Across 3 tiers (enterprise + 3 domains + skills) |

---

## Architecture at a glance
<p align="center">
  <img src="https://github.com/really5520519/Enterprise-Holo-Metrics-OSI/blob/main/architecture-before-after.png" alt="Before: SaaS metric chaos → After: OSI v3.2 semantic federation" width="100%"/>
</p>
<details>
<summary><strong>Can't see the PNG? Text-based architecture summary</strong></summary>

```
BEFORE                                AFTER (ESML v3.4)
──────────────────────                ──────────────────────
Workday  SAP SF  ADP                  L0 Ontology (type system)
   ↕  ↗  ↕  ↘  ↕                     L1 Entity + quality metadata
BambooHR  Greenhouse  Lattice         L2 Business object + dashboard hints
                                      L3 Shared dimensions
"Attrition rate" × 3 definitions      L4 Metrics (T3→T2→T1) + chart hints
"Headcount" = FTE? HC? Contractor?    L5 Analytic methods (DuPont, talent profile)
No lineage. No audit. No truth.       L6 Governance (5 mechanisms + consolidation)
                                      L7 Knowledge + storylines + golden definitions
AI Agent: "Which metric do I use?"    ┊
         → 🤷                         Cross-cutting: Identity │ Domain Registry

                                      AI Agent: "attrition_rate = T2, L4, governed ✓,
                                                 chart: line, alert: up_is_bad,
                                                 storyline: 7-step root cause analysis"
```

</details>

---

## The 8-layer dependency chain

ESML v3.4 organizes every semantic concept into 8 strictly-ordered layers. **No layer may reference a layer above it.** This is not a suggestion — it is a compile-time constraint enforced by schema validation.

> 类型系统先于一切。砖先于房间。度量先于治理。
> *The type system precedes everything. Bricks before rooms. Metrics before governance.*

| Layer | Name | Directory | Depends on | What it defines | v3.4 additions |
|:---:|---|---|---|---|---|
| **L0** | Ontology | `ontology/` | *nothing* | Type system: entity classes, relation semantics, measurement standards | — |
| **L1** | Entity (+Quality) | `entities/` | L0 | Physical tables, lineage, virtual views, freshness & provenance metadata | — |
| **L2** | Object | `objects/` | L0, L1 | Business object encapsulation: entity binding, properties, behaviors | **`dashboard_hint`**: multi-metric spatial composition |
| **L3** | Dimension | `dimensions/` | L1 | Shared dimensions with hierarchy and SCD Type 2 versioning | — |
| **L4** | Metric | `metrics/` | L1, L3 | T3 atomic → T2 derived → T1 composite metric tiers | **`display_hint`**: chart type, alert direction, benchmarks |
| **L5** | Method | `analytic_methods/` | L1, L2, L4 | Analysis plugins: attribution, DuPont causal tree, talent profiling, forecasting | DuPont decomposition (multiplicative), talent feature engineering |
| **L6** | Governance | `governance/` | L1–L5, Identity | Governance policies + 5 enforcement mechanisms | Consolidation rules, accounting standard enforcement |
| **L7** | Knowledge | `knowledge/` | L4, L5 | Glossary, disambiguation, golden definitions, conflict registry | **`storylines`**: multi-step narrative arcs, arbitration process |

### Cross-cutting concerns

These modules serve multiple layers and therefore **do not occupy a layer number** — placing them in the stack would create circular dependencies.

| Module | Directory | Consumed by |
|---|---|---|
| **Identity** | `identity/` | L2 (owner), L6 (RBAC), Skill (user context) |
| **Domain Registry** | `domain-registry/` | Skill (W8/W9/W10), L3 (shared dims), L4 (cross-domain metrics) |

### Key design decisions

| Decision | Rationale |
|---|---|
| Entity (L1) before Object (L2) | You need bricks before rooms — physical data assets must exist before business objects can bind to them |
| Quality merged into L1 | Freshness, provenance, and completeness are metadata *about* the entity — not a separate governance concern |
| Ontology promoted to L0 | The type system must exist before anything can reference it — it is the axiom layer |
| Identity & Federation as cross-cutting | They serve L2, L3, L4, L6, and the Skill layer simultaneously — any single-layer placement would be a lie |
| Display hints are optional | A voice assistant ignores `chart_type`. A CLI prints tables. Hints describe data shape, never prescribe rendering engine |
| Storylines in L7, not a new layer | "How to narrate a data story" is domain knowledge — the same category as glossary terms and disambiguation rules |

---

## Metric tier system

ESML enforces a strict **T3 → T2 → T1** dependency hierarchy. Every metric declares its tier, and the dependency validator guarantees that no metric at tier N depends on a metric at tier N-1 or lower.

| Tier | Label | Dependency rule | Examples |
|:---:|---|---|---|
| **T3** | 原子指标 (Atomic) | Depends on nothing | `SUM(gmv)`, `COUNT(order_id)`, `SUM(salary_cost)`, `SUM(debit_amount)` |
| **T2** | 派生指标 (Derived) | `depends_on: [T3]` only | `refund_rate`, `aov`, `attrition_rate`, `net_profit_margin`, `asset_turnover` |
| **T1** | 复合业务指标 (Composite) | T2 + T3 + external + methods | `ROI`, `LTV`, `CAC`, `return_on_equity` (DuPont: margin × turnover × leverage) |

**Why T1 = top, T3 = bottom**: T1 is the CEO-level north star metric (strategic). T3 is the base building block (raw aggregation). This aligns with enterprise metric hierarchy conventions where "tier 1" means "strategic level."

**Causal vs. independent composites**: ROE is `net_profit_margin × asset_turnover × equity_multiplier` — a **multiplicative** causal tree, not three independent composites. ESML declares `decomposition: multiplicative` to distinguish this from additive composition. Changing one factor directly affects the root metric. The DuPont method (L5) provides both three-factor and five-factor SQL models.

**Why this matters for AI Agents**: When an Agent asks "What is our attrition rate?", ESML doesn't just return a number. It returns the metric's tier (T2), its dependencies (`terminations`, `headcount` — both T3), its governance status, its quality score, its display hint (`chart_type: time_series, alert_direction: up_is_bad, benchmark: 8%`), and its disambiguation context. The Agent can *reason* about the metric, not just parrot it.

---

## Display hint system (v3.4)

ESML carries optional visualization hints at three granularity levels. These describe **data shape and business context**, never rendering engine or visual style.

> The right analogy: HTML's `<input type="email">` doesn't force a specific keyboard — it hints that an email keyboard would be appropriate. The browser decides. Similarly, ESML's `display_hint: time_series` doesn't force a line chart — it hints that the result is a temporal sequence. The consumer decides.

| Level | ESML location | Answers | Example |
|---|---|---|---|
| **Chart** | L4 `display_hint` | "What shape is this metric?" | `attrition_rate`: time_series, up_is_bad, benchmark 8% |
| **Dashboard** | L2 `dashboard_hint` | "How do metrics compose?" | employee object: 4 scorecards + 2 trends + heatmap + detail table |
| **Storyline** | L7 `storylines` | "How to tell a data story?" | attrition analysis: baseline → trend → segment → root cause → predict → recommend |

### How different consumers use these hints

| Consumer | Chart hint | Dashboard hint | Storyline hint |
|---|---|---|---|
| AI Agent (Claude) | Recharts component | React grid layout | Multi-turn chat with charts per step |
| BI Tool (Tableau) | Native chart type | Dashboard tab | Story tab |
| Slack Bot | Sparkline in message | Card with mini-charts | Thread: 1 message per step |
| Voice Assistant | "10%, trending up" | Skip (no screen) | Narrate steps sequentially |
| PDF Report | Static chart | Page layout with grid | Chapter per step |
| API Consumer | Ignore (raw data) | JSON: `sections[]` | JSON: `steps[]` |

### What ESML does NOT prescribe

- Rendering engine (Recharts / Chart.js / ECharts / VizQL)
- Color palette or styling
- Animation or interaction patterns
- Responsive breakpoints

---

## Three-tier federation architecture

ESML uses a **Progressive Federation** model. Instead of mandating enterprise-wide adoption on day one (which kills every governance initiative), it allows domains to join the federation incrementally — starting with basic entity registration (L1) and progressively adopting higher layers as their maturity grows.

```
enterprise-semantic-metrics-layer/
├── architecture/                    Architecture definition
│   └── progressive-federation.yaml  Three-tier federation model
│
├── enterprise/                    ← Tier 1: Enterprise shared foundation
│   ├── manifest.yaml                 (single source of semantic truth)
│   ├── ontology/                  L0  Type system
│   ├── entities/ + quality/       L1  Entities + quality metadata
│   ├── objects/                   L2  Business objects + dashboard hints
│   ├── dimensions/                L3  Shared dimensions (time, org, geo)
│   ├── metrics/                   L4  Metric schemas (T3/T2/T1) + chart hints
│   ├── analytic_methods/          L5  Analysis plugins
│   ├── governance/                L6  Governance (5 mechanisms)
│   ├── knowledge/                 L7  Glossary + golden definitions + conflict registry
│   └── identity/                  ✦   Cross-cutting (RBAC, ownership)
│
├── domain-registry/               ← Cross-cutting: domain pointers
│   ├── hr.yaml
│   ├── finance.yaml
│   └── sales.yaml
│
├── domains/                       ← Tier 2: Autonomous domain layers
│   ├── hr/                           (L2 governed — talent profiling, 3 storylines)
│   ├── finance/                      (L2 governed — ASC 606, DuPont causal tree, consolidation)
│   └── sales/                        (L2 governed — GMV/AOV/refund, channel attribution)
│
├── skills/                        ← Tier 3: AI Agent orchestrator
│   ├── SKILL.md                      W1–W14 skill workflows
│   ├── cross-domain/                 Federation-level analytic skills
│   │   ├── cost-per-hire-roi.yaml
│   │   └── workforce-cost-optimization.yaml
│   └── scripts/                      Engine + loader + governance gate
│       ├── esml_query_engine.py      Term resolver + metric DAG + SQL builder
│       ├── esml_feishu_loader.py     Feishu/Sheets MCP → DuckDB loader
│       └── esml_governance_gate.py   Role check + PII masking + RLS injection
│
├── maturity-model/                L0–L3 maturity level definitions
├── CHANGELOG.md                   Version history (v3.1 → v3.4)
├── NOTICE                         Legal independence declaration
├── LICENSE                        Apache 2.0 (code)
└── license-docs/LICENSE-docs      CC BY-SA 4.0 (documentation)
```

**Tier 1 (Enterprise)**: The shared semantic foundation. Owned by the data platform team. Contains the canonical type system, shared dimensions, golden definitions, and enterprise-level metric schemas. This is the constitution — it changes slowly, deliberately, through governance.

**Tier 2 (Domains)**: Autonomous domain-specific layers. Each domain owns its own metrics and objects but inherits from the enterprise layer. Domains declare their maturity level (L1 operational → L2 governed), and governance enforcement adapts accordingly via M5 Adaptive Governance.

**Tier 3 (Skills)**: The AI Agent orchestrator. Workflows W1–W14 handle everything from metric discovery to cross-domain federation to natural language disambiguation to interactive demo queries via Feishu/Sheets MCP.

---

## Five governance mechanisms

Governance in ESML is not a gate. It is a gradient — from gentle guidance to strict enforcement, calibrated to each domain's maturity level.

| # | Mechanism | What it does | In practice |
|:---:|---|---|---|
| **M1** | Progressive Compliance | Unlock capabilities as you mature: L0→L1→L2→L3 | A domain at L1 can register entities; at L3, it can publish shared dimensions |
| **M2** | Domain Enablement | Auto-scaffold new domains with templates, mapping wizards, compliance advisors | `esml_scaffold.py` generates the full directory structure with starter YAML |
| **M3** | Graceful Degradation | When a dependency is missing or stale, degrade gracefully instead of failing silently | `warn_and_serve` → `serve_with_caveat` → `block_with_alternative` |
| **M4** | Feedback Loop | Patterns emerging in domains bubble up as enterprise standard proposals | If 3+ domains define `time_to_fill`, it becomes a candidate for enterprise L4 promotion |
| **M5** | Adaptive Governance | Enforcement mode = f(metric_tier × domain_level) | T1 metric in L2 domain = strict enforcement; T3 metric in L1 domain = advisory only |

### Consolidation governance (v3.4)

Group-level metrics are **not simple SUM of subsidiaries**. ESML enforces consolidation rules at L6:

| Elimination type | Rule |
|---|---|
| Revenue elimination | Subsidiary A sells to B → remove from both group revenue AND COGS |
| AR/AP netting | Intercompany receivable/payable must net to zero per counterparty pair |
| Intercompany profit | Unrealized profit on inventory transfers eliminated at group level |
| Minority interest | Non-controlling interest share = net_income × (1 - ownership_pct) |

---

## Cross-domain semantic governance (v3.4)

### Golden definitions — who owns the truth?

When two domains define the same term differently, ESML doesn't pick a winner arbitrarily. It follows the **originator principle**: the domain that originates the data owns the golden definition.

| Term | Owner | Golden definition | Other domains |
|---|---|---|---|
| **revenue** | Finance | GAAP recognized revenue (ASC 606) | Sales: `net_revenue` (non-GAAP, superset) |
| **headcount** | HR | Active FTE on payroll, excl. contractors | Finance: `fte_count` (includes contractor fraction) |
| **customer** | *under review* | — | Sales: "completed purchase" vs Marketing: "registered user" |

Each golden definition includes reconciliation formulas (e.g., `fte_count = headcount + SUM(contractor.fte_factor)`) so domains can translate between their local metric and the enterprise truth.

### Conflict registry

Active semantic conflicts are tracked, assigned, and resolved through a formal arbitration process:

| ID | Term | Status | Domains | Impact |
|---|---|---|---|---|
| CONF-001 | customer | Active | Sales, Marketing | "Customer acquisition cost" returns different results per domain |
| CONF-002 | cost | Active | Finance, HR | HR `labor_cost` may exclude stock-based compensation |
| CONF-R001 | revenue | Resolved | Sales, Finance | Sales renamed to `net_revenue`, tagged non-GAAP |
| CONF-R002 | headcount | Resolved | HR, Finance | Finance uses `fte_count` with explicit reconciliation formula |

---

## Accounting standard awareness (v3.4)

ESML is the first semantic layer to carry **accounting standard metadata** on financial metrics:

```yaml
recognized_revenue:
  accounting_standard:
    current: { standard: ASC_606, effective_date: "2018-01-01" }
    prior:   { standard: ASC_605, note: "risks-and-rewards model" }
    comparability: "Cross-standard comparison requires restated figures"
```

When a query spans the ASC 605/606 boundary (pre/post 2018), the governance gate automatically attaches a warning: *"This query spans an accounting standard change. Results may not be directly comparable."*

---

## Query walkthrough example

**Question**: "上个月的GMV是多少，按渠道拆分"

**Key insight**: ESML layers are NOT loaded sequentially L0→L7. They are traversed **on demand in reverse**: L7 (term resolution) → L4 (metric formula) → L2 (object bindings) → L1 (physical table) → L6 (governance) → SQL execution.

| Step | Layer | What the agent reads | What it learns |
|---|---|---|---|
| 0 | Gateway | SKILL.md intent router | "是多少" → W6 Query. metric=GMV, dims=渠道, time=上个月 |
| 1 | L7 Knowledge | `knowledge/glossary.yaml` | GMV has 2 meanings (ad/financial), default → `sales_metrics#total_gmv` |
| 2 | L4 Metrics | `metrics/sales_metrics.yaml` | GMV is T3, expression=`SUM(gmv)`, `display_hint: time_series` |
| 3 | L2 Objects | `objects/order_object.yaml` | "渠道" → enrichment `dim_channel` via `channel_id` JOIN |
| 4 | L1 Entities | `entities/fact_sales.yaml` | Physical table: `PROD_DB.DWS_SALES.FACT_SALES_D` |
| 5 | L6 Governance | `governance/sales_access.yaml` | role=analyst OK, inject RLS: `WHERE region = user_region()` |
| 6 | Builder | `esml_query_engine.py` | Assemble `SELECT SUM(gmv) FROM fact_sales JOIN dim_channel ...` |
| 7 | Execute | Snowflake connection | 4 rows, 1.2s. quality_warning: stale data (3d > 30min SLA) |

---

## Performance

| Scale | Flat (single YAML) | Layered (ESML) |
|---|---|---|
| 5 metrics | ~800 tokens, 1 tool call | ~2,400 tokens, 5 tool calls |
| 20 metrics | ~2,000 tokens (crossover) | ~2,400 tokens (crossover) |
| 50 metrics | ~5,000 tokens, context pressure | ~2,400 tokens, selective load |
| 100+ metrics | Hits context limit | ~2,400 tokens, O(1) via object index |

**Crossover point: ~20 metrics.** Below 20, flat wins. Above 20, layered wins — selective loading keeps token cost constant while flat degrades linearly.

---

## For data architects

If you are evaluating ESML against existing approaches, here is how we compare on the dimensions that matter:

| Dimension | dbt Semantic Layer | Cube / Looker | ESML v3.4 |
|---|---|---|---|
| Metric definition | YAML in dbt project | YAML/SDL | YAML with L0–L7 dependency chain |
| Ontology / type system | None | None | **L0 — first-class** |
| Metric tiering (T1/T2/T3) | Manual convention | Not supported | **Schema-enforced** |
| Causal metric trees | Not supported | Not supported | **L5 DuPont decomposition (multiplicative)** |
| Entity quality metadata | External (Great Expectations) | External | **L1 — merged** |
| Governance lifecycle | Not in scope | Not in scope | **L6 — 5 mechanisms + consolidation** |
| Cross-domain federation | Not in scope | Limited | **Progressive Federation + golden definitions** |
| AI Agent semantic contract | None | None | **L7 knowledge graph + storylines** |
| Visualization hints | Not supported | Limited (chart types) | **Three-level: chart + dashboard + storyline** |
| SCD Type 2 dimensions | Model-level | Not supported | **L3 — native** |
| Analytic method plugins | Not supported | Not supported | **L5 — attribution, DuPont, talent profiling, forecast** |
| Accounting standard awareness | Not supported | Not supported | **ASC 606 metadata + cross-period warnings** |
| Adoption model | All-or-nothing | All-or-nothing | **Progressive (L1→L3 maturity)** |

---

## Quick start

```bash
# Clone the repo
git clone https://github.com/YOUR_ORG/enterprise-semantic-metrics-layer.git
cd enterprise-semantic-metrics-layer

# Install minimal dependencies
pip install duckdb pyyaml pytest

# Run the verification suite (27 test cases, 5 dimensions)
pytest tests/ -v

# Query engine demo
python skills/scripts/esml_query_engine.py . headcount
python skills/scripts/esml_governance_gate.py . analyst attrition_rate
```

---

## 14 workflows

| W# | Name | Scope | Trigger phrases |
|---|---|---|---|
| W1 | Create | Domain | "create model", "new semantic model" |
| W2 | Validate | Domain | "validate", "lint", "check" |
| W3 | Audit | Domain | "audit", "health check" |
| W4 | Translate | Domain | "convert to Snowflake", "export dbt" |
| W5 | Compare | Domain | "diff", "what changed" |
| W6 | Query | Domain | "what is [metric]", "how much" |
| W7 | Govern | Domain | "data quality", "access policy" |
| W8 | Enterprise Query | Cross-domain | "revenue per employee", "CAC" |
| W9 | Cross-Domain Audit | Enterprise | "any conflicts?" |
| W10 | Enterprise Governance | Enterprise | "who can see what?" |
| W11 | Compliance Check | Domain | "what level am I?" |
| W12 | Scaffold | Domain | "generate from database" |
| W13 | Contribute | Enterprise | "propose as standard" |
| W14 | Demo Query | Demo | Connects Feishu/Sheets MCP + DuckDB for live verification |

---

## Design philosophy

> 1. **Dependency is truth.** If you can't draw the dependency, you don't understand the metric.
> 2. **Progressive, not prescriptive.** Start at L1. Grow at your own pace. Governance adapts to you.
> 3. **AI Agents are first-class citizens.** Every layer emits a semantic contract that an Agent can consume without human mediation.
> 4. **Federation over centralization.** Domains own their metrics. The enterprise owns the contract.
> 5. **Bricks before rooms, rooms before buildings.** L0 → L1 → L2 → ... → L7. No shortcuts.
> 6. **Hints, not mandates.** Display hints describe data shape — the consumer decides how to render.
> 7. **Semantic truth has an owner.** Every golden definition has exactly one authoritative domain. Conflicts are tracked, arbitrated, and resolved — not ignored.

---

## Roadmap

- [x] ESML v3.1 — Enterprise Federated Architecture (L0–L7 + cross-cutting + T3→T2→T1)
- [x] ESML v3.2 — Layer reclassification (entity before object, ontology to L0, quality merged into L1)
- [x] ESML v3.3 — Legal independence, hub architecture, 3 engine scripts, 2 cross-domain skills
- [x] ESML v3.4 — Display hint system (chart + dashboard + storyline), DuPont causal tree, talent profiling, golden definitions, conflict registry, consolidation rules, accounting standard awareness
- [ ] Verification suite: DuckDB + pytest (27 test cases, 5 dimensions)
- [ ] OpenClaw + Feishu Sheet integration demo (7 verification questions)
- [ ] Finance domain starter (Enterprise-Finance-Metrics-ESML)
- [ ] E-commerce domain starter (Enterprise-Ecommerce-Metrics-ESML)
- [ ] `esml` CLI tool for validation, scaffolding, and promotion
- [ ] Agent Skill SDK (Python + TypeScript)
- [ ] ESML-to-MetricFlow / ESML-to-Cube bridge adapters
- [ ] Vector index auto-generation for L7 knowledge layer
- [ ] Governance dashboard (React + ESML API)

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

| Version | Theme | Key change |
|---|---|---|
| v3.4 | Display hints + domain depth | Chart/dashboard/storyline hints, DuPont causal tree, talent profiling, golden definitions, conflict registry, consolidation rules |
| v3.3 | Legal independence | Renamed to ESML, Apache 2.0 + CC BY-SA 4.0, hub architecture, 3 engine scripts |
| v3.2 | Layer reclassification | Entity before object, ontology to L0, quality merged into L1, zero dependency violations |
| v3.1 | Federation architecture | Three-tier federation, 5 governance mechanisms, T3→T2→T1, 13 workflows |

---

## Contributing

ESML is an open standard. We welcome contributions from data architects, data engineers, analytics engineers, and AI practitioners.

**Especially wanted:**
- Domain-specific metric schemas (supply chain, marketing, product, R&D)
- Governance mechanism implementations
- Agent skill workflows and storyline templates
- Bridge adapters to existing semantic layers (MetricFlow, Cube, Looker)
- Display hint patterns for new chart types and dashboard layouts
- Accounting standard metadata for IFRS, J-GAAP, and other jurisdictions

---

## License

| Scope | License |
|---|---|
| Code (`.py`, `.yaml`, `.json`) | Apache License 2.0 |
| Documentation (`.md`) | CC BY-SA 4.0 |

---

<div align="center">

*Built for the data architects who believe that metrics deserve the same rigor as code.*
*为那些相信指标体系应当与代码同等严谨的数据架构师而生。*

**[Read the changelog →](CHANGELOG.md)** · **[Browse the YAML →](enterprise/)** · **[Star this repo ⭐](https://github.com/YOUR_ORG/enterprise-semantic-metrics-layer)**

</div>
