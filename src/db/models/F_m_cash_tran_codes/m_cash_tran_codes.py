import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class m_cash_tran_codes(Base):  # type: ignore
    __tablename__ = "m_cash_tran_codes"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    tran_type: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    tran_description: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	

