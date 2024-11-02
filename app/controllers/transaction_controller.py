from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.transaction import Transaction
from ..views.transaction_view import TransactionCreate, TransactionResponse

router = APIRouter()


@router.post("/transactions/", response_model=TransactionResponse)
def create_transaction(
    transaction: TransactionCreate, db: Session = Depends(get_db)
) -> Transaction:
    db_transaction = Transaction(
        symbol=transaction.symbol,
        quantity=transaction.quantity,
        price=transaction.price,
        transaction_type=transaction.transaction_type,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@router.get("/transactions/", response_model=list[TransactionResponse])
def get_transactions(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> list[Transaction]:
    transactions = db.query(Transaction).offset(skip).limit(limit).all()
    return transactions


@router.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transaction(transaction_id: int, db: Session = Depends(get_db)) -> Transaction:
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
