# Source Verification Log

Last audit: **September 9, 2026** (second pass, same day, resolved the pending full-text items).

Every entry in `evidence-matrix.json` was checked against its identifier. This log records what was verified, how, and what remains open. Update it whenever an entry is added or a pending item is resolved.

---

## Method

- **DOIs** resolved through DOI content negotiation (`Accept: application/vnd.citationstyles.csl+json`) against Crossref, with DataCite as a fallback. Author, year, journal, volume, and pages compared field by field against the stored citation.
- **Grey literature** checked by resolving the stored URL with a browser user agent. A 403 under a default user agent is bot-blocking, not breakage, and was re-tested before being treated as a failure.
- **Effect sizes** checked against the published abstract or full text where openly available. Where the paper is paywalled with no open-access copy, the figure is recorded below as pending rather than treated as verified.

---

## Verified against Crossref — exact match

| Entry | Checked | Result |
| :--- | :--- | :--- |
| `TAM_2011_META` | 10.3102/0034654310393361 | Tamim, Bernard, Borokhovski, Abrami, Schmid (2011), *Review of Educational Research* 81, 4–28. All fields match. |
| `ZHE_2016_ONE_TO_ONE` | 10.3102/0034654316628645 | Zheng, Warschauer, Lin, Chang (2016), *Review of Educational Research* 86, 1052–1084. All fields match. |
| `ODG_2020_REVIEW` | 10.1111/jcpp.13190 | Odgers & Jensen (2020), *Journal of Child Psychology and Psychiatry* 61, 336–348. All fields match. |
| `DEL_2018_READING_META` | 10.1016/j.edurev.2018.09.003 | Delgado, Vargas, Ackerman, Salmerón (2018), *Educational Research Review* 25, 23–38. All fields match. |
| `SMART_2025_STUDY` | 10.1016/j.lanepe.2025.101211 | Goodyear et al. (2025), *The Lancet Regional Health – Europe* 51, 101211. All fields match. |

## Verified effect sizes

| Claim | Source text | Status |
| :--- | :--- | :--- |
| Delgado print advantage `g = −0.21` | "Both designs yielded the same advantage of paper over digital reading (Hedge's g = −0.21; dc = −0.21)." | **Confirmed.** Note this is the *overall* effect across genres, not an informational-text-specific figure. Genre is a moderator: the advantage held for informational and mixed texts but not for narrative-only studies. |
| Tamim overall mean `0.35` | "The random effects mean effect size of 0.35 was significantly different from zero." Validation subset: 0.33. | **Confirmed** from the published abstract. |
| Tamim support of instruction `0.42` | Table 3, ES = 0.42, k = 10. | **Confirmed** against the full text. |
| Tamim direct instruction | Table 3, ES = 0.31, k = 15. | **Matrix was wrong.** It listed 0.16. Corrected to 0.31. Arithmetic check: 0.42(10) + 0.31(15) weight-averages to 0.354, matching the published overall mean of 0.35. A 0.42/0.16 split cannot produce that mean. |

## Corrected in this audit

| Entry | Problem | Action |
| :--- | :--- | :--- |
| `SMART_2025_STUDY` | Attributed to "Kieling, C., et al. (2024)" with a fabricated title, volume 38, article 100842, and a DOI that does not resolve to the paper. Design given as quasi-experimental. | Replaced with the verified Goodyear et al. (2025) record. Design corrected to cross-sectional observational; findings and limitation rewritten to match the published study. |
| `UNESCO_2023_GEM` | DOI `10.54675/QBKP7378` returns 404 at doi.org and is registered with neither Crossref nor DataCite. UNESCO lists no DOI for this report. | Replaced with the UNESDOC ARK URL `ark:/48223/pf0000385723`, which resolves. |
| `DUTCH_2025_EVAL` | Stored `rijksoverheid.nl` URL returned 404. Title and ministry attribution could not be verified. Reported percentages were rounded upward. | Replaced with a description of the evaluation's actual scope (317 secondary school leaders, 313 primary schools, 12 focus groups, reported March 2025) and a resolving Eurydice summary URL. Figures corrected to ~75% concentration, ~59% climate, ~28% academic gain. Limitation now notes these are school-leader self-reports. |
| `DEL_2018_READING_META` | Synthesis text described `g = −0.21` as an informational-reading figure. | Corrected to the overall effect, with the genre moderator stated explicitly. |

---

## Resolved in the second pass

### `TAM_2011_META` — contradicted and corrected

Full text obtained. **Table 3 reports ES = 0.42 (k = 10) for technology used to support instruction and ES = 0.31 (k = 15) for direct instruction.** The matrix had listed 0.16 for the direct-instruction subgroup, understating it by 0.15 standardized units.

The characterization built on that number — that direct delivery yields "negligible or negative outcomes" — was also wrong and has been removed everywhere it appeared. Both subgroups show moderate positive effects. The defensible finding is that supporting cognitive construction outperforms direct delivery by a meaningful margin, not that direct delivery is inert.

Corrected in `evidence-matrix.md` (executive synthesis and comparative table), `evidence-matrix.json`, `index.html` (diagnostic narrative and data object), and `AGENT_HANDOFF.md`.

---

## Still pending

### 1. `ZHE_2016_ONE_TO_ONE` — subject-area values not accessible

The published abstract confirms only that the meta-analysis of 10 studies found "significantly positive average effect sizes in English, writing, mathematics, and science." It does not publish the values, and the results table was not accessible. The paper is paywalled with no open-access copy.

The previously listed values (ELA 0.15, writing 0.20, mathematics 0.17, science 0.25) and their `d` metric label are now **marked unverified in the matrix** rather than presented as sourced figures. Do not restore them from a media summary — only from the article's results table.

### 2. `LAUSD_2015_IPAD_AUDIT` — figures not traced to the cited report

The specific 2015 Inspector General report was not obtained from the LAUSD OIG index, and neither the **$1.3 billion** figure nor the **48-hour bypass** timing could be traced to it.

Contemporary press coverage describes a roughly $1.3-billion iPads-for-all plan and reports that students at several campuses removed security filters, but neither establishes OIG attribution, and no accessible source states the 48-hour timing.

Both claims are now flagged in the matrix as not attributable to the OIG report. Either locate the passage in the original document or re-cite to an accessible source that states the figure. The 48-hour detail should be deleted outright unless a primary source is found.

---

## Note on the failure pattern

Three of nine entries carried fabricated or unresolvable identifiers, and a fourth carried a fabricated effect size. All of them were claims whose verification is hard: two government grey-literature evaluations, one recent journal article, and a moderator estimate buried in a paywalled table. Every entry with a long-established DOI from a major journal checked out perfectly on the first pass, and every figure printed in an accessible abstract was accurate.

That is the characteristic signature of generated content — accurate where verification is easy, invented where it is hard. Two rules follow. Resolve every new entry against its DOI before committing it. And treat any numeric claim drawn from behind a paywall as unverified until someone has opened the table, no matter how plausible it looks next to the numbers around it.
