from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    image = Column(String(255))
    join_date = Column(DateTime, default=func.now())
    total_balance = Column(Float, default=0.0)
    total_income = Column(Float, default=0.0)
    total_expenses = Column(Float, default=0.0)

    cards = relationship("Card", back_populates="owner")


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String(16), unique=True, index=True)
    ccv = Column(String(3))
    expiry_date = Column(DateTime)
    service_provider = Column(String(255))

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="cards")
    transactions = relationship("Transaction", back_populates="card")


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    time = Column(String(10))
    date = Column(DateTime)
    details = Column(String(255))

    card_id = Column(Integer, ForeignKey("cards.id"))
    card = relationship("Card", back_populates="transactions")
    receiver_id = Column(Integer, ForeignKey("receivers.id"))
    receiver = relationship("Receiver", back_populates="transactions")


class Receiver(Base):
    __tablename__ = "receivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    card_number = Column(String(16), unique=True, index=True)
    service_provider = Column(String(255))

    transactions = relationship("Transaction", back_populates="receiver")


class Treatment(Base):
    __tablename__ = "treatments"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    receiver_service = Column(String(255))
    date = Column(DateTime)
    time = Column(String(10))
    details = Column(String(255))
