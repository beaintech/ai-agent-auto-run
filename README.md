# Agentic Testing System (Mockup)

这是一个模拟 Federico De Ponte 描述的“多智能体并行代码生成+测试”系统的简化示例。

功能演示：
1. orchestrator 分发任务
2. code_agent 生成示例代码（这里用的是假代码）
3. test_agent 生成 pytest 测试
4. run_agent 运行测试并返回结果
5. repair_agent 在失败时尝试修复

运行方式：
```bash
cd agentic-testing-system
python orchestrator/orchestrator.py

python -m orchestrator.orchestrator
```

注意：
- 这是示意项目，不会真的连接 Claude / Cursor。
- 你可以在 agents/* 里替换成你自己的 API 调用逻辑。


Short Version

He built an AI system that works like a 24/7 coding factory.
It uses many AI coders (Claude Code) running together, each doing a different job — one writes code, one tests it, one fixes bugs.

A central program (called the orchestrator) manages them all — it decides who does what, checks the results, and restarts tasks when something fails.

Everything runs on 16 NVIDIA GPUs in the cloud, so it never sleeps.

The whole thing is like an AI DevOps pipeline — code → test → fix → repeat — until everything works perfectly.

In short: it’s an AI-native workflow system that lets machines code and debug themselves, with humans only watching the progress.

他建立了一个智能体编排系统（Agentic Orchestration System），
用于在 GPU 集群上并行协调多个 AI 编码智能体（Claude Code 实例）的运行。
该系统融合了 MLOps（机器学习运维）、AI 基础设施工程（AI Infrastructure Engineering） 和 多智能体系统（MAS） 的设计理念。

系统结构包括五层：

基础设施层（Infrastructure Layer）：
 使用 16 块 NVIDIA L4 GPU 和 Google 云 VM，提供计算环境。

编排层（Orchestration Layer）：
 核心控制系统，用于调度任务、监控 Agent 状态、触发自动修复循环。

智能体层（Agent Layer）：
 由多个 Claude Code 实例组成，每个执行不同任务（写代码、写测试、跑测试、修复）。

自动化循环层（Automation & Feedback Loop）：
 形成 Code → Test → Repair → Re-test 的闭环，无需人工干预。

监控层（Observation & Reporting Layer）：
 通过 Slack 等平台汇报结果，实现人机协同监督。

简而言之，这是一种 AI 原生的自动开发管线，
能让机器自行编写、测试、修复代码，人类只需监控进度。

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

第一部分：可操作性与可复制性（实用角度分析）

我们来看：Federico De Ponte 的系统之所以能做到 > 14 Claude Code + 16 L4 GPU + 24/7 运行，靠的是企业级资源。
但——这并不意味着你做不了“小型可复制版”。

下面我给你三层现实对比👇

① 企业级版本（他做的）

算力来源：Google Cloud + 16 × NVIDIA L4 GPU

VM 架构：分布式 Kubernetes 集群，自动伸缩、负载均衡

Agent 规模：同时并行 14–20 个 Claude Code 实例

特点：自动化、高吞吐、持续运行 24/7

成本：约 每月 $15 000 – $30 000（含 GPU 租用、API token 消耗）

可操作性：⭐️⭐️⭐️⭐️⭐️（但只对有公司资源的人）

② 高级个人版（可实现）

算力来源：云端 GPU 平台（如 RunPod、Paperspace、Lambda Labs、Google Cloud 1–2 L4 GPU 租用）

VM 架构：单机 Docker 容器 + Python 多线程/异步调度

Agent 规模：同时 2–5 个 Claude Code 或 OpenAI API 实例

特点：可以实现 agentic loop（写 → 测 → 修 → 再测），并可通过 Slack 或 Webhook 汇报结果

成本：约 每月 $150 – $500（视 GPU 和 API 使用量）

可操作性：⭐️⭐️⭐️⭐️
复制难度：中等（用 Python + Claude API 可实现）

③ 轻量本地版（我给你的 mockup 项目）

算力来源：你自己电脑的 CPU （MacBook 完全可跑）

Agent 架构：单机多脚本模拟（Code → Test → Run → Repair）

Agent 规模：1–2 个线程模拟

特点：结构正确，但不调用 Claude API；纯教学与验证逻辑用

成本：0 €

功能限制：不能持续 24/7 或并行多 GPU ，但逻辑等价

可操作性：⭐️⭐️⭐️⭐️⭐️
复制难度：极低，任何人可复现

✅ 结论

如果是公司级资源（有 GPU + API 预算），可以 100 % 复制他的架构。

如果是个人项目，你可以实现 60–70 % 功能（核心 loop、agent 协作、测试机制都能跑）。

本地 mockup 版就是入门级的 orchestration 逻辑，未来你可以一步步加上 Claude API 、并行 agent 和 Slack 汇报，就能逐渐接近他的版本。

Operability and Reproducibility (Practical Analysis)

Let’s look at why Federico De Ponte’s system can run more than 14 Claude Code instances on 16 L4 GPUs, 24/7 — it’s powered by enterprise-level infrastructure.
But — that doesn’t mean you can’t build a smaller, reproducible version yourself.

Below are three realistic implementation tiers 👇

① Enterprise-Level Version (what he built)

Compute source: Google Cloud + 16 × NVIDIA L4 GPUs

VM architecture: Distributed Kubernetes cluster with auto-scaling and load balancing

Agent scale: 14 – 20 Claude Code instances running in parallel

Features: Fully automated, high throughput, 24/7 continuous operation

Cost: Approx. $15 000 – $30 000 per month (including GPU rental and API token usage)

Operability: ⭐️⭐️⭐️⭐️⭐️ (but only for organizations with infrastructure resources)

② Advanced Personal Version (feasible)

Compute source: Cloud GPU services such as RunPod, Paperspace, Lambda Labs, or Google Cloud (1 – 2 L4 GPUs)

VM architecture: Single machine with Docker containers + Python multi-threading/async scheduling

Agent scale: 2 – 5 Claude Code or OpenAI API instances running together

Features: Implements an agentic loop (write → test → repair → re-test) and can report via Slack or Webhook

Cost: Approx. $150 – $500 per month (depending on GPU and API usage)

Operability: ⭐️⭐️⭐️⭐️

Reproducibility: Medium difficulty (Python + Claude API sufficient to build)

③ Lightweight Local Version (the mockup project I gave you)

Compute source: Your own CPU (e.g., MacBook works fine)

Agent architecture: Local multi-script simulation (Code → Test → Run → Repair)

Agent scale: 1 – 2 threads simulated

Features: Correct structure, no Claude API calls — for educational and logic validation only

Cost: 0 €

Limitations: Cannot run 24/7 or use multi-GPU parallelism, but logical behavior is equivalent

Operability: ⭐️⭐️⭐️⭐️⭐️

Reproducibility: Very easy — anyone can replicate it

✅ Conclusion

With enterprise-level resources (GPU + API budget), you can replicate his architecture 100 %.

As a personal project, you can achieve about 60 – 70 % of the functionality (core loops, agent coordination, testing mechanisms all work).

The local mockup version already contains the foundational orchestration logic — you can gradually add Claude API integration, parallel agents, and Slack reporting to approach his full setup.

# Agentic Orchestration System — Technical Overview

**He built an agentic orchestration system**  
that coordinates multiple AI coding agents (Claude Code instances) running in parallel across a GPU cluster.  
This system integrates concepts from **MLOps**, **AI Infrastructure Engineering**, and **Multi-Agent System (MAS)** design.

---

## 1️⃣ Infrastructure Layer — AI Compute & Environment

At the foundation lies a robust AI infrastructure that powers continuous, large-scale computation:

- **16 × NVIDIA L4 GPUs**, managed via **Google Cloud virtual machines (VMs)**.  
- Containers isolate each agent’s runtime environment (e.g., Docker or Kubernetes).  
- Designed for **24/7 high-availability** and **low-latency orchestration**.

This layer ensures that multiple Claude Code instances can run safely and concurrently without resource conflicts.

---

## 2️⃣ Orchestration Layer — Workflow Controller (MLOps Core)

This is the **central coordination engine**, sometimes called the *orchestrator*.  
In MLOps, it acts as the **workflow automation system**, responsible for:

- Scheduling and distributing tasks across all agents.  
- Tracking execution states and collecting feedback.  
- Triggering automatic repair or re-test cycles when failures occur.

It may be implemented through:
- Asynchronous Python controllers (`asyncio`, `FastAPI`, or message queues).  
- Workflow frameworks such as **Prefect**, **Ray**, **Airflow**, or **LangGraph**.

The orchestrator ensures synchronization between all running agents — enabling a continuous, self-correcting AI workflow.

---

## 3️⃣ Agent Layer — Multi-Agent System (MAS)

The agent layer hosts multiple **Claude Code** instances, each assigned to a specific function.  
Together, they operate as a **multi-agent network**:

- **Code Agent** → Generates core code functions.  
- **Test Agent** → Produces automated unit and integration tests.  
- **Run Agent** → Executes tests and reports results.  
- **Repair Agent** → Fixes bugs or failed code sections.

Agents interact through the orchestrator’s task routing system, ensuring that outputs from one stage become inputs for the next.

---

## 4️⃣ Automation & Feedback Loop — MLOps Pipeline

The entire process follows a **closed feedback loop**, similar to a CI/CD pipeline:

1. Generate code  
2. Generate tests  
3. Run tests  
4. Repair errors  
5. Re-test until success  

Once all tests pass, the system automatically validates and stores the final code — no human intervention required.

This design represents an **AI-native continuous development pipeline** capable of self-evaluation and self-improvement.

---

## 5️⃣ Observation & Reporting Layer — Monitoring & Collaboration

- **Slack integration** for real-time reporting of metrics, logs, and test outcomes.  
- Centralized log storage for analytics and performance tracking.  
- Human engineers can supervise progress or study system failures.

This layer bridges **human oversight** with **autonomous AI operations**.

---

## 📘 Summary

Federico’s architecture can be described as an **AI-native agentic testing and orchestration platform**, built upon:

- **AI Infrastructure** → GPU/VM computing backbone.  
- **MLOps** → Automated pipeline and workflow control.  
- **Multi-Agent System (MAS)** → Specialized agents collaborating via orchestration logic.

In simple terms, it is a **self-running AI software factory** — capable of writing, testing, and fixing code around the clock.
# ai-agent-auto-run
