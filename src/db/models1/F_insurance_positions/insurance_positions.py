import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class insurance_positions(Base):  # type: ignore
    __tablename__ = "insurance_positions"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    carrier: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    policy_num: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=24), nullable=True, unique=)
	

	
    policy_type: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=4), nullable=True, unique=)
	

	

	

	

	

	
    policy_status: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	
    carrier_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=8), nullable=True, unique=)
	

	
    policy_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=6), nullable=True, unique=)
	

	
    issue_date: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    renewal_date_fixed: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	

	

	

	
    policy_role: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

