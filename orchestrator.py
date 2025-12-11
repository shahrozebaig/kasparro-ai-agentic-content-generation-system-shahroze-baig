<<<<<<< HEAD
import os
import json
from config import settings
from input_data import PRODUCT_DATA
from models.state_model import PipelineState
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent

class Orchestrator:
    def __init__(self):
        self.state = PipelineState()
        self.parser = ParserAgent()
        self.question = QuestionGenerationAgent()
        self.faq = FAQAgent()
        self.product = ProductPageAgent()
        self.comparison = ComparisonAgent()
        self.outputs = settings.outputs_dir

    def run(self):
        self.state = self.parser.run(self.state, PRODUCT_DATA)
        self.state = self.question.run(self.state)
        self.state = self.faq.run(self.state)
        self.state = self.product.run(self.state)
        self.state = self.comparison.run(self.state)
        os.makedirs(self.outputs, exist_ok=True)
        self.write_json(os.path.join(self.outputs, "faq.json"), {"product_name": self.state.product.product_name, "faqs": self.state.faqs})
        self.write_json(os.path.join(self.outputs, "product_page.json"), self.state.product_page)
        self.write_json(os.path.join(self.outputs, "comparison_page.json"), self.state.comparison_page)
        self.write_json(os.path.join(self.outputs, "run_logs.json"), {"logs": self.state.logs})

    def write_json(self, path: str, data):
=======
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
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
<<<<<<< HEAD
    orch = Orchestrator()
    orch.run()
=======
    orchestrator = Orchestrator()
    orchestrator.run()
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
