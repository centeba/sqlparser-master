import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class f_acct_positions(Base):  # type: ignore
    __tablename__ = "f_acct_positions"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    security_id: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	

	
    maturity_date: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	

	

	
    custodian: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	
    date_acquired: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    is_annuity: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

	

	

	

	

