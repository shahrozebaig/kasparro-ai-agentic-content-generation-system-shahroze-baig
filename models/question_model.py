<<<<<<< HEAD
from pydantic import BaseModel

class Question(BaseModel):
=======
from dataclasses import dataclass

@dataclass
class Question:
>>>>>>> a45da5129a34f31c80f2a5e0334180f00f6b8dcd
    text: str
    category: str
