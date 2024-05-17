from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Keyval(BaseModel):
    key: str
    value: str


class HashKeyval(Keyval):
    field: str | None = None


class ZetKeyval(Keyval):
    score: float
