# ESML Changelog

All notable changes to the Enterprise Semantic Metrics Layer.

## v3.4.0 — Display hint system

**Problem solved:** Consumers (AI Agents, BI tools, voice assistants) had no guidance on how to visualize query results. Each consumer guessed chart types independently, leading to inconsistent user experiences.

**Changes:**
- L4 Metrics: added `display_hint` field — chart_type, alert_direction, benchmark, comparison_periods, sparkline
- L2 Objects: added `dashboard_hint` field — multi-metric spatial composition (sections, layouts, drill_paths)
- L7 Knowledge: added `storylines` field — multi-step narrative arcs (problem_diagnosis, periodic_review, deep_dive)
- Architecture: documented three-level hint system (chart/dashboard/storyline) with consumer behavior matrix
- SKILL.md: added W14 Demo Query workflow
- All three domains (HR, Finance, Sales) enriched with display hints across L4/L2/L7
- Cross-domain skills: added display_hint with quadrant analysis and scatter plots

**Design principle:** Hints are optional suggestions, never requirements. A voice assistant ignores chart_type. A CLI prints tables. Each consumer reads what it can use.

---

## v3.3.0 — Legal independence and hub architecture

**Problem solved:** The project shared naming and structural patterns with the OSI specification, creating potential legal ambiguity. Also needed a hub architecture for multi-repo domain management.

**Changes:**
- Renamed from "Enterprise OSI v3.2" to "Enterprise Semantic Metrics Layer (ESML)"
- Added Apache 2.0 license (code) + CC BY-SA 4.0 license (docs), physically separated
- Added NOTICE file declaring independent origin
- Added copyright header + knowledge sources + proprietary-data disclaimer to all 80 files
- Restructured to hub architecture: architecture/, enterprise/, domain-registry/, domains/, skills/, maturity-model/
- Added 3 new engine scripts: esml_feishu_loader.py, esml_query_engine.py, esml_governance_gate.py
- Added 2 cross-domain federation skills: cost-per-hire-roi, workforce-cost-optimization
- Renamed all `osi_*` references to `esml_*`
- Replaced OSI-specific field names (ai_context, vendor_extensions) with original ESML naming

**Legal status:** Zero OSI spec field overlap. All knowledge sources are public (ISO standards, textbooks, SEC filings, open-source documentation).

---

## v3.2.0 — Layer reclassification and dependency correction

**Problem solved:** The original L1-L7 ordering had a critical dependency violation — L1 Objects referenced L2 Entities "upward," and 4 modules (ontology, identity, quality, federation) had no layer assignment.

**Changes:**
- Ontology promoted to L0 (type system foundation, zero dependencies)
- Entities promoted to L1, Objects demoted to L2 (you need bricks before rooms)
- Quality merged INTO L1 Entity as sub-directory (entity metadata, not separate layer)
- Identity and Federation reclassified as cross-cutting concerns (no layer number)
- Final architecture: L0 Ontology -> L1 Entity(+quality) -> L2 Object -> L3 Dimension -> L4 Metric -> L5 Method -> L6 Governance -> L7 Knowledge + 2 cross-cutting
- Dependency chain verified: zero violations (every layer only references lower-numbered layers)
- Setup-time vs query-time separation clarified: Adapter/Accelerator/Checker run ONCE at initialization, W6/W8 workflows use pre-built cached artifacts

**Key insight:** The test for "layer vs cross-cutting" is whether a module has a fixed position in the dependency chain. Identity serves L2, L6, and Skill simultaneously — it has no single position, so it's cross-cutting.

---

## v3.1.0 — Enterprise federated architecture

**Problem solved:** Single-domain v3.0 could not handle cross-domain queries ("revenue per employee" needs Sales + HR), term collisions ("revenue" means different things in Sales vs Finance), or centralized governance across autonomous domains.

**Changes:**
- Three-tier federation: enterprise shared layer + autonomous domain projects + skill orchestrator
- 5 governance mechanisms: M1 Progressive Compliance (L0-L3), M2 Domain Enablement (scaffold/wizard/advisor), M3 Graceful Degradation (warn/caveat/block), M4 Feedback Loop (domain->enterprise proposals), M5 Adaptive Governance (tier x level matrix)
- Cross-domain metrics with federation CTE (per-domain W6 -> join via shared dimensions)
- Enterprise glossary with golden definitions and conflict registry
- T3 atomic -> T2 derived -> T1 composite metric tier convention (reversed from v3.0)
- 13 workflows (W1-W13) covering domain + enterprise + scaffold + contribute
- 3 starter domains: Sales (L2 governed), Finance (L2 governed), HR (L1 operational)
- Quality separated from governance: "data IS stale" (fact, L1) vs "data SHOULD be fresh" (rule, L6)

**Key design:** Each governance level UNLOCKS capabilities, not just adds restrictions. L0 gets single-domain query. L1 gets cross-domain draft. L2 gets production cross-domain + heartbeat. L3 gets enterprise featuring.
