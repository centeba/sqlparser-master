import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class p_l_loan_eligibility(Base):  # type: ignore
    __tablename__ = "p_l_loan_eligibility"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    reason_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=12), nullable=True, unique=)
	

	
    reason_desc: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	

