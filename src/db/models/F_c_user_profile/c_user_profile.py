import sqlalchemy

from sqlalchemy import Column, Integer, String, Text, Boolean, Float, Date, TIMESTAMP, Time, JSON, ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


Base =  sqlalchemy.orm.declarative_base()

class c_user_profile(Base):  # type: ignore
    __tablename__ = "c_user_profile"


	
    system_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	
    alternate_email: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    anticipated_retirement_date: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    birthplace: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    birthdate: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    country_of_cit: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    country_of_origin: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    country_of_residence: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    date_of_death: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	
    date_of_marriage: Mapped[sqlalchemy.types.Date] = mapped_column(sqlalchemy.Date, primary_key=False, nullable=True, autoincrement="auto")
	

	

	
    drivers_license: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    edu_level: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    primary_email: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    employer: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    employer_address: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=256), nullable=True, unique=)
	

	
    employment_status: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    govt_id_doc: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    state_of_residence: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=10), nullable=True, unique=)
	

	
    govt_id_doc_num: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=100), nullable=True, unique=)
	

	
    gender: Mapped[sqlalchemy.types.String] = mapped_column(sqlalchemy.String(length=10), nullable=True, unique=)
	

	
    user_id: Mapped[sqlalchemy.types.Integer] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement="auto")
	

	

	

