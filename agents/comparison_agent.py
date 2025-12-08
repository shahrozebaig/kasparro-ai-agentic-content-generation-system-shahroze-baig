from typing import Dict, Any
from models import Product
from logic_blocks import generate_comparison
from templates import build_comparison_page

class ComparisonAgent:
    def create_fictional_product_b(self, product_a: Product) -> Product:
        product_b = Product(
            product_name="RadiantLift Vitamin C Serum",
            concentration=product_a.concentration,
            skin_type=product_a.skin_type,
            key_ingredients=[product_a.key_ingredients[0], "Aloe Vera"],
            benefits=[
                "Brightening",
                "Helps even out skin tone",
            ],
            how_to_use=product_a.how_to_use,
            side_effects=product_a.side_effects,
            price=799,
            currency=product_a.currency,
        )
        return product_b

    def run(self, product: Product) -> Dict[str, Any]:
        product_b = self.create_fictional_product_b(product)
        comparison_data = generate_comparison(product, product_b)
        page = build_comparison_page(product, product_b, comparison_data)
        return page
