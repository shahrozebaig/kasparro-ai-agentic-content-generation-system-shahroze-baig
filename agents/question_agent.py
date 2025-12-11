import json
import re
from models.question_model import Question
from models.state_model import PipelineState
from utils.llm_client import llm_generate

PROMPT = """
You are an expert skincare assistant.
Generate EXACTLY 15 FAQ questions about the following product.
Return ONLY valid JSON in this format:

[
  {{"text": "QUESTION HERE", "category": "CATEGORY HERE"}},
  ...
]

Product:
{product_json}
"""

def extract_json(text):
    matches = re.findall(r'\[.*\]', text, re.DOTALL)
    if matches:
        return matches[0]
    return None

class QuestionGenerationAgent:
    def run(self, state: PipelineState) -> PipelineState:
        if not state.product:
            raise RuntimeError("No product in state")

        prompt = PROMPT.format(product_json=state.product.json())
        raw = llm_generate(prompt, max_tokens=800)

        json_block = extract_json(raw)
        if not json_block:
            raise ValueError("LLM did not return valid JSON array")

        try:
            data = json.loads(json_block)
            questions = [Question(**q) for q in data]
        except Exception as e:
            raise ValueError(f"Failed to parse LLM JSON: {e}")

        state.questions = questions
        state.logs.append(f"QuestionGenerationAgent: generated {len(questions)} questions")

        return state
