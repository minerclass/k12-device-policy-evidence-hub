# K–12 Device Policy & Pedagogical Friction Evidence Hub

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Active-teal.svg)](https://minerclass.github.io/k12-device-policy-evidence-hub/)
[![Curated by](https://img.shields.io/badge/Curated_by-Micah_J._Miner-gold.svg)](https://micahminer.com)

A research clearinghouse, empirical evidence matrix, and policy diagnostic platform exploring the intersection of K–12 device access models (take-home 1:1 vs. classroom carts), phone restrictions (pouches, lockers, bans), and **pedagogical friction in the age of generative AI**.

---

## Live Interactive Hub

Access the live single-page application and interactive diagnostic tools on GitHub Pages:

🔗 **[https://minerclass.github.io/k12-device-policy-evidence-hub/](https://minerclass.github.io/k12-device-policy-evidence-hub/)**

---

## Core Premise: Infrastructure vs. Pedagogy

American and international schools experienced a 15-year rapid expansion of school-issued devices, followed by an aggressive wave of phone bans, locker mandates, and cart transitions. 

**Neither hardware expansion nor hardware removal inherently changes the cognitive demand of classroom tasks.**

```
┌──────────────────────────────────────────────┐
│        INFRASTRUCTURAL INTERVENTION          │
│   (Pouches, Lockers, Carts, Screen Quotas)   │
└──────────────────────┬───────────────────────┘
                       │
             Does hardware removal
           alter instructional demand?
                       │
       ┌───────────────┴───────────────┐
       ▼                               ▼
┌─────────────────────────────┐ ┌─────────────────────────────┐
│    THE UNADDRESSED BYPASS   │ │     PRODUCTIVE FRICTION     │
│  Passive delivery & AI off- │ │ Active sensemaking, deep    │
│  loading continue on 1:1    │ │ inquiry, and dialogue       │
│  district-issued hardware   │ │ restored in learning tasks  │
└─────────────────────────────┘ └─────────────────────────────┘
```

This hub distinguishes **Infrastructural Interventions** (physical device access, containment, filtering) from **Instructional/Noetic Outcomes** (cognitive struggle, sensemaking, dialogue, student agency). Pouching a smartphone while assigning low-demand digital worksheets on 1:1 Chromebooks simply reroutes cognitive offloading to generative AI and automated tools.

---

## Repository Structure

```
.
├── index.html                  # Interactive, single-file GitHub Pages application
├── search-protocol.md          # Agent Search & Evaluation Protocol with query vectors
├── evidence-matrix.json        # Structured JSON dataset of benchmark empirical studies
├── evidence-matrix.md          # APA 7-formatted literature synthesis and comparative table
├── github-collection-map.md    # Architecture of connected public scholarship repositories
├── README.md                   # Repository overview, deployment, and usage guide
├── LICENSE                     # CC BY-NC-SA 4.0 (Content) & MIT (Code)
└── .nojekyll                   # Disables Jekyll processing on GitHub Pages
```

---

## What the Interactive Platform Includes

- **The 4 Core Diagnostic Tests:** Interactive evaluator for (1) Infrastructure vs. Pedagogy, (2) The Bypass Diagnostic, (3) Equity & Vulnerability Boundary, and (4) Policy Divergence Analysis.
- **Searchable Empirical Evidence Matrix:** Filterable by policy mechanism (Pouch, Locker, Cart vs. 1:1, Analogue Mandate, Screen Quota), grade band, and friction dimension.
- **District Policy Audit & Scorecard:** Real-time 6-question policy audit designed for school boards, administrative cabinets, and consulting workshops.
- **Search & Evaluation Protocol Engine:** Copy-ready query vectors (A, B, C), inclusion/exclusion filters, and JSON extraction prompt generator for AI agents and human researchers.
- **Connected Repository Collection Navigator:** Live visual links to Micah Miner’s related public scholarship and dissertation-adjacent repositories.

---

## Connected Repository Collection & Ecosystem Hubs

This repository serves as an empirical evidence gateway connecting multiple public scholarship hubs under [`minerclass`](https://github.com/minerclass):

1. **✍️ Writing Hub & Essays:**
   - **[Writing Sites Hub](https://minerclass.github.io/writing-sites-hub/):** Unified portal for essays, articles, and public scholarship.
   - **[The Pouch & The Bypass](https://minerclass.github.io/screen-time-wrong-question/pouch-and-bypass/):** Deep dive into the Haidt–Odgers–Horvath debate, 1:1 expansion/reversal symmetry, and district policy questions.
   - **[Screen Time Is the Wrong Question](https://minerclass.github.io/screen-time-wrong-question/):** CoSN companion essay reframing screen time around cognitive work.
2. **🎤 Conference & Keynote Hub:**
   - **[Pedagogical Friction Presentation Decks](https://minerclass.github.io/pedagogical-friction-iste-ascd-decks/):** ISTE and ASCD session decks on AI governance and friction.
   - **[AI Education Conference](https://minerclass.github.io/nlu_ai-ed-conference-pres26/):** Keynote and session deck on AI assessment validity.
   - **[Screen Practice Compass](https://minerclass.github.io/screen-practice-compass/):** Interactive reflection tool for educator workshops.
3. **🎓 Dissertation & Theoretical Hub:**
   - **[Dissertation Overview Gateway](https://minerclass.github.io/dissertation-overview/):** Doctoral research portal and case study methodology.
   - **[Pedagogy of Friction Hub](https://minerclass.github.io/genAI-ML-pedagogy-of-friction-site/):** Theoretical exploration of noetic, rhetorical, existential, and infrastructural friction.
   - **[When Output Looks Like Learning](https://minerclass.github.io/When-Output-Looks-Like-Learning/):** Companion on tertiary algorithmicity and unproductive success.
4. **🎮 Gaming Hubs & Simulations:**
   - **[Games Hub Portal](https://minerclass.github.io/games-hub/):** Directory of reflective pedagogical simulations.
   - **[Keeper of the Word (Orality Game)](https://minerclass.github.io/orality_game/):** Ongian simulation from oral memory to algorithmic secondary orality.
   - **[Historical Inquiry Friction Suite](https://minerclass.github.io/historical-inquiry-friction/):** *Common Ground*, *Devil's Advocate*, and *Keepers of Inquiry*.
5. **🏛️ District Leadership & Governance:**
   - **[District Tech Review Matrix](https://minerclass.github.io/bpd3-tech-review/):** Procurement and privacy evaluation rubric for K–12 software tools.

See [`github-collection-map.md`](github-collection-map.md) for full audience pathways and workshop sequencing.

---

## Deployment to GitHub Pages

1. Create a repository named `k12-device-policy-evidence-hub` under your GitHub account (`minerclass`).
2. Push this local directory to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: K-12 device policy evidence hub"
   git branch -M main
   git remote add origin https://github.com/minerclass/k12-device-policy-evidence-hub.git
   git push -u origin main
   ```
3. In repository settings, navigate to **Pages** -> **Build and deployment**.
4. Set **Source** to `Deploy from a branch`, **Branch** to `main`, and **Folder** to `/ (root)`.
5. Save. The site will deploy to `https://minerclass.github.io/k12-device-policy-evidence-hub/`.

---

## Author & Attribution

**Micah J. Miner, CETL, Ed.S.**  
*Director of Innovation and Technology, Beach Park CCSD 3*  
*Author of AI Goes to School (Times 10 Publications)*  
*Doctoral Candidate in Curriculum, Advocacy, and Policy, National Louis University*  
*CoSN AI and EdTech Innovation Committees*

🌐 [micahminer.com](https://micahminer.com) | 💻 [github.com/minerclass](https://github.com/minerclass)
