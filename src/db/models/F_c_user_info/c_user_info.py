import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class c_user_info(Base):  # type: ignore
    __tablename__ = "c_user_info"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    first_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    last_name: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=False, unique=)
	

	
    mobile_number: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=24), nullable=True, unique=)
	

	
    mobile_country_code: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=False, autoincrement="auto")
	

	

