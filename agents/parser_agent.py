<<<<<<< HEAD
from typing import Dict, Any
from models.product_model import Product
from models.state_model import PipelineState

class ParserAgent:
    def run(self, state: PipelineState, raw_data: Dict[str, Any]) -> PipelineState:
        product = Product.from_dict(raw_data)
        state.product = product
        state.logs.append("ParserAgent: parsed product")
        return state
=======
from typing import Any, Dict
from models import Product

class ParserAgent:
    def run(self, raw_data: Dict[str, Any]) -> Product:
        product = Product.from_dict(raw_data)
        return product
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
