<<<<<<< HEAD
import json
from models.state_model import PipelineState
from utils.llm_client import llm_generate
from config import settings

PROMPT = """
You are an expert skincare assistant. Given a product JSON and a user question, provide a concise, accurate answer.
Return plain text or JSON. Product: {product}
Question: {question}
"""

class FAQAgent:
    def run(self, state: PipelineState) -> PipelineState:
        if not state.product:
            raise RuntimeError("No product in state")
        faqs = []
        limit = settings.faq_limit
        for q in state.questions:
            if len(faqs) >= limit:
                break
            prompt = PROMPT.format(product=state.product.json(), question=q.text)
            try:
                ans = llm_generate(prompt, max_tokens=250)
                try:
                    parsed = json.loads(ans)
                    answer = parsed.get("answer") or parsed.get("response") or ans
                except Exception:
                    answer = ans
            except Exception:
                answer = "Sorry, unable to generate answer at this time."
            faqs.append({"question": q.text, "answer": answer})
        state.faqs = faqs
        state.logs.append(f"FAQAgent: generated {len(faqs)} faqs")
        return state
=======
from typing import List, Dict, Any
from models import Product, Question
from logic_blocks import (
    generate_usage_copy,
    generate_safety_copy,
    generate_benefits_copy,
)
from templates import build_faq_page

class FAQAgent:
    def run(self, product: Product, questions: List[Question]) -> Dict[str, Any]:
        faqs: List[Dict[str, str]] = []
        usage_copy = generate_usage_copy(product)
        safety_copy = generate_safety_copy(product)
        benefits_copy = generate_benefits_copy(product)

        for question in questions:
            if len(faqs) >= 8:
                break
            answer = ""
            if question.category == "usage":
                answer = usage_copy
            elif question.category == "safety":
                answer = safety_copy
            elif question.category == "informational":
                if "benefits" in question.text.lower():
                    answer = "; ".join(benefits_copy)
                elif "dark spots" in question.text.lower():
                    answer = "It helps fade the appearance of dark spots over time."
                elif "skin types" in question.text.lower():
                    answer = f"It is suitable for {', '.join(product.skin_type)} skin types."
                elif "concentration" in question.text.lower():
                    answer = f"It contains {product.concentration}."
                elif "ingredients" in question.text.lower():
                    answer = ", ".join(product.key_ingredients)
                else:
                    answer = "; ".join(benefits_copy)
            else:
                answer = "This question is related to how the serum fits into your routine and preferences."

            faqs.append(
                {
                    "question": question.text,
                    "answer": answer,
                }
            )

        page = build_faq_page(product, faqs)
        return page
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
