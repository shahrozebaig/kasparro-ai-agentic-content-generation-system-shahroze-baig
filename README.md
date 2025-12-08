# 🚀 Kasparro – Multi-Agent Content Generation System

A Python-based multi-agent automation system that transforms a single structured product dataset into multiple machine-readable JSON content pages using modular agents, reusable logic blocks, and a custom template engine.

---

## 🗂️ Project Structure

```
kasparro-ai-agentic-content-generation-system/
│
├── agents/                    
│   ├── parser_agent.py
│   ├── question_agent.py
│   ├── faq_agent.py
│   ├── product_agent.py
│   └── comparison_agent.py
│
├── logic_blocks/              
│   ├── benefits_block.py
│   ├── usage_block.py
│   ├── safety_block.py
│   └── comparison_block.py
│
├── templates/                
│   ├── faq_template.py
│   ├── product_template.py
│   └── comparison_template.py
│
├── models/                    
│   ├── product.py
│   └── question.py
│
├── outputs/                   
│   ├── faq.json
│   ├── product_page.json
│   └── comparison_page.json
│
├── orchestrator.py            
├── input_data.py              
└── README.md
```

---

## 🔧 System Design

### Key Components

**1. Parser Agent**
- Converts raw input dictionary into structured `Product` model
- Enforces data validation

**2. Question Generation Agent**
- Generates exactly 15 questions across 15 distinct categories
- Produces structured `Question` objects

**3. FAQ Agent**
- Converts categorized questions into structured FAQ JSON
- Uses logic blocks and templates

**4. Product Page Agent**
- Builds product description JSON using reusable logic blocks
- Structures all product information

**5. Comparison Agent**
- Creates fictional Product B internally
- Generates structured comparison JSON

**6. Logic Blocks**
- Benefits transformation
- Usage extraction
- Safety messaging
- Ingredients extraction
- Structured comparison logic

**7. Template Engine**
- Defines exact JSON structure for each page type
- Specifies required fields and formatting rules

**8. Orchestrator**
- Controls execution order of agents
- Ensures proper pipeline flow
- Handles JSON file output

---

## 📊 Data Flow

1. Raw product data is loaded from `input_data.py`
2. **Parser Agent** creates internal `Product` model
3. **Question Agent** generates 15 categorized questions
4. **FAQ Agent** generates `faq.json`
5. **Product Page Agent** generates `product_page.json`
6. **Comparison Agent** generates `comparison_page.json` with fictional Product B
7. **Orchestrator** saves all outputs to `outputs/` directory

---

## 📝 Documentation

For detailed system design documentation, see:

```
docs/projectdocumentation.md
```

---
