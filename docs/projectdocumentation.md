<<<<<<< HEAD
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
=======
# 🚀 Kasparro – Multi-Agent Content Generation System

## 🧩 Problem Statement

Design and implement a modular, production-style multi-agent automation system that takes a single structured product dataset as input and automatically generates machine-readable content pages in JSON format. The system must demonstrate proper agent boundaries, reusable logic blocks, template-driven generation, and a clear orchestration flow. The challenge explicitly avoids UI development, prompt-only solutions, and monolithic scripts, and instead focuses on systems engineering and automation design.
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

## 🛠️ Solution Overview

<<<<<<< HEAD
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
=======
This project delivers a fully automated, rule-driven, multi-agent content generation system implemented in Python. The system is designed to mirror real-world production automation where independent services (agents) cooperate through structured data contracts.

The pipeline accepts a single canonical product dataset as input and autonomously produces three independent, machine-readable content artifacts:

* ✅ FAQ Page (faq.json)  
* ✅ Product Description Page (product_page.json)  
* ✅ Comparison Page (comparison_page.json)  

Each output page is generated through:

* Explicit agent responsibilities  
* Shared reusable logic blocks  
* A custom-built template layer  
* A centralized orchestration engine  

The system is intentionally designed to be framework-agnostic, free from UI layers, and independent of third-party orchestration tools. The focus remains exclusively on system design, automation correctness, and structured output reliability.
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

## 🎯 Key System Objectives

<<<<<<< HEAD
* ✅ Use real AI-powered agents (LLM-driven)
* ✅ Use LangGraph for multi-agent orchestration
* ✅ Maintain a single shared PipelineState
* ✅ Enforce strong agent boundaries
* ✅ Maintain deterministic JSON output
* ✅ Clean separation between logic blocks, models, templates, and agents
* ✅ Ensure production-style modular architecture
=======
* ✅ Demonstrate correct agent boundary design  
* ✅ Enforce strict single-responsibility principle  
* ✅ Enable logic reuse across multiple page types  
* ✅ Prove template-driven content generation  
* ✅ Guarantee deterministic, machine-readable JSON output  
* ✅ Maintain complete separation between data, logic, templates, and orchestration  

---

This project implements a Python-based multi-agent content generation pipeline that transforms structured product data into three different content pages:

* FAQ Page (JSON)  
* Product Description Page (JSON)  
* Comparison Page (JSON)  

The solution is composed of:

* Independent agents, each with a single responsibility  
* Reusable logic blocks that apply deterministic transformation rules  
* A custom template layer that defines the structure of each output page  
* A central orchestrator that executes the end-to-end pipeline  

The system operates fully on the provided dataset without any external research or additional facts and produces clean, structured, machine-readable JSON outputs.
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

## 📦 Scopes & Assumptions

### ✅ Scope

<<<<<<< HEAD
* Uses the provided **GlowBoost Vitamin C Serum** as the primary input
* Creates a fictional **Product B via LLM** for comparison
* Generates exactly 3 output artifacts:

  * FAQ JSON (AI generated)
  * Product Description JSON (AI + logic blocks)
  * Comparison JSON (AI competitor + structured reasoning)
* Runs entirely locally
* Outputs are strictly **machine-readable JSON**
=======
* Only the provided GlowBoost Vitamin C Serum dataset is used as real input data.  
* A single fictional Product B is generated internally only for the comparison page.  
* The system generates exactly three output artifacts:  
  * ✅ One FAQ Page  
  * ✅ One Product Description Page  
  * ✅ One Comparison Page  
* The solution operates entirely as a backend automation system with no UI.  
* All outputs are generated in clean JSON format suitable for downstream machine consumption.  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 🚫 Out of Scope

<<<<<<< HEAD
* No frontend
* No external product lookup
* No manual curation
* No non-AI rule-based content writing
=======
* Frontend UI, dashboards, or websites  
* Manual content writing or editing  
* External APIs, databases, or web scraping  
* Model fine-tuning or training workflows  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 📌 Assumptions

<<<<<<< HEAD
* Input data is valid
* LLM responses are parsed into structured content
* Logic blocks act as fallback when LLM output is malformed
=======
* Input data is structurally valid and complete  
* Output JSON will be consumed by downstream systems such as CMS platforms, search indexes, or APIs  
* The same architecture can be extended to batch-processing multiple products without redesign  

---

### ✅ Scope

* Only the provided product dataset (GlowBoost Vitamin C Serum) is treated as the real input.  
* A fictional Product B is generated internally for the comparison page only.  
* The system generates:  
  * ✅ One FAQ Page  
  * ✅ One Product Page  
  * ✅ One Comparison Page  
* All final outputs are generated strictly in JSON format.  

---

### 📌 Assumptions

* No external APIs or databases are used.  
* No frontend, website, or UI components are required.  
* The system runs as a local Python automation pipeline.  
* All transformations are rule-based and deterministic.  
* The generated content is structured for machine use, not for human-formatted presentation.  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

## 🧠 System Design (Mandatory)

### 1️⃣ Architectural Philosophy

<<<<<<< HEAD
This is a **true agentic system**, where:

* Each agent performs one specialized AI-driven task
* Agents **do not depend on each other directly**
* All information is passed via a **shared Pydantic PipelineState**
* LangGraph determines execution flow

This mirrors modern enterprise AI workflow orchestrators.
=======
The system is designed using a modular agent-based architecture that mirrors real production pipelines. Each agent operates as a stateless worker that:

* ✅ Accepts a clearly defined input  
* ✅ Executes a single transformation  
* ✅ Produces a structured output  

Agents never modify shared global state and never directly depend on each other’s internal implementation.
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 2️⃣ Layered System Architecture

<<<<<<< HEAD
The architecture is cleanly divided into:

1. **Input Layer**
2. **Data Modeling Layer**
3. **AI Agent Layer (LLM-powered)**
4. **Logic Block Layer**
5. **Template Layer**
6. **LangGraph Orchestration Layer**
7. **Output Layer**
=======
The full system is divided into six independent layers:

1. Input Layer  
2. Data Modeling Layer  
3. Agent Execution Layer  
4. Logic Block Layer  
5. Template Layer  
6. Orchestration & Output Layer  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 3️⃣ Input Layer

<<<<<<< HEAD
**input_data.py**

* Contains the canonical product dataset
* No external API calls
=======
* 📄 File: input_data.py  
* 🎯 Responsibility: Stores the canonical product dataset as a pure Python dictionary  
* ✅ Purpose: Acts as the single source of truth for the entire pipeline  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 4️⃣ Data Modeling Layer

<<<<<<< HEAD
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
=======
* Product model  
* Question model  

Responsibilities:

* ✅ Enforce strong internal typing  
* ✅ Normalize raw data into predictable formats  
* ✅ Serve as the contract between agents  

---

### 5️⃣ Agent Execution Layer

Each agent is intentionally isolated and focused on a single responsibility:

* ParserAgent  
  * Input: Raw product dictionary  
  * Output: Structured Product model  

* QuestionGenerationAgent  
  * Input: Product  
  * Output: Exactly 15 Question objects across 15 distinct categories  

* FAQAgent  
  * Input: Product + Questions  
  * Output: Structured FAQ JSON  

* ProductPageAgent  
  * Input: Product  
  * Output: Structured Product Description JSON  

* ComparisonAgent  
  * Input: Product  
  * Output: Structured Comparison JSON with fictional Product B  

---

### 6️⃣ Reusable Logic Block Layer

Logic blocks contain pure transformation functions with no side effects. These blocks may be invoked by multiple agents.

Examples include:

* ✅ Benefits generation block  
* ✅ Usage extraction block  
* ✅ Safety messaging block  
* ✅ Ingredients extraction block  
* ✅ Structured comparison block  

This design ensures maximum composability and reuse while preventing duplication of business rules.
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 7️⃣ Template Layer

<<<<<<< HEAD
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
=======
Templates define the final JSON schemas for each output page type.

Each template explicitly defines:

* ✅ Required fields  
* ✅ Field-level structure  
* ✅ Dependency on specific logic block outputs  

Templates are implemented as deterministic Python functions to ensure complete control over output structure.

---

### 8️⃣ Orchestration & Output Layer

* ⚙️ Controlled by orchestrator.py  
* ✅ Executes agents strictly in dependency order  
* ✅ Ensures failure isolation between pipeline stages  
* ✅ Writes output files atomically into the outputs directory  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

### 9️⃣ Determinism & Safety Guarantees

<<<<<<< HEAD
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
=======
* ✅ No randomness is used  
* ✅ No external network calls are performed  
* ✅ No implicit data injection is allowed  
* ✅ All transformations are reproducible and auditable  

---

### 1️⃣ Architectural Overview

The system follows a pipeline-based, multi-agent architecture where each agent is responsible for a single transformation step. Agents communicate only through structured data objects and do not share any global state.

High-level flow:

Input Data → Parser Agent → Question Agent → Page Generation Agents → JSON Outputs

---

### 2️⃣ Core Components

#### a. Input Layer

* input_data.py  
* Contains the raw product dataset as a structured dictionary.  

---

#### b. Data Models

* Product model  
* Question model  

These models enforce internal data consistency and define the structured format passed between agents.

---

#### c. Agents Layer

Each agent has one clear responsibility:

* ParserAgent  
  * Converts raw input dictionary into a structured Product model  

* QuestionGenerationAgent  
  * Generates exactly 15 questions across 15 distinct categories  

* FAQAgent  
  * Converts categorized questions into structured FAQ JSON using logic blocks and templates  

* ProductPageAgent  
  * Builds the product description JSON using reusable logic blocks  

* ComparisonAgent  
  * Creates a fictional Product B and generates a structured comparison JSON  

---

#### d. Reusable Logic Blocks

Logic blocks apply deterministic transformation rules and can be reused across multiple agents:

* ✅ Benefits transformation  
* ✅ Usage extraction  
* ✅ Safety messaging  
* ✅ Ingredients extraction  
* ✅ Structured comparison logic  

These blocks ensure separation between business logic and page layout.

---

#### e. Template Engine

Custom-built template functions define the exact JSON structure for each page type:

* ✅ FAQ Template  
* ✅ Product Page Template  
* ✅ Comparison Page Template  

Templates define:

* ✅ Required fields  
* ✅ Formatting rules  
* ✅ Dependencies on logic blocks  

---

#### f. Orchestration Layer

* orchestrator.py  
* Controls full execution order of agents  
* Ensures that:  
  * ✅ Parsing occurs first  
  * ✅ Question generation happens next  
  * ✅ Page generation agents run last  
* Handles final JSON file output to the outputs directory  

---

### 3️⃣ Data Flow Summary

1. ✅ Raw product data is loaded  
2. ✅ Parser Agent creates internal product model  
3. ✅ Question Agent generates 15 categorized questions  
4. ✅ FAQ Agent generates FAQ JSON  
5. ✅ Product Page Agent generates product JSON  
6. ✅ Comparison Agent generates comparison JSON with fictional Product B  
7. ✅ Orchestrator saves all outputs as clean JSON files  

---

### 4️⃣ Design Principles Followed

* ✅ Single Responsibility per Agent  
* ✅ No hidden global state  
* ✅ Deterministic rule-based transformations  
* ✅ Template-driven output generation  
* ✅ Fully modular and extensible design  
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
