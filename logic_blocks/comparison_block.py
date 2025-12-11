from typing import Dict, Any
<<<<<<< HEAD
from models.product_model import Product

def generate_comparison(product_a: Product, product_b: Product) -> Dict[str, Any]:
    cheaper = product_a.price < product_b.price
    higher_conc = product_a.concentration != product_b.concentration and product_a.concentration > product_b.concentration if isinstance(product_a.concentration, (int, float)) and isinstance(product_b.concentration, (int, float)) else None
    better_for = list(set(product_a.skin_type) - set(product_b.skin_type)) or list(set(product_b.skin_type) - set(product_a.skin_type))
    notable_ingredients = {
        product_a.product_name: product_a.key_ingredients,
        product_b.product_name: product_b.key_ingredients
    }
    return {
        "cheaper": product_a.product_name if cheaper else product_b.product_name,
        "higher_concentration": product_a.product_name if higher_conc else (product_b.product_name if higher_conc is False else None),
        "better_for": better_for,
        "notable_ingredients": notable_ingredients
    }
=======
from models import Product

def generate_comparison(product_a: Product, product_b: Product) -> Dict[str, Any]:
    comparison = {
        "price": {
            product_a.product_name: {
                "value": product_a.price,
                "currency": product_a.currency,
            },
            product_b.product_name: {
                "value": product_b.price,
                "currency": product_b.currency,
            },
        },
        "concentration": {
            product_a.product_name: product_a.concentration,
            product_b.product_name: product_b.concentration,
        },
        "skin_type": {
            product_a.product_name: product_a.skin_type,
            product_b.product_name: product_b.skin_type,
        },
        "key_ingredients": {
            product_a.product_name: product_a.key_ingredients,
            product_b.product_name: product_b.key_ingredients,
        },
        "benefits": {
            product_a.product_name: product_a.benefits,
            product_b.product_name: product_b.benefits,
        },
    }
    return comparison
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
