# Agent Handoff: K–12 Device Policy & Pedagogical Friction Evidence Hub

**Date:** September 1, 2026  
**Author / Principal Investigator:** Micah J. Miner, CETL, Ed.S.  
**Target Repositories:**  
- `minerclass/k12-device-policy-evidence-hub` (New Canonical Evidence Hub)
- `minerclass/screen-time-wrong-question` (CoSN Companion & *The Pouch and the Bypass*)
- `minerclass/minerclass.github.io` (Root Public Ecosystem Hub)

---

## 1. Objective

This document coordinates the completed architecture, empirical research protocols, multi-hub ecosystem integration, and deployment configuration for the **K–12 Device Policy & Pedagogical Friction Evidence Hub**. It serves as the primary orientation and review document for incoming coding agents, researchers, and doctoral reviewers.

---

## 2. Project Context & Theoretical Spine

Micah J. Miner is Director of Innovation and Technology for Beach Park CCSD 3 and an Ed.D. candidate at National Louis University. His research investigates **pedagogical friction in the age of generative AI** and the intersection of educational technology policy, learning sciences, and media ecology.

### Core Evaluative Premise
**An infrastructural intervention (e.g., phone pouches, locker mandates, or 1:1 Chromebook cart transitions) alters the physical channel of access; it does not dictate the pedagogical design of the learning environment.**

```
                        ┌─────────────────────────────────────────────────────────┐
                        │              INFRASTRUCTURAL INTERVENTION               │
                        │   (Phone Pouches, Locker Policies, Cart Deployments)    │
                        └───────────────────────────┬─────────────────────────────┘
                                                    │
                                   Does hardware removal alone
                                   restore cognitive struggle?
                                                    │
                                    ┌───────────────┴───────────────┐
                                    ▼                               ▼
                      ┌───────────────────────────┐   ┌───────────────────────────┐
                      │   THE UNADDRESSED BYPASS  │   │    PRODUCTIVE FRICTION    │
                      │  Algorithmic offloading & │   │ Intentional noetic/agency │
                      │  passive screen delivery  │   │  struggle embedded into   │
                      │  on district Chromebooks  │   │   instructional design    │
                      └───────────────────────────┘   └───────────────────────────┘
```

### Key Theoretical Constructs
1. **The 1:1 Expansion & Reversal Symmetry (Cuban's Theorem Applied Twice):**
   * *The Expansion:* 15 years of 1:1 laptop/Chromebook adoption converted paper worksheets into digital PDFs without fundamentally changing teacher-led pedagogy.
   * *The Reversal:* The current international wave of phone bans and cart rollbacks converts digital PDFs back into paper worksheets without inherently elevating cognitive demand.
2. **The Four Dimensions of Friction:**
   * **Noetic:** Cognitive resistance required for deep linear reading, conceptual encoding, and sensemaking.
   * **Rhetorical:** Discursive resistance required for spoken dialogue, thesis defense, and unassisted drafting.
   * **Existential:** Student agency, self-efficacy, and identity cultivated through navigating unresolved difficulty.
   * **Infrastructural:** District policy guardrails, procurement standards, device containment, and network filtering.
3. **The Haidt–Odgers–Horvath Triangulation:**
   * **Jonathan Haidt (*The Anxious Generation*):** Highlights population-level developmental displacement (play, sleep, attention).
   * **Candice Odgers (Methodological Counterweight):** Highlights within-person variance, near-zero average associations ($r \approx -0.05$), and the reality that digital tools replicate and amplify pre-existing offline vulnerabilities.
   * **Jared Cooney Horvath (*The Digital Delusion*):** Emphasizes task-level cognitive offloading, handwriting benefits, and shallow digital reading habits.
4. **Empirical Meta-Analytic Baselines:**
   * **Tamim et al. (2011) 2nd-Order Meta-Analysis:** Technology supporting student cognitive construction yields $g = 0.42$; technology used for direct delivery/drill yields $g = 0.16$.
   * **Zheng, Warschauer et al. (2016) 1:1 Meta-Analysis:** 1:1 laptop programs achieved significant positive effect sizes in writing ($d=0.20$), science ($d=0.25$), math ($d=0.17$), and ELA ($d=0.15$), complicating simplistic claims that classroom devices are inherently harmful.
   * **Delgado et al. (2018) Reading Meta-Analysis:** Robust print advantage ($g = -0.21$) for informational text comprehension over digital screens.
   * **Dutch Phone Ban (2025) vs. UK SMART Schools (2024):** Divergence between high perceived classroom calm (75%) and flat measured academic/mental health outcomes, demonstrating *unproductive success* at the system policy level.

---

## 3. Files & Repository Architecture

### Primary Hub: `c:\Users\mminer\OneDrive - bpd3.org\Desktop\Research\k12-device-policy-evidence-hub`
Remote: `https://github.com/minerclass/k12-device-policy-evidence-hub`

| File Path | Description & Role |
| :--- | :--- |
| [`index.html`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/index.html) | Interactive single-page application for GitHub Pages with responsive styling, 4 diagnostics, evidence matrix, policy audit, 13-hub collection navigator, deck mode, and printable board memo generator. |
| [`search-protocol.md`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/search-protocol.md) | The complete **Agent Search & Evaluation Protocol** with query vectors (A, B, C), inclusion/exclusion filters, and JSON extraction schema. |
| [`evidence-matrix.json`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/evidence-matrix.json) | Structured benchmark empirical dataset conforming to the JSON schema. |
| [`evidence-matrix.md`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/evidence-matrix.md) | APA 7-formatted literature synthesis and comparative analysis table. |
| [`github-collection-map.md`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/github-collection-map.md) | Strategic architecture mapping the four connected scholarship hubs and audience pathways. |
| [`README.md`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/README.md) | Repository documentation, deployment guide, and audience pathways. |
| [`scripts/fetch_openalex_evidence.py`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/scripts/fetch_openalex_evidence.py) | Standalone Python 3 script executing scholarly vector queries via the OpenAlex API. |
| [`.github/workflows/deploy.yml`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/.github/workflows/deploy.yml) | GitHub Actions deployment workflow with explicit token permissions (`pages: write`, `id-token: write`). |
| [`LICENSE`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/LICENSE) & [`.nojekyll`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/.nojekyll) | Licensing (CC BY-NC-SA 4.0 & MIT) and GitHub Pages static routing flag. |

---

## 4. Multi-Hub Integration Map

The evidence hub connects across Micah Miner’s four primary public scholarship hubs:

| Hub Cluster | Key Repositories Linked | Presentation & Practical Role |
| :--- | :--- | :--- |
| **✍️ Writing Hub** | • `writing-sites-hub`<br>• `screen-time-wrong-question`<br>• `pouch-and-bypass`<br>• `When-Output-Looks-Like-Learning` | Long-form policy essays, CoSN companion articles, and theoretical reframes. |
| **🎤 Conference Hub** | • `pedagogical-friction-iste-ascd-decks`<br>• `nlu_ai-ed-conference-pres26`<br>• `screen-practice-compass` | ISTE/ASCD slide decks, interactive workshop reflection tools, and **🖥️ Deck Mode**. |
| **🎓 Dissertation Hub** | • `dissertation-overview`<br>• `genAI-ML-pedagogy-of-friction-site`<br>• `genAI-ML-the-technologizing-word-site`<br>• `nlu-doccolloquium-may26` | Doctoral proposal gateway, Ongian media ecology, and qualitative-dominant convergent mixed methods. |
| **🎮 Gaming Hubs** | • `games-hub`<br>• `orality_game` (*Keeper of the Word*)<br>• `source_game` (*Keeper of the Source*)<br>• `friction_game` (*Friction Lab*)<br>• `historical-inquiry-friction` | Interactive simulations making media ecology, source judgment, and friction playable. |
| **🏛️ District Leadership** | • `bpd3-tech-review`<br>• `bpd3-privacy-training`<br>• Beach Park CCSD 3 Governance | Software vetting rubrics, SOPPA/FERPA compliance, and **🖨️ Printable Board Policy Memo**. |

---

## 5. Deployment & Configuration Status

1. **Git Remote & Branch:** All files committed and pushed to `origin/main` on GitHub (`minerclass/k12-device-policy-evidence-hub`).
2. **GitHub Pages Workflow:**
   * Automated deployment file [`.github/workflows/deploy.yml`](file:///c:/Users/mminer/OneDrive%20-%20bpd3.org/Desktop/Research/k12-device-policy-evidence-hub/.github/workflows/deploy.yml) is active on `main`.
   * Repository settings should have **Source** set to **GitHub Actions** under [Settings -> Pages](https://github.com/minerclass/k12-device-policy-evidence-hub/settings/pages).
3. **Live URL:** `https://minerclass.github.io/k12-device-policy-evidence-hub/`

---

## 6. Verification Checklist for Incoming Agents

- [x] Local repository created with valid `.git` configuration and zero build dependencies.
- [x] Single-file application (`index.html`) operates 100% offline without external CDN failures.
- [x] All benchmark studies in `evidence-matrix.json` conform to the JSON extraction schema.
- [x] Interactive 6-Question Policy Audit calculates live scores (0–18) and generates printable board memos.
- [x] Presentation / Deck Mode toggle tested and operational.
- [x] OpenAlex Python extraction script tested (`scripts/fetch_openalex_evidence.py`).
- [x] Bidirectional links in `screen-time-wrong-question` and `minerclass.github.io` tested and pushed.
- [x] GitHub Actions workflow `.github/workflows/deploy.yml` pushed with explicit `pages: write` permissions.

---

## 7. Next Actions & Ongoing Maintenance

1. **Automated Evidence Ingestion:** Incoming agents can run `python scripts/fetch_openalex_evidence.py` to harvest newly published studies matching Vectors A, B, and C and merge validated entries into `evidence-matrix.json`.
2. **Dissertation Chapter Mapping:** Future agents working on dissertation Chapters 1 & 2 should cross-reference `evidence-matrix.md` when framing the problem of device containment versus pedagogical bypass.
3. **Conference Deck Updates:** When preparing new keynote decks under `pedagogical-friction-iste-ascd-decks`, link directly to the 6-Question District Audit in this hub.
