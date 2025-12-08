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
