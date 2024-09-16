import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class m_acct_types(Base):  # type: ignore
    __tablename__ = "m_acct_types"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    acct_category: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    acct_types: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    acct_type_desc: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	

