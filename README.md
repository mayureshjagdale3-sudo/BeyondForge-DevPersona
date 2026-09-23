<div align="center">

# 🚀 BeyondForge: DevPersona Simulator
### *Autonomous Multi-Agent Developer Simulation & Code Review Engine*

**Built with Purpose for the IBM Bob 2.0 Hackathon on Lablab.ai**

[![IBM Bob 2.0](https://img.shields.io/badge/Powered%20By-IBM%20Bob%202.0-052FAD?style=for-the-badge&logo=ibm&logoColor=white)](https://lablab.ai/ai-hackathons/ibm-bob-2-hackathon)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  <b>Simulate code reviews with specialized AI personas before merging to production.</b>
</p>

---

</div>

## 📑 Navigation
* [Overview](#-project-overview)
* [The Problem](#-the-core-problem)
* [The Solution](#-the-solution)
* [Architecture Flow](#-architecture-flow)
* [The 4 AI Personas](#-the-4-ai-personas)
* [IBM Bob 2.0 Integration](#-ibm-bob-20-integration)
* [Tech Stack](#-tech-stack)
* [Quickstart Guide](#-quickstart-guide)
* [Roadmap](#-future-roadmap)

---

## 📌 Project Overview
**BeyondForge (DevPersona Simulator)** bridges the gap between solitary development and collaborative enterprise reviews. Inspired by multi-agent behavioral simulators, it replaces flat linters with an active engineering round-table. Before a pull request (PR) reaches production, a virtual committee of autonomous personas stress-tests code logic, security integrity, onboarding ease, and system resilience.

---

## ⚡ The Core Problem
> *"Solo builders and lean engineering pods ship fast, but often blind to operational, security, and cognitive debt."*

* 🔴 **Isolated Context:** Freelancers and small teams lack in-house security auditors, DevOps engineers, and QA leads.
* 🟡 **Superficial LLM Linting:** Standard AI copilots generate syntax fixes without understanding organizational maintainability or adversarial edge-cases.
* 🔵 **High Onboarding Debt:** Undocumented, cryptic PRs quietly erode team velocity as codebases scale.

---

## 💡 The Solution
BeyondForge launches a **multi-agent debate framework** powered by **IBM Bob 2.0**. It passes code through distinct psychographic engineering lenses to deliver:
1. **Interactive Round-Table Critique:** Live debate between personas identifying specific trade-offs.
2. **Merge Confidence Index (0–100%):** A balanced readiness metric.
3. **Automated Remediation Patch:** IBM Bob-synthesized refactoring diffs ready for 1-click merge.

---

## 🧠 Architecture Flow

```text
               ┌──────────────────────────────────────┐
               │    Developer Codebase / Target PR    │
               └──────────────────┬───────────────────┘
                                  │
                                  ▼
               ┌──────────────────────────────────────┐
               │     IBM Bob 2.0 Agentic Engine       │
               │   (Repo Context & Subagent Router)   │
               └──────────────────┬───────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Security Lead   │    │ Junior Onboarder │    │   DevOps / SRE   │
│  (Paranoid Eye)  │    │  (Cognitive Load)│    │ (Scale & Memory) │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                     ┌───────────────────────┐
                     │    QA Chaos Monkey    │
                     │  (Nulls & Edgecases)  │
                     └───────────┬───────────┘
                                 │
                                 ▼
                     [Simulated Round-Table]
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
   📊 Merge Confidence Score          🛠️ IBM Bob Auto-Patch


## 🎭 The 4 AI Personas

| Persona | Archetype | Primary Lens | Target Signals |
| :---    | :--- | :--- | :--- |
| 🛡️ **Chief Security Officer** | *Paranoid & Defensive* | Vulnerability Assessment | SQL injections, unescaped queries, hardcoded credentials, authorization bypasses |
| 👶 **Junior Developer** | *Learner & Novice* | Onboarding & Readability | Missing docstrings, obtuse variable naming, spaghetti patterns, high cognitive load |
| ⚡ **Lead SRE / DevOps** | *Strict & Scalable* | Performance & Stability | N+1 database leaks, thread locks, high time complexity, memory footprint |
| 💥 **QA Chaos Engineer** | *Adversarial Breaker* | Edge Case Discovery | Fault tolerance, schema mutations, unhandled null exceptions, timeout crashes |

---

## 🤖 IBM Bob 2.0 Integration

BeyondForge utilizes core primitives from **IBM Bob 2.0**:
* **Full-Repository Grounding:** Bob 2.0 analyzes multi-file structural context across the repository to identify systemic side effects.
* **Subagent Parallelization:** Personas execute concurrently inside Bob’s subagent loop, reducing execution latency.
* **Remediation Synthesis:** Translates multi-persona consensus into actionable code diffs directly within the development workflow.

---


## 💻 Tech Stack

| Layer | Tools & Technologies |
| :--- | :--- |
| **Agentic Core** | IBM Bob 2.0 (Agent Mode, Parallel Tasks, Document Understanding) |
| **Backend API** | Python 3.10+, FastAPI, Uvicorn, Pydantic |
| **Simulation Logic** | LangGraph / CrewAI Agentic State Orchestration |
| **Interface** | Streamlit Real-Time Dashboard / Next.js |
| **VCS Integration** | GitHub REST API, Webhooks |

---

## 🚀 Quickstart Guide

### Prerequisites
* Python 3.10 or higher
* Git

### Local Setup
```bash
# 1. Clone repository
git clone [https://github.com/mayureshjagdale3-sudo/BeyondForge-DevPersona.git](https://github.com/mayureshjagdale3-sudo/BeyondForge-DevPersona.git)
cd BeyondForge-DevPersona

# 2. Initialize environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch simulation server
uvicorn main:app --reload

🗺️ Future Roadmap
[ ] Automated GitHub Actions Bot to run simulation directly on Pull Requests.
[ ] Slider controls to dynamically tune persona strictness (OCEAN psychographics).
[ ] Enterprise support for Rust, Golang, and C++ codebases.
<div align="center">
<sub>Built with ❤️ by Team <b>BeyondForge</b> for IBM Bob 2.0 Hackathon</sub>
</div>
