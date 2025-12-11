from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    product_name: str = Field(...)
    concentration: str = Field(default="")
    skin_type: List[str] = Field(default_factory=list)
    key_ingredients: List[str] = Field(default_factory=list)
    benefits: List[str] = Field(default_factory=list)
    how_to_use: str = Field(default="")
    side_effects: str = Field(default="")
    price: float = Field(default=0.0)
    currency: str = Field(default="INR")

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(**data)
