from langgraph.graph import StateGraph, END
from models.state_model import PipelineState
from input_data import PRODUCT_DATA
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent
from config import settings
import json, os

parser = ParserAgent()
question_agent = QuestionGenerationAgent()
faq_agent = FAQAgent()
product_agent = ProductPageAgent()
comparison_agent = ComparisonAgent()

def to_state(data):
    if isinstance(data, PipelineState):
        return data
    return PipelineState(**data)

def node_parse(state):
    s = to_state(state)
    new_state = parser.run(s, PRODUCT_DATA)
    return new_state.model_dump()

def node_questions(state):
    s = to_state(state)
    new_state = question_agent.run(s)
    return new_state.model_dump()

def node_faq(state):
    s = to_state(state)
    new_state = faq_agent.run(s)
    return new_state.model_dump()

def node_product(state):
    s = to_state(state)
    new_state = product_agent.run(s)
    return new_state.model_dump()

def node_compare(state):
    s = to_state(state)
    new_state = comparison_agent.run(s)
    return new_state.model_dump()

workflow = StateGraph(PipelineState)

workflow.add_node("parse", node_parse)
workflow.add_node("questions", node_questions)
workflow.add_node("faqs", node_faq)
workflow.add_node("product_page", node_product)
workflow.add_node("comparison_page", node_compare)

workflow.set_entry_point("parse")

workflow.add_edge("parse", "questions")
workflow.add_edge("questions", "faqs")
workflow.add_edge("faqs", "product_page")
workflow.add_edge("product_page", "comparison_page")
workflow.add_edge("comparison_page", END)

app = workflow.compile()

class LangGraphOrchestrator:
    def __init__(self):
        self.outputs_dir = settings.outputs_dir

    def run(self):
        initial = PipelineState().model_dump()
        result = app.invoke(initial)

        final_state = PipelineState(**result)

        os.makedirs(self.outputs_dir, exist_ok=True)

        self._write("faq.json", {
            "faqs": final_state.faqs,
            "product_name": final_state.product.product_name
        })

        self._write("product_page.json", final_state.product_page)
        self._write("comparison_page.json", final_state.comparison_page)
        self._write("run_logs.json", {"logs": final_state.logs})

        return final_state

    def _write(self, filename, data):
        path = os.path.join(self.outputs_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    LangGraphOrchestrator().run()
