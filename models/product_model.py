<<<<<<< HEAD
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
=======
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Product:
    product_name: str
    concentration: str
    skin_type: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    how_to_use: str
    side_effects: str
    price: int
    currency: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        return cls(
            product_name=data.get("product_name", ""),
            concentration=data.get("concentration", ""),
            skin_type=list(data.get("skin_type", [])),
            key_ingredients=list(data.get("key_ingredients", [])),
            benefits=list(data.get("benefits", [])),
            how_to_use=data.get("how_to_use", ""),
            side_effects=data.get("side_effects", ""),
            price=int(data.get("price", 0)),
            currency=data.get("currency", "INR"),
        )
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
