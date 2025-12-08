from typing import Dict, Any
from models import Product
from logic_blocks import (
    generate_benefits_copy,
    generate_usage_copy,
    generate_safety_copy,
    generate_ingredients_copy,
)
from templates import build_product_page

class ProductPageAgent:
    def run(self, product: Product) -> Dict[str, Any]:
        benefits_copy = generate_benefits_copy(product)
        usage_copy = generate_usage_copy(product)
        safety_copy = generate_safety_copy(product)
        ingredients_copy = generate_ingredients_copy(product)

        page = build_product_page(
            product=product,
            benefits_copy=benefits_copy,
            usage_copy=usage_copy,
            safety_copy=safety_copy,
            ingredients_copy=ingredients_copy,
        )
        return page
