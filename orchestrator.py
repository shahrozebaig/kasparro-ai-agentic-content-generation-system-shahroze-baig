import json
import os
from typing import Any, Dict, List
from input_data import PRODUCT_DATA
from agents import (
    ParserAgent,
    QuestionGenerationAgent,
    FAQAgent,
    ProductPageAgent,
    ComparisonAgent,
)
from models import Question

class Orchestrator:
    def __init__(self) -> None:
        self.parser_agent = ParserAgent()
        self.question_agent = QuestionGenerationAgent()
        self.faq_agent = FAQAgent()
        self.product_agent = ProductPageAgent()
        self.comparison_agent = ComparisonAgent()

    def run(self) -> None:
        product = self.parser_agent.run(PRODUCT_DATA)
        questions: List[Question] = self.question_agent.run(product)
        faq_page: Dict[str, Any] = self.faq_agent.run(product, questions)
        product_page: Dict[str, Any] = self.product_agent.run(product)
        comparison_page: Dict[str, Any] = self.comparison_agent.run(product)
        os.makedirs("outputs", exist_ok=True)
        self.write_json("outputs/faq.json", faq_page)
        self.write_json("outputs/product_page.json", product_page)
        self.write_json("outputs/comparison_page.json", comparison_page)

    def write_json(self, path: str, data: Dict[str, Any]) -> None:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run()
