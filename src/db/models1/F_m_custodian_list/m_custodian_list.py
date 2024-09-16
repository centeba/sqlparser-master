import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class m_custodian_list(Base):  # type: ignore
    __tablename__ = "m_custodian_list"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    cust_code: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=10), nullable=False, unique=)
	

	
    cust_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	

