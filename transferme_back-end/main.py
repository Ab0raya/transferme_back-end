from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from app import crud, models, schemas
# from app.database import SessionLocal, engine
from app import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return cu(db=db, user=user)


@app.get("/users/{user_id}/cards/", response_model= List[schemas.Card])
def get_user_cards(user_id: int, db: Session = Depends(get_db)):
    return get_cards(db=db, user_id=user_id)


@app.post("/users/{user_id}/cards/", response_model=schemas.Card)
def create_user_card(user_id: int, card: schemas.CardCreate, db: Session = Depends(get_db)):
    return create_card(db=db, card=card, user_id=user_id)


from sqlalchemy.exc import IntegrityError

@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    try:
        return ct(db=db, transaction=transaction)
    except IntegrityError as e:
        raise HTTPException(status_code=400, detail="Invalid card or receiver ID") from e

