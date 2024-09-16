import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class f_margin_call(Base):  # type: ignore
    __tablename__ = "f_margin_call"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    date_trade: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    date_settle: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	

	

	
    in_violation: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    margin_call_type: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    date_extension: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    date_sellout: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	

	

