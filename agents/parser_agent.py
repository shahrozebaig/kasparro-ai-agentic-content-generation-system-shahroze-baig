from typing import Dict, Any
from models.product_model import Product
from models.state_model import PipelineState

class ParserAgent:
    def run(self, state: PipelineState, raw_data: Dict[str, Any]) -> PipelineState:
        product = Product.from_dict(raw_data)
        state.product = product
        state.logs.append("ParserAgent: parsed product")
        return state
