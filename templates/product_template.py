from typing import Dict, Any, List
from models.product_model import Product

def build_product_page(
    product: Product,
    benefits_copy: List[str],
    usage_copy: str,
    safety_copy: str,
    ingredients_copy: List[str],
) -> Dict[str, Any]:
    page = {
        "page_type": "product_description",
        "product_name": product.product_name,
        "concentration": product.concentration,
        "skin_type": product.skin_type,
        "key_ingredients": ingredients_copy,
        "benefits": benefits_copy,
        "usage_instructions": usage_copy,
        "safety_information": safety_copy,
        "price": {
            "value": product.price,
            "currency": product.currency,
        },
    }
    return page
