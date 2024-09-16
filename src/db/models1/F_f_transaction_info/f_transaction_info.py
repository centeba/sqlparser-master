import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class f_transaction_info(Base):  # type: ignore
    __tablename__ = "f_transaction_info"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    date_transaction: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=False, autoincrement="auto")
	

	
    date_effective: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=False, autoincrement="auto")
	

	
    date_trade: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=False, autoincrement="auto")
	

	
    date_settle: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=False, autoincrement="auto")
	

	
    security_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    buy_or_sell: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	

	

	

	

	

	

	

	

	

	
    tran_exchange: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    tran_broker: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    tran_reinvest_code: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	
    account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	

	

