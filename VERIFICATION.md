# Source Verification Log

Last audit: **September 9, 2026.**

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

## Corrected in this audit

| Entry | Problem | Action |
| :--- | :--- | :--- |
| `SMART_2025_STUDY` | Attributed to "Kieling, C., et al. (2024)" with a fabricated title, volume 38, article 100842, and a DOI that does not resolve to the paper. Design given as quasi-experimental. | Replaced with the verified Goodyear et al. (2025) record. Design corrected to cross-sectional observational; findings and limitation rewritten to match the published study. |
| `UNESCO_2023_GEM` | DOI `10.54675/QBKP7378` returns 404 at doi.org and is registered with neither Crossref nor DataCite. UNESCO lists no DOI for this report. | Replaced with the UNESDOC ARK URL `ark:/48223/pf0000385723`, which resolves. |
| `DUTCH_2025_EVAL` | Stored `rijksoverheid.nl` URL returned 404. Title and ministry attribution could not be verified. Reported percentages were rounded upward. | Replaced with a description of the evaluation's actual scope (317 secondary school leaders, 313 primary schools, 12 focus groups, reported March 2025) and a resolving Eurydice summary URL. Figures corrected to ~75% concentration, ~59% climate, ~28% academic gain. Limitation now notes these are school-leader self-reports. |
| `DEL_2018_READING_META` | Synthesis text described `g = −0.21` as an informational-reading figure. | Corrected to the overall effect, with the genre moderator stated explicitly. |

---

## Pending — needs full-text access

Both papers are paywalled with no open-access copy (checked via Unpaywall). The **citations are verified**; only the subgroup figures drawn from them are outstanding.

### 1. `TAM_2011_META` — the support-versus-direct-instruction split

The matrix states cognitive construction `g ≈ 0.42` against direct delivery `g ≈ 0.16`.

The 0.42 figure is consistent with the paper's reported effect for technology used to *support* instruction. **The 0.16 figure is doubtful.** The paper's overall random-effects mean is 0.35, and a 0.42/0.16 split is difficult to reconcile with that mean unless the sample is heavily unbalanced toward the higher group. A direct-instruction figure nearer 0.30 would sit more naturally against 0.35.

Do not cite 0.16 publicly until it has been checked against pp. 4–28 of the published article.

### 2. `ZHE_2016_ONE_TO_ONE` — the subject-area effect sizes

The matrix states writing `d = 0.20`, science `d = 0.25`, mathematics `d = 0.17`.

The abstract confirms only that the meta-analysis of 10 studies found "significantly positive average effect sizes in English, writing, mathematics, and science" without publishing the values. The writing and science figures are plausible; the mathematics figure may be 0.16 rather than 0.17. The effect-size metric should also be confirmed, since the matrix labels these `d` while the other entries use Hedges' `g`.

### 3. `LAUSD_2015_IPAD_AUDIT` — the $1.3B and 48-hour figures

The LAUSD Common Core Technology Project and its collapse are well documented, and the `edtech.lausd.org` URL resolves. The specific $1.3 billion bond figure and the "bypass in 48 hours" detail were not traced to the Inspector General report itself in this audit.

---

## Note on the failure pattern

Three of nine entries carried fabricated or unresolvable identifiers, and all three were sources whose metadata is hard to verify from memory: two government grey-literature evaluations and one recent journal article. Every entry with a long-established DOI from a major journal checked out perfectly on the first pass.

That is the characteristic signature of generated citations — accurate where verification is easy, invented where it is hard. Any future addition to this matrix should be resolved against its DOI before it is committed, and grey literature should carry a URL that has been fetched, not inferred.
