import json
from models.state_model import PipelineState
from utils.llm_client import llm_generate
from templates import build_product_page
from logic_blocks import generate_benefits_copy, generate_usage_copy, generate_safety_copy, generate_ingredients_copy

PROMPT = """
You are a product page writer. Given the product JSON, produce:
Return a JSON object: benefits (list), usage (str), safety (str), ingredients (list)
Product: {product}
"""

class ProductPageAgent:
    def run(self, state: PipelineState) -> PipelineState:
        if not state.product:
            raise RuntimeError("No product in state")
        prod_json = state.product.json()
        try:
            ans = llm_generate(PROMPT.format(product=prod_json), max_tokens=400)
            parsed = json.loads(ans)
            benefits = parsed.get("benefits", [])
            usage = parsed.get("usage", "")
            safety = parsed.get("safety", "")
            ingredients = parsed.get("ingredients", [])
        except Exception:
            benefits = generate_benefits_copy(state.product)
            usage = generate_usage_copy(state.product)
            safety = generate_safety_copy(state.product)
            ingredients = generate_ingredients_copy(state.product)
        state.product_page = build_product_page(
            product=state.product,
            benefits_copy=benefits,
            usage_copy=usage,
            safety_copy=safety,
            ingredients_copy=ingredients,
        )
        state.logs.append("ProductPageAgent: generated product page")
        return state
