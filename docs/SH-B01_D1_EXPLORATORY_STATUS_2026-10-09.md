# SH-B01 · D1 — Exploratory Research Status

**Status date:** 9 October 2026  
**Research author:** Daniel Alejandro Robles Rionegro  
**Project:** BIOIA / WUOM (BIOIA-WUOM)  
**Domain:** D1 · Forest Management  
**Scientific status:** UNRESOLVED · zero confirmed eligible cases  
**Operational status:** Research paused; D1 screening remains open  
**Custody reference:** v6 operational; v27 isolated and not promoted

> This is an **exploratory research status report**, not a confirmatory research result or an independent scientific validation. It preserves documented literature-screening and methodological work. It does not test, confirm or reject the SH-B01 hypothesis.

## 1. Study identification and preregistration

The retained protocol is **SH-B01 · Empirical Contrast of the Structural Hypothesis: Does Explicit Representation of the Material Base Reduce False Positives of Continuity?**, version **0.3**, attributed to Daniel Alejandro Robles Rionegro / BIOIA-WUOM. Its study design is a systematic comparative review with a retrospective paired diagnostic comparison. [R1]

**Official OSF preregistration reference, identified by the research custodian and retained documentation:** [SH-B01 · OSF overview](https://osf.io/bct9s/overview). The associated DOI is [10.17605/OSF.IO/BCT9S](https://doi.org/10.17605/OSF.IO/BCT9S), as recorded in the later protocol variant and the existing English documentation index.

The OSF overview could not be retrieved during this documentation pass. The registry reference therefore does not establish which local PDF bytes were frozen at preregistration. No independently verifiable, version-specific deposit receipt linking either retained PDF hash to the preregistration date has been recovered. That identity question remains **UNRESOLVED**. The retained local search timestamps do not independently demonstrate submission before search execution, as required by the protocol. [R1, R5]

The publication cutoff remains **8 October 2026**. This report does not amend the hypothesis, six eligibility criteria, evidence chronology, analysis plan or cutoff.

## 2. Research question and confirmatory hypothesis

The protocol asks:

> In human–technical configurations materially dependent on a sustaining base, does explicitly representing the state and constraints of that material base reduce false-positive assessments of continuity compared with evaluations based only on the internal functioning of the configuration?

The confirmatory hypothesis is **FPR(M₂) < FPR(M₁)**; the null hypothesis is **FPR(M₂) ≥ FPR(M₁)**. [R1]

- **M₁:** evaluation based on the observable functioning or performance of positions 1·2·3.
- **M₂:** the same evaluation plus explicit representation of the state, constraints or validated indicators of 0, the material base required to sustain the target function.

The structural notation `0 + 1 + 2 = 3 → 0′` is conceptual, not arithmetic or a demonstrated causal law. SH-B01 tests the narrower empirical proposition about detecting non-continuity; it does not test the notation as a universal law.

The primary comparison is **ΔFPR = FPR(M₁) − FPR(M₂)**, with **FPR(M) = FP(M) / [FP(M) + TN(M)]**. Its denominator consists of cases empirically classified at t₁ as materially non-continuable within the predefined horizon. It is not the number of publications screened. No such comparison has been performed. [R1, R3, R4]

## 3. Scope of the D1 exploratory literature work

D1 concerns forest management, forestry, silviculture, logging and forest restoration. The predefined search combines four conceptual blocks: forest-management activities; yield, harvest, productivity or performance; material conditions such as soil, water, biomass, regeneration or mortality; and monitoring, longitudinal evidence, time series, case studies or trends. English and Spanish publications are eligible, with no lower publication-date limit and the unchanged upper cutoff. [R1]

The discovery sources are **OpenAlex Works** and the **Semantic Scholar Academic Graph**. Crossref may verify bibliographic metadata and DOI identifiers; it is not a third case-discovery source. Deduplication uses normalized DOI first, then normalized title, publication year and first author where a DOI is absent.

Work completed includes discovery-record processing, title/abstract retention, PDF-access attempts, partial and full-document eligibility reviews, and targeted investigation of historical t₀ documentation. These activities concern documentary feasibility and potential eligibility. They do not constitute diagnostic coding of M₁, M₂ or t₁. The empirical case, rather than the publication, is the preregistered unit of analysis. Formal consolidation of publications into cases has not begun. [R1–R4]

## 4. Corpus statistics and documentary provenance

### 4.1 Discovery and retained corpus

The following counts belong to the initial processing and retention stages, not to a confirmatory sample. [R2]

| Stage or measure | Count | Exact documentary source |
| --- | ---: | --- |
| OpenAlex raw records retained after cutoff processing | 14,878 | `SHB01_D1_pre_screening_log.txt`, generated 8 October 2026 |
| Semantic Scholar records retrieved | 9,845 | `SHB01_D1_SemanticScholar_searchlog.txt`, executed 8 October 2026 |
| Combined discovery records | 24,723 | Processing log and `SHB01_D1_combined_raw.csv` |
| Unique records after deduplication | 18,206 | Processing log and `SHB01_D1_unique_corpus.csv` |
| Duplicate groups reported | 6,384 | Processing log; a group count, not the number of records removed |
| Records retained for full-text assessment | 3,255 | `SHB01_D1_fulltext_retained_v1.csv`, screening rule `TA-D1-v1` |
| Initial `POTENTIAL_FULLTEXT` labels | 2,913 | Retained v1 CSV |
| Initial `UNCLEAR_FULLTEXT` labels | 342 | Retained v1 CSV |

The processing log reports exact publication-date resolution for all 1,474 OpenAlex records dated 2026, with zero unresolved dates and zero post-cutoff removals in that processing step. This is a statement about the retained processing record, not an independent revalidation of remote metadata or the external preregistration chronology.

Within the retained v1 corpus, source labels are OpenAlex only **1,453**, Semantic Scholar only **312**, and both sources **1,490**. The original corpus has **17 columns**. Both v6 and isolated v27 retain **3,255 rows and 62 columns**; the original 17 field names, values and row order are preserved. None of these counts establishes case eligibility. [R2–R5]

### 4.2 Operational v6 and isolated v27

The columns below report two distinct historical states. **The v27 figures have not been adopted into v6.** Counts were checked against the corresponding CSVs; checkpoint increment fields remain subject to the custody issues described in Section 8. [R3–R5]

| Recorded documentary measure | v6 operational | v27 isolated |
| --- | ---: | ---: |
| Records with any documentary review | 56 | 58 |
| Records marked `NOT_REVIEWED` | 3,199 | 3,197 |
| Recorded exclusion labels | 11 | 21 |
| `PENDING_T0_DOCUMENTATION` decisions | 27 | 33 |
| `PENDING_FULLTEXT_ASSESSMENT` decisions | 16 | 2 |
| `PENDING_FULL_REPORT` decisions | 1 | 1 |
| Generic `PENDING` decisions | 3,200 | 3,198 |
| Retrieved documents awaiting any review | 95 | 93 |
| Confirmed eligible cases recorded | **0** | **0** |

“Any documentary review” includes initial checks, language or completeness gates and partial readings. It does not mean that every document received a complete six-criterion assessment. The exclusion totals count historical administrative labels; they are not independently validated empirical findings, and they do not incorporate the separate provisional reviews in Section 6.

Access states are identical in v6 and isolated v27. [R3, R4]

| Access state | Records |
| --- | ---: |
| `RETRIEVED` | 150 |
| `RETRIEVED_PARTIAL` | 1 |
| `NO_PDF_URL_IN_OPENALEX` | 1,089 |
| `ACCESS_ATTEMPT_FAILED` | 510 |
| `NOT_ATTEMPTED` | 1,505 |
| Total | **3,255** |

The sequential recovery pass reached row **1,750**. A missing PDF URL, a failed request or an unattempted retrieval is an access state, not an exclusion. A downloaded PDF is not automatically identity-verified, complete, eligible or scientifically validated. [R3]

## 5. Methodological findings and limitations

The documentary work repeatedly encountered a distinction between **material information in an article** and **evidence sufficient to reconstruct a historical continuity assessment**. An article can contain measured soil conditions, mortality, growth, hydrology or production without establishing a real prior M₁, a separable M₂ and a linked later material outcome for the same target function. [R3, R4]

Other retained limitations include:

- Calculated scenarios and model projections do not substitute for an empirically documented later outcome.
- Cross-sectional measurements or retrospective narratives do not by themselves establish a linked t₀→t₁ sequence.
- A material loss, damage indicator or decline is not automatically proof that the defined target function became non-continuable within its frozen horizon.
- If the actual prior assessment already incorporated the relevant material-base information, a hypothetical M₁ cannot be invented to create the comparison.
- Favorable, null and contradictory observations must remain visible. The records preserve such observations alongside adverse changes.
- A translated abstract does not establish that the article body satisfies the English/Spanish language requirement.
- Damaged text extraction and selective visual checks leave numerical transcription and completeness limitations; extracted values have not been globally validated for quantitative coding.

The eligibility reviewers’ exposure to later-outcome information is documented. Eligibility screening must therefore not be presented as blinded confirmatory diagnostic coding. The required information chronology and coding sequence remain to be implemented for any eligible case. [R1, R3, R4]

These are methodological and documentary observations (**MICRO observed**). An improvement in diagnostic FPR, or a broader claim about the Structural Hypothesis (**MACRO inferred**), has not been demonstrated.

## 6. Nine provisional article reviews outside the v27 custody chain

The nine identified assessments concern **D1-P01009, D1-P01012, D1-P01020, D1-P01022, D1-P01025, D1-P01026, D1-P01029, D1-P01031 and D1-P01052**. All remain outside the v27 custody chain. The custodian supplied eight independent Markdown notes dated 9 October 2026 and a filename/size/SHA-256 manifest. All eight files match that manifest; the P01012 copy also matches the previously retained standalone note. This verifies the delivered notes' bytes, not the underlying articles' scientific adequacy or remote/local PDF equivalence. [R6]

### 6.1 Eight separately traceable provisional notes

The following summaries reproduce the existing notes' assessments without reassessing the articles. Every exclusion below is an **unapplied provisional proposal**, limited to the publication described. It is not a confirmed result and does not exclude underlying field data, separately cited studies or associated reports.

| Record and article identity, as recorded | Existing provisional assessment | Reading scope and unresolved limitations |
| --- | --- | --- |
| **D1-P01012 — Pari et al. (2013).** *Preliminary evaluation of a short rotation forestry poplar biomass supply chain in Emilia Romagna Region* | Distinguishes field characterization from calculated harvesting/transport scenarios; records no linked historical continuity diagnosis and later outcome or prior M₁/M₂ pair. Proposed `EXCLUDE_C3_C5_NO_LINKED_MATERIAL_OUTCOME`. | Note reports complete five-page remote PDF inspection with figure/table checks. Work's local PDF was not opened; binary equivalence remains unresolved. |
| **D1-P01020 — Čermák.** *Root layering in a tropical forest after logging (Central Vietnam)* | Compares plots with different logging histories. Preserves the reported absence of a demonstrated logging-intensity effect and the distinction between nonsignificance and absence of effects. Historical plot differences do not establish paired prior diagnoses. Proposed `EXCLUDE_C3_C5_CROSS_SECTIONAL`; the note also retains a document-only non-eligibility formulation pending terminology. | Six-page web text; failed local download, no independent visual verification of figures and no Work PDF hash comparison. **2012 journal issue versus 2013 corpus/web metadata** remains an explicit dating discrepancy. Original t₀ sources were not inspected. |
| **D1-P01022 — Gunaratne et al.** *Screening of woody and shrub legumes for agro-forestry systems based on biomass production, N yield and biological N₂ fixing capacity* | Abstract describes a nine-month field experiment and recommends further work before concluding soil-N maintenance. Retains `PENDING_FULL_REPORT_OR_COMPLETENESS_CONFIRMATION`; the original experiment and associated reports are not excluded. | **Abstract and secondary bibliography only.** Declared one-page PDF not opened; no authenticated longer report recovered. **2013 catalogue date versus 1998 in secondary references; original publication year UNRESOLVED.** |
| **D1-P01025 — Cintra et al. (2013).** *Soil physical restrictions and hydrology regulate stand age and wood biomass turnover rates of Purus–Madeira interfluvial wetlands in Amazonia* | Distinguishes field measurements and retrospective estimates from direct mortality/recruitment observations. Records no linked prior continuity diagnosis and later outcome. Proposed `EXCLUDE_C3_C5_NO_LINKED_MATERIAL_OUTCOME`. | Note reports editorial-PDF methods, data, table and figure inspection. Limits include a small plot sample, retrospective estimates and missing direct demographic data. No comparison with Work's PDF bytes. |
| **D1-P01026 — *Soil-Quality Indicators for Forest Management* (2013), book chapter.** | Synthesis and spatial applications do not establish a historical evaluation followed by a linked material continuity outcome. Proposed `EXCLUDE_C3_C5_NO_LINKED_MATERIAL_OUTCOME`. | Directed reading of author-posted text, with publisher/institutional bibliographic corroboration. Original 62-page PDF and all figures/tables not fully inspected or compared with Work's hash. Cited empirical studies remain separately unevaluated. |
| **D1-P01029 — *Stand age structural dynamics of conifer, mixedwood, and hardwood stands in the boreal forest of central Canada* (2013).** | Chronosequence compares different stands; age differences and management recommendations are not a prior assessment and subsequent outcome in the same unit. Proposed `EXCLUDE_C3_C5_CROSS_SECTIONAL`. | Web-viewer text and selected table/figure checks, without complete visual inspection of all nine pages or Work byte comparison. The separately cited longitudinal study was not assessed or excluded. |
| **D1-P01031 — *Superabsorbent polymer for water management in forestry* (2013).** | Note identifies laboratory measurements and a herbaceous-pasture field trial, rather than forest stands. Proposed `EXCLUDE_DOMAIN_D1`; treatment comparisons are not paired M₁/M₂ continuity diagnoses. | Four-page editorial PDF viewed with figure checks; local download failed. Short-term experimental observations do not establish long-term forest continuity. Work PDF equivalence was not established. |
| **D1-P01052 — *An Analysis on Agroforestry Partnership in Order to Minimize Forest Encroachment (Case Study of “Tumpangsari” for Food Crops at Plantation Forest Concession in Pulau Laut, South Kalimantan)* (2014).** | Proposed `EXCLUDE_LANGUAGE` because the main article is Indonesian despite its English title/abstract. C1–C6 remain not assessed at the language gate; no six-criterion rejection is inferred. | Editorial PDF viewed without local byte comparison. Metadata language conflicts with the reported body language. **CSV DOI `10.19081/jpsl.2014.4.1.1` versus publisher DOI reported as `10.29244/jpsl.4.1.1` remains unresolved.** |

These eight notes are not eight eligible cases or eight validated complete full-text reviews. None has been incorporated into the CSV/checkpoint counts in Section 4.

### 6.2 Ninth assessment: conversation-only provenance

**D1-P01009 — Peringer et al. (2013), *Past and future landscape dynamics in pasture-woodlands of the Swiss Jura Mountains under climate change*.** The custodian identifies this as an earlier conversation-only provisional assessment and reports that no separate Markdown review file was generated or located. No ninth file was supplied, and the original conversation assessment was not accessible in this documentation pass. It is **not a verified ninth file**. [R6]

The supplied locator manifest's brief recap distinguishes aerial-photo observations for 1934–2000 from future simulations and states that no linked prior continuity diagnosis and later material outcome was accredited. That recap is attributed to the manifest; it is not a recovered original adjudication. The assessment's original documentary provenance remains **UNRESOLVED**, and no exclusion or full-reading status is reconstructed from it.

No outside-chain assessment has been merged into v6 or v27, and no v28 has been created.

## 7. Historical t₀ reconstruction and eligibility constraints

The six preregistered eligibility requirements remain: [R1]

1. A specific target function can be defined.
2. A necessary material dependency can be justified independently of the later outcome.
3. Meaningful t₀ and t₁ can be identified.
4. M₁ and M₂ can both be reconstructed using information that existed, or could reasonably have been available, at t₀.
5. The subsequent material outcome is empirically documented.
6. No hypothetical M₁ needs to be invented retrospectively.

The protocol also excludes cases whose real t₀ evaluation already fully incorporated the required explicit material-base assessment when no separable M₁ can be reconstructed.

Information chronology must retain three categories: **A**, genuinely available at t₀; **B**, later sources reproducing measurements or records already existing at t₀; and **C**, later interpretation. Category C cannot construct either model. Before outcome examination, the target function X, necessary material condition Y and horizon Z must be frozen; M₁ and M₂ classifications must then be locked before opening t₁ outcome evidence. [R1]

The existing D1 work illustrates several unresolved reconstruction problems. Polish forest-management program and archive references did not establish a contemporaneous assessment linked to a subsequent outcome in the same unit. A regional forest plan associated with the Czech forest literature was recovered locally, but its existence alone does not establish a real separable M₁. Pen Branch restoration records in isolated later versions include partial thesis inspection and supplementary source or catalogue investigations; cited original planning documentation remains incomplete or unavailable. None of these leads resolved an eligible case’s t₀ reconstruction. [R3–R5]

An indexed catalogue entry, bibliographic record or later quotation must not be described as a recovered and verified original document. Identity, version, date, local unit, content and linguistic admissibility still require documentary evidence. Search-index access and remote-viewer access also do not establish local byte custody.

## 8. Custody and unresolved reconciliation

**v6 remains the sole operational reference. v27 remains isolated. Global custody reconciliation is OPEN with a NO PASS integration verdict.** This custody verdict concerns provenance and metadata; it is not the preregistered scientific NO PASS conclusion. [R5]

The structural audit verified all **21 transitions from v6 to v27**: 3,255 rows, 62 columns, preservation of the 17 original fields and row order, stable unique identifiers, and exactly one changed record per transition with changes restricted to tracking fields. These structural checks do not settle semantic metadata or external document authority.

The retained discrepancy position is:

- **15 confirmed metadata inconsistencies**, documented as proposed errata and not applied to historical files.
- **C06, C08 and C10: three semantic inconsistencies remain UNRESOLVED.** The proposals `[]` and count `0` apply only conditionally under a retrospective reconciliation definition of `new_reviewed_records` that excludes supplementary inspections of already-open records. No original explicit definition proving that meaning has been recovered. The three conflicts are not definitively resolved.
- **C19: external identity of the frozen preregistration PDF remains UNRESOLVED.** Both retained PDFs have ten pages; pages 1–9 match in text and rendered appearance. The later variant adds an OSF bibliographic citation and licence block on page 10. No scientific-rule difference was observed, but the documents differ in content and bytes. Their local or internal dates do not establish an independently dated deposit.

Separate pending evidence comprises **24 remote supplementary links without local byte proof** and **one missing separate JSON access receipt for D1-P00001**. The retained main PDFs passed the existing hash/page-count custody comparison; that does not repair the missing receipt or verify remote supplementary versions. Existing JSON receipts were compared to manifest contents without claiming a historical byte-hash baseline where none existed. [R5]

Additional checkpoint-context observations, including the v24 catalogue-counter definition and stale provenance wording, remain documented separately and uncorrected. Custody checks do not independently validate every numerical claim or scientific interpretation in the historical records.

The later malformed v5 copy is preserved separately. v6 derives from the v5 reconstruction matching the originally recorded verified hash. The first errata layer and validated addendum remain unchanged. Only the addendum’s documentary delivery was closed; global reconciliation and scientific D1 work were not closed. All historical originals remain preserved, with no v27 promotion or new scientific version.

## 9. Scientific outcome at the pause

**SH-B01 remains UNRESOLVED. Zero eligible cases have been confirmed. No FPR comparison has been performed.** [R3–R5]

Full-text screening is incomplete. Formal case consolidation, formal backward/forward citation searching, confirmatory case selection and diagnostic coding have not begun. No paired M₁/M₂ outcome table exists from which the preregistered comparison could be calculated.

Zero confirmed eligible cases does not demonstrate that eligible cases do not exist, that the domain search has been exhausted, or that the hypothesis is true or false. Documentary retrieval and screening progress are not empirical confirmation. This report provides no independent scientific validation.

## 10. Operational pause and possible independent continuation

The research workflow is paused. The v6 checkpoint records an earlier operational interruption of parallel work; incomplete proposals were not incorporated as completed assessments. The present documentation work preserves the record without resuming scientific evaluation. The operational pause does not satisfy the protocol's search-exhaustion or scientific stopping rules. [R1, R3]

A possible independent scientific continuation would require:

1. Establishing the externally frozen protocol reference through independently verifiable file identity, version and timing, and addressing documented custody discrepancies transparently. Originals must remain intact; v6 remains operational unless a separate verified integration is authorized.
2. Recovering the original D1-P01009 conversation assessment if possible and keeping all outside-chain assessments provisional and separate until provenance and authorized handling are documented.
3. Continuing incomplete screening, recovery and historical t₀ reconstruction under the unchanged cutoff, languages and six eligibility criteria; recording access limitations and unresolved cases.
4. Establishing empirical case eligibility and source chronology before formal case consolidation and the prescribed citation-search stage, without inventing prior diagnoses or substituting later interpretation for t₀ evidence.
5. Following the preregistered sequence for freezing X/Y/Z and locking M₁/M₂ before outcome coding. Any protocol change requires a dated, explicit amendment; this status report supplies none.
6. Following the planned independent coding of a preregistered random 25% subset and reporting agreement. Without independent coding, any future confirmatory evidence must be described as internal, not independent scientific validation.

The target remains eight eligible cases per domain across five frozen domains; a D1 shortfall cannot be replaced from another domain. These are conditions and retained protocol obligations, not a claim that continuation has occurred or that v27 may be promoted. [R1, R5]

## 11. References and traceability

The source identifiers below refer to retained originals. Private working records are cited by filename, version and scope; they are not redistributed by this document. No personal filesystem paths, private correspondence or raw unpublished review payloads are included.

**[R1] Protocol and registration reference.** Robles Rionegro, D. A. (2026). *SH-B01 · Empirical Contrast of the Structural Hypothesis: Does Explicit Representation of the Material Base Reduce False Positives of Continuity?* Version 0.3. BIOIA / WUOM. [Repository protocol](./SH_B01_v0.3.pdf); [official OSF overview](https://osf.io/bct9s/overview). Methods were checked against retained protocol text and the existing PDF comparison; external frozen-byte identity remains unresolved.

**[R2] Discovery and retention records.** `SHB01_D1_SemanticScholar_searchlog.txt`; `SHB01_D1_pre_screening_log.txt`; `SHB01_D1_combined_raw.csv`; `SHB01_D1_unique_corpus.csv`; `SHB01_D1_fulltext_retained_v1.csv` (`TA-D1-v1`). Combined, unique and retained row counts were checked locally; remote discovery completeness and exact-date claims were not independently rerun.

**[R3] Operational v6 records.** `SHB01_D1_fulltext_log_v6.csv`; `SHB01_D1_checkpoint_v6.json`; `SHB01_D1_access_and_t0_evidence_v6.json`; `SHB01_D1_avance_v6.md`; `SHB01_D1_custody_verification_v6.json`. Version date: 9 October 2026; publication cutoff: 8 October 2026.

**[R4] Isolated later records.** `SHB01_D1_TRANSFERENCIA_CUSTODIA_v27.zip`, including historical CSVs and checkpoints v6–v27 and the package verifier. The v27 statistics are sourced from `SHB01_D1_fulltext_log_v27.csv` and `SHB01_D1_checkpoint_v27.json`; they are not operationally integrated.

**[R5] Custody and reconciliation records.** `SHB01_D1_custody_integration_v27.json`; `SHB01_D1_checkpoint_errata_v27.json`; `SHB01_D1_checkpoint_errata_clarification_v27.json`; `SHB01_D1_preregistration_pdf_comparison_v27.json`; `temporal_reference_audit.json`; `SHB01_D1_custody_reconciliation_v27.json`; `SHB01_D1_addendum_documentary_closure_v27.json`. The closure is documentary only. The existing reconciliation manifest’s 131 files were checked without modification during this preparation.

**[R6] Outside-chain review records.** `SHB01_D1_8_provisional_reviews_for_Work_2026-10-09.zip` and `SHB01_D1_out_of_chain_reviews_MANIFEST_2026-10-09.md`. Eight original notes follow the filename pattern `SHB01_D1_Pxxxxx_revision_provisional_fuera_cadena.md`, for P01012, P01020, P01022, P01025, P01026, P01029, P01031 and P01052. Their hashes and sizes match the supplied manifest. Article titles and provisional findings in Section 6 are attributed to these notes, without new article assessment. D1-P01009 is identified only by the custodian's clarification and locator recap; no ninth original file or original conversation adjudication was authenticated. Bibliographic conflicts and reading limits are retained explicitly.

### Selected SHA-256 custody anchors

These hashes identify retained bytes; they do not establish scientific validity or an external deposit date.

| Artifact | SHA-256 |
| --- | --- |
| Retained v1 CSV | `167057838f5882de2dac4152eb67656ab99037fc756db79957d720f3062d581a` |
| Operational v6 CSV | `347d588bb654e762d7bbac8b7e48c577ff8e5ec943eb92fed1830bb7af0166d7` |
| Isolated v27 CSV | `1130ed7bb0f22ef7c77dc3e5a64bda68ba4df595b5a6f8bc7f0197e102be6393` |
| First independent errata layer | `87a12bcce2ddf9deae0cbdd6500284f8f376a0e52a7cca77d5dc2ed931f28dc5` |
| Validated clarification addendum | `f07c49ae45272d07ef1d92d7674c253fc88e0d4b2d556c559b603460b4c1f4e6` |
| Global reconciliation report | `490a1cf06675b8dca887e826c3d4ac5642d8fc47b72840d9391592bbd6e0f1d3` |
| Standalone provisional P01012 note | `f8da92b78eb68fafd995a7806928016e4883e660f06dc9c1181ee60926afbeb7` |
| Supplied eight-review convenience ZIP | `e86662d7d0ec8288408c8dd8b6c949b2381023deb3cd6d293b4bd17b3083940a` |

**D1 OPEN · SH-B01 UNRESOLVED · ZERO CONFIRMED ELIGIBLE CASES.**
