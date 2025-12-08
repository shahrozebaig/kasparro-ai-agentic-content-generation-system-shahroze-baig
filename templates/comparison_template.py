from typing import Dict, Any
from models import Product

def build_comparison_page(
    product_a: Product,
    product_b: Product,
    comparison_data: Dict[str, Any],
) -> Dict[str, Any]:
    page = {
        "page_type": "comparison",
        "product_a": {
            "product_name": product_a.product_name,
            "concentration": product_a.concentration,
            "skin_type": product_a.skin_type,
            "key_ingredients": product_a.key_ingredients,
            "benefits": product_a.benefits,
            "price": {
                "value": product_a.price,
                "currency": product_a.currency,
            },
        },
        "product_b": {
            "product_name": product_b.product_name,
            "concentration": product_b.concentration,
            "skin_type": product_b.skin_type,
            "key_ingredients": product_b.key_ingredients,
            "benefits": product_b.benefits,
            "price": {
                "value": product_b.price,
                "currency": product_b.currency,
            },
        },
        "comparison": comparison_data,
    }
    return page
