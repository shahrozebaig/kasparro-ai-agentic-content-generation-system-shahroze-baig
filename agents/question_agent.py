from typing import List
from models import Product, Question

class QuestionGenerationAgent:
    def run(self, product: Product) -> List[Question]:
        questions: List[Question] = []
        name = product.product_name
        concentration = product.concentration
        skin = ", ".join(product.skin_type)
        ingredients = ", ".join(product.key_ingredients)

        questions.append(
            Question(
                text=f"What skin types is {name} suitable for?",
                category="informational",
            )
        )
        questions.append(
            Question(
                text=f"What is the concentration of Vitamin C in {name}?",
                category="informational",
            )
        )
        questions.append(
            Question(
                text=f"What are the key ingredients in {name}?",
                category="informational",
            )
        )
        questions.append(
            Question(
                text=f"How should I use {name} in my daily routine?",
                category="usage",
            )
        )
        questions.append(
            Question(
                text=f"Can I use {name} in the morning?",
                category="usage",
            )
        )
        questions.append(
            Question(
                text=f"Should I apply sunscreen after using {name}?",
                category="usage",
            )
        )
        questions.append(
            Question(
                text=f"Can I use {name} with other skincare products?",
                category="usage",
            )
        )
        questions.append(
            Question(
                text=f"Are there any side effects when using {name}?",
                category="safety",
            )
        )
        questions.append(
            Question(
                text=f"Is {name} safe for sensitive skin?",
                category="safety",
            )
        )
        questions.append(
            Question(
                text=f"Can I use {name} every day?",
                category="safety",
            )
        )
        questions.append(
            Question(
                text=f"What benefits can I expect from using {name}?",
                category="informational",
            )
        )
        questions.append(
            Question(
                text=f"Will {name} help with dark spots?",
                category="informational",
            )
        )
        questions.append(
            Question(
                text=f"How long will one bottle of {name} last if I use it daily?",
                category="purchase",
            )
        )
        questions.append(
            Question(
                text=f"Is {name} a good option for oily and combination skin compared to other serums?",
                category="comparison",
            )
        )
        questions.append(
            Question(
                text=f"What makes {name} different from other Vitamin C serums?",
                category="comparison",
            )
        )

        if len(questions) < 15:
            questions.append(
                Question(
                    text=f"Can I apply moisturizer after using {name}?",
                    category="usage",
                )
            )

        return questions
