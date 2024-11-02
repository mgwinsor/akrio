from datetime import datetime

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    symbol: str
    quantity: float
    price: float
    transaction_type: str


class TransactionResponse(BaseModel):
    id: int
    symbol: str
    quantity: float
    price: float
    transaction_type: str
    timestamp: datetime

    class Config:
        from_attributes = True
