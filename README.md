# 🚀 Multi-Agent Content Generation System

This project is a Python-based multi-agent AI content generation system designed to demonstrate how a modular, production-grade automation pipeline can transform a structured product dataset into multiple machine-readable JSON content pages. The system uses independent AI agents powered by LangGraph, reusable logic blocks, a custom template engine, and a shared state orchestrator to automatically generate a FAQ page, a product description page, and a comparison page featuring an LLM-generated fictional product. The focus of the project is on clean system architecture, intelligent agent orchestration, and deterministic structured output generation—rather than UI development or static prompt-based content creation.

---

## System Architecture

<img width="1849" height="476" alt="Screenshot 2025-12-11 200206" src="https://github.com/user-attachments/assets/9b7930ae-9e18-45da-9595-089b518a9545" />

<img width="2170" height="955" alt="Screenshot 2025-12-11 200343" src="https://github.com/user-attachments/assets/ae77ed71-378b-4a3c-ad61-2046635c383f" />

---

## 🏃 How to Run the System

Follow these steps to successfully run the Multi-Agent AI Content Generation System:

### **1️⃣ Install Dependencies**

Run the following command:

```
pip install -r requirements.txt
```

Use **Python 3.10 or 3.11** for best compatibility.

---

### **2️⃣ Set Up Environment Variables**

Create a `.env` file in the project root and add:

```
GROQ_API_KEY=your_api_key_here
LLM_MODEL=llama-3.1-8b-instant
```

Replace `your_api_key_here` with your actual Groq API key.

---

### **3️⃣ Run the LangGraph Orchestrator (Recommended)**

This executes the full AI-powered multi-agent pipeline:

```
python langgraph_orchestrator.py
```

This generates:

* outputs/faq.json
* outputs/product_page.json
* outputs/comparison_page.json
* outputs/run_logs.json

---

### **4️⃣ Alternatively: Run the Simple Orchestrator**

Use this for basic deterministic execution:

```
python orchestrator.py
```

Outputs will still be saved into the **outputs** folder.

---

### **5️⃣ Run Tests (Optional)**

To verify output file creation:

```
pytest -q
```

---

## 📝 Documentation

For detailed system design documentation, see:

```
docs/projectdocumentation.md
```
