# 🚀 Multi-Agent Content Generation System

<<<<<<< HEAD
This project is a Python-based multi-agent AI content generation system designed to demonstrate how a modular, production-grade automation pipeline can transform a structured product dataset into multiple machine-readable JSON content pages. The system uses independent AI agents powered by LangGraph, reusable logic blocks, a custom template engine, and a shared state orchestrator to automatically generate a FAQ page, a product description page, and a comparison page featuring an LLM-generated fictional product. The focus of the project is on clean system architecture, intelligent agent orchestration, and deterministic structured output generation—rather than UI development or static prompt-based content creation.

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
=======
This project is a Python-based multi-agent content generation system designed to demonstrate how a modular, production-style automation pipeline can transform a structured product dataset into multiple machine-readable JSON content pages. The system uses independent agents, reusable logic blocks, a custom template engine, and a centralized orchestrator to automatically generate a FAQ page, a product description page, and a comparison page with a fictional product. The focus of the project is on clean system architecture, agent orchestration, and deterministic, structured output generation rather than UI or prompt-based content creation.

---

## 🗂️ System Structure

<img width="923" height="1422" alt="Screenshot 2025-12-08 213226" src="https://github.com/user-attachments/assets/ec60cbbb-888a-4d45-be1e-b21057fad369" />

## Sequence diagram

<img width="1383" height="1474" alt="Screenshot 2025-12-08 213356" src="https://github.com/user-attachments/assets/ad5886d4-81c9-4174-bd0a-72a7dc886271" />

## Flowchart

<img width="1439" height="1538" alt="Screenshot 2025-12-08 213558" src="https://github.com/user-attachments/assets/c81d9c83-6f29-4cee-91f1-435d80b387e1" />
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd

---

## 📝 Documentation

For detailed system design documentation, see:

```
docs/projectdocumentation.md
```
