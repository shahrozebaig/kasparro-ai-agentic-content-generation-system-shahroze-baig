# Kasparro – Multi-Agent Content Generation System

## Problem Statement

Design and implement a modular, production-style **multi-agent automation system** that takes a **single structured product dataset** as input and automatically generates **machine-readable content pages in JSON format**. The system must demonstrate proper agent boundaries, reusable logic blocks, template-driven generation, and a clear orchestration flow. The challenge explicitly avoids UI development, prompt-only solutions, and monolithic scripts, and instead focuses on **systems engineering and automation design**.

---

## Solution Overview

This project delivers a **fully automated, rule-driven, multi-agent content generation system** implemented in Python. The system is designed to mirror real-world production automation where independent services (agents) cooperate through structured data contracts.

The pipeline accepts a **single canonical product dataset** as input and autonomously produces three independent, machine-readable content artifacts:

* FAQ Page (`faq.json`)
* Product Description Page (`product_page.json`)
* Comparison Page (`comparison_page.json`)

Each output page is generated through:

* Explicit **agent responsibilities**
* Shared **reusable logic blocks**
* A **custom-built template layer**
* A centralized **orchestration engine**

The system is intentionally designed to be **framework-agnostic**, free from UI layers, and independent of third-party orchestration tools. The focus remains exclusively on **system design, automation correctness, and structured output reliability**.

---

## Key System Objectives

* Demonstrate correct **agent boundary design**
* Enforce strict **single-responsibility principle**
* Enable **logic reuse across multiple page types**
* Prove **template-driven content generation**
* Guarantee **deterministic, machine-readable JSON output**
* Maintain complete **separation between data, logic, templates, and orchestration**

---

This project implements a **Python-based multi-agent content generation pipeline** that transforms structured product data into three different content pages:

* FAQ Page (JSON)
* Product Description Page (JSON)
* Comparison Page (JSON)

The solution is composed of:

* Independent **agents**, each with a single responsibility
* **Reusable logic blocks** that apply deterministic transformation rules
* A **custom template layer** that defines the structure of each output page
* A central **orchestrator** that executes the end-to-end pipeline

The system operates fully on the provided dataset without any external research or additional facts and produces clean, structured, machine-readable JSON outputs.

---

## Scopes & Assumptions

### Scope

* Only the provided **GlowBoost Vitamin C Serum** dataset is used as real input data.
* A **single fictional Product B** is generated internally only for the comparison page.
* The system generates exactly three output artifacts:

  * One FAQ Page
  * One Product Description Page
  * One Comparison Page
* The solution operates entirely as a **backend automation system** with no UI.
* All outputs are generated in **clean JSON format** suitable for downstream machine consumption.

### Out of Scope

* Frontend UI, dashboards, or websites
* Manual content writing or editing
* External APIs, databases, or web scraping
* Model fine-tuning or training workflows

### Assumptions

* Input data is structurally valid and complete
* Output JSON will be consumed by downstream systems such as CMS platforms, search indexes, or APIs
* The same architecture can be extended to batch-processing multiple products without redesign

---

### Scope

* Only the provided product dataset (GlowBoost Vitamin C Serum) is treated as the real input.
* A fictional Product B is generated internally for the comparison page only.
* The system generates:

  * One FAQ Page
  * One Product Page
  * One Comparison Page
* All final outputs are generated strictly in JSON format.

### Assumptions

* No external APIs or databases are used.
* No frontend, website, or UI components are required.
* The system runs as a local Python automation pipeline.
* All transformations are rule-based and deterministic.
* The generated content is structured for machine use, not for human-formatted presentation.

---

## System Design (Mandatory)

### 1. Architectural Philosophy

The system is designed using a **modular agent-based architecture** that mirrors real production pipelines. Each agent operates as a stateless worker that:

* Accepts a clearly defined input
* Executes a single transformation
* Produces a structured output

Agents never modify shared global state and never directly depend on each other’s internal implementation.

---

### 2. Layered System Architecture

The full system is divided into six independent layers:

1. Input Layer
2. Data Modeling Layer
3. Agent Execution Layer
4. Logic Block Layer
5. Template Layer
6. Orchestration & Output Layer

---

### 3. Input Layer

* File: `input_data.py`
* Responsibility: Stores the canonical product dataset as a pure Python dictionary
* Purpose: Acts as the **single source of truth** for the entire pipeline

---

### 4. Data Modeling Layer

* `Product` model
* `Question` model

Responsibilities:

* Enforce strong internal typing
* Normalize raw data into predictable formats
* Serve as the contract between agents

---

### 5. Agent Execution Layer

Each agent is intentionally isolated and focused on a single responsibility:

* **ParserAgent**

  * Input: Raw product dictionary
  * Output: Structured `Product` model

* **QuestionGenerationAgent**

  * Input: `Product`
  * Output: Exactly 15 `Question` objects across 15 distinct categories

* **FAQAgent**

  * Input: `Product` + Questions
  * Output: Structured FAQ JSON

* **ProductPageAgent**

  * Input: `Product`
  * Output: Structured Product Description JSON

* **ComparisonAgent**

  * Input: `Product`
  * Output: Structured Comparison JSON with fictional Product B

---

### 6. Reusable Logic Block Layer

Logic blocks contain **pure transformation functions** with no side effects. These blocks may be invoked by multiple agents.

Examples include:

* Benefits generation block
* Usage extraction block
* Safety messaging block
* Ingredients extraction block
* Structured comparison block

This design ensures **maximum composability and reuse** while preventing duplication of business rules.

---

### 7. Template Layer

Templates define the **final JSON schemas** for each output page type.

Each template explicitly defines:

* Required fields
* Field-level structure
* Dependency on specific logic block outputs

Templates are implemented as deterministic Python functions to ensure complete control over output structure.

---

### 8. Orchestration & Output Layer

* Controlled by `orchestrator.py`
* Executes agents strictly in dependency order
* Ensures failure isolation between pipeline stages
* Writes output files atomically into the `outputs/` directory

---

### 9. Determinism & Safety Guarantees

* No randomness is used
* No external network calls are performed
* No implicit data injection is allowed
* All transformations are reproducible and auditable

---

### 1. Architectural Overview

The system follows a **pipeline-based, multi-agent architecture** where each agent is responsible for a single transformation step. Agents communicate only through structured data objects and do not share any global state.

High-level flow:

Input Data → Parser Agent → Question Agent → Page Generation Agents → JSON Outputs

---

### 2. Core Components

#### a. Input Layer

* `input_data.py`
* Contains the raw product dataset as a structured dictionary.

---

#### b. Data Models

* `Product` model
* `Question` model

These models enforce internal data consistency and define the structured format passed between agents.

---

#### c. Agents Layer

Each agent has one clear responsibility:

* **ParserAgent**

  * Converts raw input dictionary into a structured `Product` model

* **QuestionGenerationAgent**

  * Generates exactly 15 questions across 15 distinct categories

* **FAQAgent**

  * Converts categorized questions into structured FAQ JSON using logic blocks and templates

* **ProductPageAgent**

  * Builds the product description JSON using reusable logic blocks

* **ComparisonAgent**

  * Creates a fictional Product B and generates a structured comparison JSON

---

#### d. Reusable Logic Blocks

Logic blocks apply deterministic transformation rules and can be reused across multiple agents:

* Benefits transformation
* Usage extraction
* Safety messaging
* Ingredients extraction
* Structured comparison logic

These blocks ensure separation between business logic and page layout.

---

#### e. Template Engine

Custom-built template functions define the exact JSON structure for each page type:

* FAQ Template
* Product Page Template
* Comparison Page Template

Templates define:

* Required fields
* Formatting rules
* Dependencies on logic blocks

---

#### f. Orchestration Layer

* `orchestrator.py`
* Controls full execution order of agents
* Ensures that:

  * Parsing occurs first
  * Question generation happens next
  * Page generation agents run last
* Handles final JSON file output to the `outputs/` directory

---

### 3. Data Flow Summary

1. Raw product data is loaded
2. Parser Agent creates internal product model
3. Question Agent generates 15 categorized questions
4. FAQ Agent generates FAQ JSON
5. Product Page Agent generates product JSON
6. Comparison Agent generates comparison JSON with fictional Product B
7. Orchestrator saves all outputs as clean JSON files

---

### 4. Design Principles Followed

* Single Responsibility per Agent
* No hidden global state
* Deterministic rule-based transformations
* Template-driven output generation
* Fully modular and extensible design

---

## Final Summary

This system demonstrates a production-style **multi-agent automation pipeline** that cleanly separates responsibilities across agents, logic blocks, templates, and orchestration. The output is fully structured, machine-readable, and generated without any manual intervention or UI dependency. It directly satisfies all architectural, automation, and output requirements defined in the Kasparro Applied AI Engineer challenge.
