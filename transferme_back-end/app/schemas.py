from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TreatmentBase(BaseModel):
    amount: float
    receiver_service: str
    date: datetime
    time: str
    details: Optional[str] = None


class TreatmentCreate(TreatmentBase):
    pass


class Treatment(TreatmentBase):
    id: int

    class Config:
        orm_mode = True


class ReceiverBase(BaseModel):
    name: str
    card_number: str
    service_provider: str


class ReceiverCreate(ReceiverBase):
    pass


class Receiver(ReceiverBase):
    id: int

    class Config:
        orm_mode = True


class TransactionBase(BaseModel):
    amount: float
    time: str
    date: datetime
    details: Optional[str] = None


class TransactionCreate(TransactionBase):
    receiver_id: int
    card_id: int


class Transaction(TransactionBase):
    id: int
    receiver: Receiver

    class Config:
        orm_mode = True


class CardBase(BaseModel):
    card_number: str
    ccv: str
    expiry_date: datetime
    service_provider: str


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int
    transactions: List[Transaction] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    image: Optional[str] = None
    join_date: Optional[datetime] = None
    total_balance: float
    total_income: float
    total_expenses: float


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    cards: List[Card] = []

    class Config:
        orm_mode = True
