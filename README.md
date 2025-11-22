# Agentic Testing System (Mockup)

This is a simplified demonstration of the “multi-agent parallel code generation + testing” system described by Federico De Ponte.

Features shown:
1. orchestrator distributes tasks
2. code_agent generates example code (dummy code here)
3. test_agent generates pytest tests
4. run_agent executes tests and returns results
5. repair_agent attempts fixes when failures occur

Run with:
    cd agentic-testing-system
    python orchestrator/orchestrator.py
    python -m orchestrator.orchestrator

Note:
- This is a demo project and will not actually connect to Claude / Cursor.
- You can replace the logic inside agents/* with your own API calls.

---

## Short Version

He built an AI system that works like a 24/7 coding factory.
It uses many AI coders (Claude Code) running together — one writes code, one tests it, one fixes bugs.

A central program (called the orchestrator) manages them all — it decides who does what, checks the results, and restarts tasks when something fails.

Everything runs on 16 NVIDIA GPUs in the cloud, so it never sleeps.

The whole thing is like an AI DevOps pipeline — code → test → fix → repeat — until everything works perfectly.

In short: it’s an AI-native workflow system that lets machines code and debug themselves, with humans only watching the progress.

---

Er hat ein Agentic Orchestration System entwickelt,
das mehrere AI-Coding-Agents (Claude Code Instanzen) parallel auf einem GPU-Cluster koordiniert.
Das System kombiniert Konzepte aus MLOps, AI-Infrastruktur-Engineering und Multi-Agent-System (MAS)-Design.

Das System besteht aus fünf Ebenen:

Infrastrukturebene:
16 × NVIDIA L4-GPUs und Google-Cloud-VMs bilden die Rechenbasis.

Orchestrierungsebene:
Der zentrale Workflow-Controller steuert Aufgaben, überwacht den Status der Agents und startet bei Fehlern automatische Reparaturzyklen.

Agent-Ebene:
Mehrere Claude Code Instanzen mit spezifischen Rollen – Code schreiben, Tests erstellen, ausführen und Fehler beheben.

Automatisierungs- & Feedback-Schleife:
Ein geschlossener Loop (Code → Test → Repair → Re-Test) ohne menschliche Eingriffe.

Überwachungs- & Reporting-Ebene:
Slack-Integration und zentrale Logs ermöglichen menschliche Kontrolle und Analyse.

Kurz gesagt: Es ist eine AI-native Entwicklungs-Pipeline,
die Code autonom schreibt, testet und verbessert, während Menschen nur den Prozess beobachten.

---

## Operability and Reproducibility (Practical Analysis)

Federico De Ponte’s system can run >14 Claude Code instances on 16 L4 GPUs, 24/7 — because it uses enterprise-grade infrastructure.
But you can still replicate it at smaller scales.

Enterprise-Level Version (what he built)
- Compute: Google Cloud + 16 × NVIDIA L4 GPUs
- Architecture: Distributed Kubernetes cluster
- Agents: 14–20 Claude instances
- Cost: $15 000 – $30 000 per month

Advanced Personal Version (realistic)
- Compute: RunPod / Paperspace / Lambda / Google Cloud (1–2 L4 GPUs)
- Architecture: Single VM + Docker + Python async orchestration
- Agents: 2–5 AI agents
- Cost: $150 – $500 per month

Lightweight Local Version (your mockup)
- Compute: Your MacBook CPU
- Architecture: Local scripts simulating the agents
- Cost: 0 €
- Functionally correct; limited parallelism

Conclusion:
Enterprise version = fully reproducible with resources.
Personal version = 60–70% functionality achievable.
Mockup version = perfect for learning and incremental expansion.

---

# Agentic Orchestration System — Technical Overview

He built an agentic orchestration system coordinating multiple AI coding agents (Claude Code instances) across a GPU cluster.
It integrates MLOps, AI Infrastructure Engineering, and Multi-Agent System (MAS) design.

Infrastructure Layer — Compute & Environment
- 16 × NVIDIA L4 GPUs
- Google Cloud VMs
- Containerized runtime
- 24/7 high-availability

Orchestration Layer — Workflow Controller
Handles:
- Task scheduling
- Agent status tracking
- Automatic repair triggering
Technologies: Python asyncio, FastAPI, Ray, LangGraph.

Agent Layer — Multi-Agent Design
- Code Agent
- Test Agent
- Run Agent
- Repair Agent

Automation & Feedback Loop
Closed pipeline:
1. Generate code
2. Generate tests
3. Run tests
4. Repair
5. Re-test until success

Observation & Reporting Layer
- Slack integration
- Central logging
- Human oversight

---

## Summary

This is an AI-native autonomous software factory — a continuous development pipeline that writes, tests, fixes, and improves code with minimal human intervention.

---

## How to Run Locally

### 1. Create and activate a virtual environment

## How to Run Locally

1. Create and activate a virtual environment

    python3 -m venv venv
    source venv/bin/activate        # macOS / Linux
    venv\Scripts\activate           # Windows

2. Install dependencies

    pip install -r requirements.txt

3. Run the orchestrator

    python -m orchestrator.orchestrator

or

    python orchestrator/orchestrator.py

## Notes

- All components are mock implementations.  
- You can replace the agents with real LLM-driven code generation and repair.  
- This local design mirrors larger multi-agent orchestration systems used in production environments.
