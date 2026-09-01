# Agent Search & Evaluation Protocol: K–12 Screen Time Rules, Device Policies, and Pedagogical Friction

Prepared for research workflows, automated AI agents, and practitioner-scholar policy analysis.  
Author: Micah J. Miner, CETL, Ed.S. — Director of Innovation and Technology, Beach Park CCSD 3; Ed.D. Candidate, National Louis University.

---

## 1. Overview & Objective

This protocol directs an AI research agent (or human researcher) to systematically search, screen, evaluate, and synthesize research literature, empirical studies, and district policy documents regarding K–12 screen time rules, personal device bans (e.g., phone pouches, lockers), 1:1 device management models (classroom carts vs. take-home), and their measured impact on learning, attention, equity, and pedagogical design.

### Core Evaluative Premise
Distinguish between **Infrastructural Interventions** (device presence, physical containment, network filtering, take-home rules) and **Instructional/Noetic Outcomes** (cognitive demand, active sensemaking, dialogue, student agency). A policy restriction alters the channel of access; it does not inherently dictate the pedagogical design of the learning environment.

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

---

## 2. Agent Persona & Analytical Stance

- **Domain:** K–12 Educational Technology Leadership (CETL standards), Media Ecology, Educational Policy, and Learning Sciences.
- **Analytical Lens:** Technoskeptical and evidence-grounded. Avoid techno-solutionism and moral panic binaries.
- **Key Distinctions:**
  - *Hardware Containment vs. Pedagogical Redesign:* Does the source treat device removal as an end in itself, or does it examine what replaces screen time?
  - *Correlation vs. Causation:* Differentiate self-report cross-sectional surveys from longitudinal, experimental, or quasi-experimental designs (e.g., UK SMART Schools study vs. correlational screen-time surveys).
  - *Delivery vs. Cognitive Construction:* Differentiate direct delivery/drill applications from active inquiry/generative tasks (drawing on meta-analyses such as Tamim et al., 2011; Zheng et al., 2016).
  - *Productive vs. Exclusionary Friction:* Differentiate learning-supportive cognitive struggle from infrastructural barriers that disproportionately penalize vulnerable student groups.

---

## 3. Targeted Search Matrix & Query Vectors

Use the following queries across academic search engines (Google Scholar, ERIC, Scopus, Semantic Scholar, OpenAlex, PubMed) and policy repositories (CoSN, UNESCO, NCES, State Boards of Education):

### Vector A: Meta-Analytic & Empirical Foundations
- `"Rana Tamim"` AND (`"meta-analysis"` OR `"technology on learning"` OR `"second-order"`)
- `("screen time"` OR `"device restriction"` OR `"phone ban"`) AND (`"academic achievement"` OR `"cognitive load"` OR `"wellbeing"`) AND (`"longitudinal"` OR `"quasi-experimental"`)
- `("SMART Schools"` OR `"Dutch phone ban"` OR `"Swedish textbook investment"`) AND (`"evaluation"` OR `"outcomes"`)
- `"Candice Odgers"` AND (`"digital inequality"` OR `"adolescent mental health"` OR `"screen time"`)
- `("print vs digital reading"` OR `"screen reading comprehension"`) AND (`"Delgado"` OR `"Clinton"` OR `"meta-analysis"`)

### Vector B: Institutional Policy & Access Models
- `("take-home 1:1"` OR `"classroom cart"` OR `"shared device"`) AND (`"district policy"` OR `"middle school"` OR `"instructional shift"`)
- `("Yondr"` OR `"phone pouch"` OR `"bell-to-bell ban"`) AND (`"implementation"` OR `"classroom climate"` OR `"enforcement"`)
- `"UNESCO Global Education Monitoring Report"` AND (`"technology in education"` OR `"appropriate use"`)
- `"K-12 screen time policy"` AND (`"analogue learning"` OR `"handwriting"` OR `"print vs digital reading"`)
- `("1:1 laptop program"` OR `"one-to-one"`) AND `"Zheng"` AND `"Warschauer"` AND `"meta-analysis"`

### Vector C: Pedagogical Friction & Assessment Validity
- `("pedagogical friction"` OR `"productive struggle"` OR `"unproductive success"`) AND (`"generative AI"` OR `"instructional design"`)
- `("cognitive offloading"` OR `"automation bypass"`) AND (`"secondary education"` OR `"writing instruction"`)
- `"tertiary algorithmicity"` OR (`"media ecology"` AND `"educational assessment"`)
- `("Larry Cuban"` OR `"oversold and underused"`) AND (`"grammar of schooling"` OR `"device policy"`)

---

## 4. Inclusion & Exclusion Criteria

| Category | Include | Exclude |
| :--- | :--- | :--- |
| **Study Design** | Meta-analyses, systematic reviews, pre-registered longitudinal studies, natural experiments, district policy comparative case studies. | Unsubstantiated op-eds, single-classroom anecdotes without methodology, commercial vendor marketing whitepapers. |
| **Focus** | Interaction between screen rules/device availability and learning, attention, social climate, equity, or instructional quality. | Generic technology reviews lacking focus on policy, access models, or cognitive/pedagogical friction. |
| **Construct Clarity** | Clearly defines the type of screen use (passive vs. active, instructional vs. recreational, personal phone vs. district Chromebook). | Treats "screen time" as a monolithic, undifferentiated variable without context or platform analysis. |
| **Target Population** | K–12 students, teachers, building administrators, district leaders, and system governance. | Exclusively higher education or adult workforce studies (unless providing foundational theoretical frameworks). |

---

## 5. Structured Data Extraction Template

For each retrieved source, the agent must extract data into the following JSON schema:

```json
{
  "source_id": "AUT_YEAR_KEYWORD",
  "citation": "Full APA 7th Edition Citation",
  "url_or_doi": "Direct link or DOI",
  "document_type": "Empirical Study | Meta-Analysis | Policy Evaluation | Theoretical Framework | District Policy Case",
  "policy_or_intervention": {
    "mechanism": "Phone Pouch | Locker Policy | Cart vs Take-Home | Screen Quota | Analogue Mandate | Algorithmic Guardrail",
    "grade_bands": "Elementary (K-5) | Middle (6-8) | High (9-12) | System-wide",
    "enforcement_level": "Building | District | State/National Mandate"
  },
  "theoretical_framing": {
    "considers_instructional_design": true,
    "friction_dimension_addressed": "Noetic | Rhetorical | Existential | Infrastructural | Multi-layer",
    "avoids_device_panacea_fallacy": true,
    "udl_and_accessibility_considerations": "Notes on ELL, IEP, 504, or socioeconomic assistive impact"
  },
  "findings_summary": {
    "measured_outcomes": ["Achievement", "Attention/Focus", "Wellbeing", "Classroom Climate", "Equity/Access"],
    "effect_sizes_or_trends": "Specific Cohen's d, Hedges' g, odds ratios, or qualitative consensus",
    "discrepancy_notes": "Note any tension between perceived climate improvements vs. direct outcome measures (e.g. Dutch Ban vs SMART Schools)"
  },
  "critical_limitations": "Confounding variables, self-reporting bias, pre-AI cohort limitation, lack of baseline data, etc.",
  "relevance_score": "1 to 5 (5 = Highly relevant empirical/policy paper directly addressing screen ecology)"
}
```

---

## 6. Synthesis Prompts for Agent Report Output

When compiling search results, the agent must answer the following diagnostic questions:

1. **The Infrastructure vs. Pedagogy Test:**
   * Does the source demonstrate that altering hardware access (e.g., phone pouches, cart transitions) produces direct cognitive gains, or does it confirm that gains depend entirely on the subsequent instructional design?
2. **The "Bypass" Diagnostic:**
   * Does the source examine what students and educators do when hardware restrictions are imposed? Are cognitive tasks bypassed through district-issued platforms, or does the policy restore intentional cognitive friction?
3. **The Equity & Vulnerability Boundary:**
   * How does the policy or rule impact historically marginalized students who may rely on school devices for home connectivity, translation, or assistive technology? Does the rule remove exclusionary barriers or erect new ones?
4. **Policy Divergence Analysis:**
   * If comparing multiple studies (e.g., Dutch phone ban vs. UK SMART Schools study), what methodological differences explain diverging conclusions regarding wellbeing vs. academic attainment?

---

## 7. Operational Workflow for the Agent

```
[Start Search]
       │
       ▼
[Execute Vector A, B, C Queries across Repositories & Databases]
       │
       ▼
[Apply Inclusion / Exclusion Filters]
       │
       ▼
[Extract via JSON Schema to evidence-matrix.json]
       │
       ▼
[Synthesize Findings Against 4 Core Diagnostic Questions]
       │
       ▼
[Output Executive Synthesis & Annotated Evidence Matrix into evidence-matrix.md]
```
