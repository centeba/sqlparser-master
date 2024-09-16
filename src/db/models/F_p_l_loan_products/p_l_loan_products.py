import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class p_l_loan_products(Base):  # type: ignore
    __tablename__ = "p_l_loan_products"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    loan_type: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=12), nullable=True, unique=)
	

	
    can_deduct_tax: Mapped[sqlalchemy.types.Boolean] = mapped_column(sqlalchemy.Boolean, primary_key=False, nullable=True, autoincrement="auto")
	

	

	
    loan_description: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    penalty_prepay: Mapped[sqlalchemy.types.Boolean] = mapped_column(sqlalchemy.Boolean, primary_key=False, nullable=True, autoincrement="auto")
	

	
    loan_product: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=8), nullable=True, unique=)
	

	
    coupon_adjustment_freq: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=8), nullable=True, unique=)
	

	

	
    first_coupon_change: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	

	

	

	

	

	
    risk_rating: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    underwriter: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=12), nullable=True, unique=)
	

	
    prepay_penalty: Mapped[sqlalchemy.types.Boolean] = mapped_column(sqlalchemy.Boolean, primary_key=False, nullable=True, autoincrement="auto")
	

	

	
    accrual_method: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=12), nullable=True, unique=)
	

	
    payment_freq: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=4), nullable=True, unique=)
	

	
    fee_type: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	
    note_type: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    index_code: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	

	

	

	

	

