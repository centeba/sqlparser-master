import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class org_pos_ext(Base):  # type: ignore
    __tablename__ = "org_pos_ext"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    attr_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    attr_data: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    attr_data_type: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    account_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	

	

