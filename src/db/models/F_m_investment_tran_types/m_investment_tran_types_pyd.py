

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_investment_tran_typesInfoBase(BaseModel):

    


class m_investment_tran_typesInfoCreate(m_investment_tran_typesInfoBase):
    pass

class m_investment_tran_typesInfoUpdate(m_investment_tran_typesInfoBase):
    pass

class m_investment_tran_typesInfoInDBBase(m_investment_tran_typesInfoBase):
    class Config:
        orm_mode = True

class m_investment_tran_typesInfo(m_investment_tran_typesInfoInDBBase):
    pass

