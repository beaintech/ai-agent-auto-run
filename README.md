# Agentic FastAPI Testing System (Mock)

This project is a **proof-of-concept** that simulates how a Claude-like
multi-agent system can automatically:

- generate code
- generate tests
- run tests
- repair failing code
- repeat until all tests pass

It uses a very small example: a FastAPI service with a single `/add` endpoint.

## Files

- `main.py`  
  Orchestrator. Runs the loop: code → tests → run → repair.

- `agents/code_agent.py`  
  Simulated code generator. Returns an initial **buggy** FastAPI app
  (it ignores the `do_round` flag).

- `agents/test_agent.py`  
  Simulated test generator. Produces pytest tests using `TestClient`,
  including cases that require rounding and validation errors.

- `agents/run_agent.py`  
  Simulated execution agent. Writes `user_code.py` and `test_user_code.py`
  to a temporary directory and runs `pytest -q`.

- `agents/repair_agent.py`  
  Simulated repair agent. Takes the failing tests and report,
  and returns a corrected FastAPI app that passes all tests.

## How the Flow Works

1. `code_agent.generate_code(task)`  
   Creates an initial FastAPI implementation as a string.

2. `test_agent.generate_tests(task, code)`  
   Generates pytest tests that describe the expected behaviour.

3. `run_agent.run_tests(code, tests)`  
   Writes both strings into files and runs `pytest`.

4. If tests fail:  
   `repair_agent.repair_code(task, code, tests, report)`  
   returns a new version of the code which should fix the failures.

5. The orchestrator (`main.py`) repeats the run/repair loop
   until all tests pass or the retry limit is reached.

## Installation

Create a virtual environment (recommended) and install:

```bash
pip install fastapi pytest httpx
```
## run locally

python main.py

## Note:
- This is a demo project and will not actually connect to Claude / Cursor.
- You can replace the logic inside agents/* with your own API calls, the agents with real LLM-driven code generation and repair.  
- This local design mirrors larger multi-agent orchestration systems used in production environments.

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


## Testing Pattern & Effect
1. Why the first test is supposed to fail

The code agent intentionally writes an imperfect FastAPI version on purpose.
It ignores the do_round=True feature.
So the rounding test fails.
This failure shows the system can detect real mistakes, not just run code blindly.

2. What happens after the failure

When the test fails, the repair agent reads the error report.
Then it generates a fixed version of the FastAPI endpoint.
This new version now correctly rounds the result to two decimals.

3. Why the second run passes

The orchestrator runs the tests again.
This time, all tests pass because the repaired code is correct.
This shows the system can self-correct without human help.

4. What this proves

This whole cycle demonstrates how an AI agentic system works:

Write code → Test it → Detect failure → Repair code → Test again → Success

This is exactly how 14 Claude agents can work together in a real automated coding pipeline.

