from sqlalchemy import ForeignKey, String, Integer, Float, Numeric, DateTime, Date, Time, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from .config import Base
from decimal import Decimal
from datetime import datetime, date, time
import enum


class Nature(Base):
    __tablename__ = "nature_db"
    pk_nature: Mapped[int] = mapped_column(primary_key=True)
    nature_group: Mapped[str] = mapped_column(String(50), nullable=False)
    nature_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    #posts: Mapped[List["Post"]] = relationship(back_populates="author")

class Person(Base):
    __tablename__ = "person_db"
    pk_person: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    #posts: Mapped[List["Post"]] = relationship(back_populates="author")

class Bank(Base):
    __tablename__ = "bank_db"
    pk_bank: Mapped[int] = mapped_column(primary_key=True)
    bank_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    credit: Mapped[bool] = mapped_column(default=True)
    debit: Mapped[bool] = mapped_column(default=True)
    stocks: Mapped[bool] = mapped_column(default=True)
    day_credit_payment: Mapped[int] = mapped_column()

    #posts: Mapped[List["Post"]] = relationship(back_populates="author")

class Entity(Base):
    __tablename__ = "entity_db"
    pk_entity: Mapped[int] = mapped_column(primary_key=True)
    entity_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    number_a: Mapped[int] = mapped_column()
    complement: Mapped[str] = mapped_column(String(50))
    street: Mapped[str] = mapped_column(String(50))
    neighborhood: Mapped[str] = mapped_column(String(50))
    city: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(50))

    #posts: Mapped[List["Post"]] = relationship(back_populates="author")

class PaymentMethods(enum.Enum):
    CREDIT = "credit"
    DEBIT = "debit"

class InOrOut(enum.Enum):
    IN = "in"
    OUT = "out"

class Moviment(Base):
    __tablename__ = "moviment_db"
    pk_moviment: Mapped[int] = mapped_column(primary_key=True)
    spend_description: Mapped[str] = mapped_column(String(50), nullable=False)
    fk_entity: Mapped[int] = mapped_column(ForeignKey("entity_db.pk_entity"), nullable=False)
    cost_value: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), default=0.00, nullable=False)
    installments: Mapped[int] = mapped_column()
    fk_nature: Mapped[int] = mapped_column(ForeignKey("nature_db.pk_nature"), nullable=False)
    period_date: Mapped[date] = mapped_column(Date, server_default=func.now())
    fk_bank: Mapped[int] = mapped_column(ForeignKey("bank_db.pk_bank"), nullable=False)
    payment_method: Mapped[PaymentMethods] = mapped_column(Enum(PaymentMethods), nullable=False)
    fk_person: Mapped[int] = mapped_column(ForeignKey("person_db.pk_person"), nullable=False)
    in_out: Mapped[bool] = mapped_column(Enum(InOrOut), nullable=False)
    paied: Mapped[bool] = mapped_column(default=False)

class FutureMoviment(Base):
    __tablename__ = "future_moviment_db"
    pk_fm: Mapped[int] = mapped_column(primary_key=True)
    spend_description: Mapped[str] = mapped_column(String(50), nullable=False)
    fk_entity: Mapped[int] = mapped_column(ForeignKey("entity_db.pk_entity"), nullable=False)
    total: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), default=0.00, nullable=False)
    value_installment: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), default=0.00, nullable=False)
    init_date: Mapped[date] = mapped_column(Date, server_default=func.now())
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    fk_nature: Mapped[int] = mapped_column(ForeignKey("nature_db.pk_nature"), nullable=False)
    fk_bank: Mapped[int] = mapped_column(ForeignKey("bank_db.pk_bank"), nullable=False)
    payment_method: Mapped[PaymentMethods] = mapped_column(Enum(PaymentMethods), nullable=False)
    fk_person: Mapped[int] = mapped_column(ForeignKey("person_db.pk_person"), nullable=False)
    in_out: Mapped[bool] = mapped_column(Enum(InOrOut), nullable=False)
    paied: Mapped[bool] = mapped_column(default=False)

