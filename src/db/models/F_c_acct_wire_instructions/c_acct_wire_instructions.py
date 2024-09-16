import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class c_acct_wire_instructions(Base):  # type: ignore
    __tablename__ = "c_acct_wire_instructions"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    currency_code: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    aba_num: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=12), nullable=True, unique=)
	

	
    bank_routing_num: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=24), nullable=True, unique=)
	

	
    bank_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    bank_address: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    bank_address_2: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    bank_address_3: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    bank_city_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    bank_state_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=10), nullable=True, unique=)
	

	
    bank_country_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=4), nullable=True, unique=)
	

	
    cust_account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    cust_account_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    fee_tag: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=10), nullable=True, unique=)
	

	
    obi_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    obi_account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	

	

