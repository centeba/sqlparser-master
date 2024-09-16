import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class f_security_master(Base):  # type: ignore
    __tablename__ = "f_security_master"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    ticker_symbol: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    cash_equiv: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	
    close_price_as_of_date: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=False, autoincrement="auto")
	

	

	
    isin: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    cusip: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    ticker: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    sedol: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    institution_id: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    institution_sec_id: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    proxy_security_id: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	

