import json
import re
from models.state_model import PipelineState
from utils.llm_client import llm_generate

PROMPT_COMPETITOR = """
Create a fictional competing skincare product similar to the following product.
Return ONLY valid JSON in this format:

{{
  "product_name": "...",
  "concentration": "...",
  "skin_type": ["...", "..."],
  "key_ingredients": ["...", "..."],
  "benefits": ["...", "..."],
  "how_to_use": "...",
  "side_effects": "...",
  "price": 999,
  "currency": "INR"
}}

Product A:
{product_json}
"""

PROMPT_COMPARISON = """
Compare the following two skincare products.
Return ONLY valid JSON in this format:

{{
  "narrative": "Detailed comparison paragraph.",
  "comparison": {{
    "cheaper": "...",
    "higher_concentration": "...",
    "better_for": ["skin-type", "..."],
    "notable_ingredients": {{
      "Product A": ["...", "..."],
      "Product B": ["...", "..."]
    }}
  }}
}}

Product A:
{product_a}

Product B:
{product_b}
"""

def extract_json(text):
    matches = re.findall(r'\{.*\}', text, re.DOTALL)
    if matches:
        return matches[0]
    return None

class ComparisonAgent:
    def run(self, state: PipelineState) -> PipelineState:
        prompt_b = PROMPT_COMPETITOR.format(
            product_json=state.product.json()
        )

        raw_b = llm_generate(prompt_b, max_tokens=600)
        json_b = extract_json(raw_b)
        if not json_b:
            raise ValueError("LLM competitor JSON invalid")

        competitor = state.product.__class__(**json.loads(json_b))
        state.product_b = competitor

        prompt_compare = PROMPT_COMPARISON.format(
            product_a=state.product.json(),
            product_b=competitor.json()
        )

        raw_compare = llm_generate(prompt_compare, max_tokens=900)
        json_compare = extract_json(raw_compare)
        if not json_compare:
            raise ValueError("LLM comparison JSON invalid")

        compare_data = json.loads(json_compare)

        state.comparison_page = {
            "product_a": state.product.model_dump(),
            "product_b": competitor.model_dump(),
            "narrative": compare_data["narrative"],
            "comparison": compare_data["comparison"]
        }

        state.logs.append("ComparisonAgent: generated comparison reasoning")

        return state
