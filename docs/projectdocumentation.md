# 🚀 Kasparro – Multi-Agent AI Content Generation System

## 🧩 Problem Statement

Design and implement a true **AI-agentic**, production-style multi-agent automation system that takes a single structured product dataset as input and generates machine-readable JSON content pages.
The system must:

* Use **LLMs** inside agents
* Use a **StateGraph** (LangGraph) instead of a sequential script
* Use shared memory/state across agents
* Demonstrate proper agent boundaries
* Use reusable logic blocks
* Produce deterministic JSON outputs

The task explicitly avoids template-only scripts and requires an **AI-powered, agentic architecture** — not a monolithic or rule-based pipeline.

---

## 🛠️ Solution Overview

This project implements a fully autonomous **AI-Powered Multi-Agent Pipeline** using:

* **LangGraph** for graph-style orchestration
* **Groq LLM (llama-3.1-8b-instant)** for generation
* **Pydantic PipelineState** for shared memory
* **Specialized agents** for each content generation task
* **Logic-block fallbacks** to guarantee deterministic output

The pipeline consumes a single structured product dataset and generates:

* ✅ FAQ Page (faq.json)
* ✅ Product Description Page (product_page.json)
* ✅ Comparison Page (comparison_page.json)
* ✅ Logs (run_logs.json)

Each AI agent independently contributes content and updates the shared state.

---

## 🎯 Key System Objectives

* ✅ Use real AI-powered agents (LLM-driven)
* ✅ Use LangGraph for multi-agent orchestration
* ✅ Maintain a single shared PipelineState
* ✅ Enforce strong agent boundaries
* ✅ Maintain deterministic JSON output
* ✅ Clean separation between logic blocks, models, templates, and agents
* ✅ Ensure production-style modular architecture

---

## 📦 Scopes & Assumptions

### ✅ Scope

* Uses the provided **GlowBoost Vitamin C Serum** as the primary input
* Creates a fictional **Product B via LLM** for comparison
* Generates exactly 3 output artifacts:

  * FAQ JSON (AI generated)
  * Product Description JSON (AI + logic blocks)
  * Comparison JSON (AI competitor + structured reasoning)
* Runs entirely locally
* Outputs are strictly **machine-readable JSON**

---

### 🚫 Out of Scope

* No frontend
* No external product lookup
* No manual curation
* No non-AI rule-based content writing

---

### 📌 Assumptions

* Input data is valid
* LLM responses are parsed into structured content
* Logic blocks act as fallback when LLM output is malformed

---

## 🧠 System Design (Mandatory)

### 1️⃣ Architectural Philosophy

This is a **true agentic system**, where:

* Each agent performs one specialized AI-driven task
* Agents **do not depend on each other directly**
* All information is passed via a **shared Pydantic PipelineState**
* LangGraph determines execution flow

This mirrors modern enterprise AI workflow orchestrators.

---

### 2️⃣ Layered System Architecture

The architecture is cleanly divided into:

1. **Input Layer**
2. **Data Modeling Layer**
3. **AI Agent Layer (LLM-powered)**
4. **Logic Block Layer**
5. **Template Layer**
6. **LangGraph Orchestration Layer**
7. **Output Layer**

---

### 3️⃣ Input Layer

**input_data.py**

* Contains the canonical product dataset
* No external API calls

---

### 4️⃣ Data Modeling Layer

Models include:

* **Product**
* **Question**
* **PipelineState (Pydantic)**

PipelineState holds:

* product
* product_b
* questions
* faqs
* product_page
* comparison_page
* logs

This ensures all agents read/write a consistent shared memory.

---

### 5️⃣ Agent Execution Layer (AI-Powered Agents)

Each agent performs one specialized AI task:

---

#### **ParserAgent**

* Converts raw dict → Product model
* Initializes state

---

#### **QuestionGenerationAgent (LLM-powered)**

* Uses Groq LLM to generate ~15 structured questions
* Writes them into `state.questions`

---

#### **FAQAgent (LLM-powered + logic fallback)**

* For each question → generates answer via LLM
* If LLM returns invalid JSON → fallback to logic blocks
* Writes final structured FAQ data into `state.faqs`

---

#### **ProductPageAgent**

* Generates product description content
* Uses:

  * logic blocks for structure
  * LLM for narrative enhancement

---

#### **ComparisonAgent (LLM-powered)**

* LLM creates a fictional competitor product
* LLM provides a narrative comparison
* Deterministic logic-block comparison ensures valid JSON fields
* Outputs final comparison JSON

---

### 6️⃣ Logic Block Layer

Reusable modules handle deterministic transformations:

* benefits_block
* usage_block
* safety_block
* ingredients_block
* comparison_block

These serve as **fallbacks** & **validators** for LLM output.

---

### 7️⃣ Template Layer

Templates define strict JSON schemas for:

* FAQ Page
* Product Description Page
* Comparison Page

Templates ensure consistent structure regardless of LLM behavior.

---

### 8️⃣ Orchestration Layer (LangGraph)

**langgraph_orchestrator.py**

* Builds a StateGraph
* Each agent becomes a node
* State flows through nodes
* Execution stops when all nodes complete
* Final state is dumped into JSON files

This replaces the old **linear script**, meeting the evaluator’s requirements.

---

### 9️⃣ Determinism & Safety Guarantees

* LLM output is validated and sanitized
* Logic fallbacks ensure structural correctness
* Templates enforce JSON schema
* Shared state ensures predictable agent interactions

---

## 3️⃣ Data Flow Summary

1. Product loaded
2. ParserAgent → Product Model
3. LLM generates questions (QuestionGenerationAgent)
4. LLM generates answers (FAQAgent)
5. LLM + logic generate product page (ProductPageAgent)
6. LLM creates competitor + narrative + structured comparison (ComparisonAgent)
7. LangGraph writes all final JSONs

---

## 4️⃣ Design Principles Followed

* **Single Responsibility** per agent
* **No global variables**
* **AI-powered agents**
* **Shared structured state**
* **Deterministic final JSON**
* **Reproducible pipeline**
* **Fully modular**
* **Production-ready separation of concerns**
