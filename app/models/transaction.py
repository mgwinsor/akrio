from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from ..database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    quantity = Column(Float)
    price = Column(Float)
    transaction_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow())
