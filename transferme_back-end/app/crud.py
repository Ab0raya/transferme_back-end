from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_card(db: Session, card: schemas.CardCreate, user_id: int):
    db_card = models.Card(**card.dict(), owner_id=user_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_cards(db: Session, user_id: int):
    return db.query(models.Card).filter(models.Card.owner_id == user_id).all()


def ct(db: Session, transaction: schemas.TransactionCreate):
    # Ensure the receiver exists
    receiver = db.query(models.Receiver).filter(models.Receiver.id == transaction.receiver_id).first()
    if not receiver:
        raise HTTPException(status_code=400, detail="Receiver does not exist")

    # Proceed to create the transaction
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

