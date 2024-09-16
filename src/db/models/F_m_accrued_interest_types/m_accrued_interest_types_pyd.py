

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_accrued_interest_typesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                int_code: Optional[int]
            
        
    
        
            
                int_type : str
            
         
    
        
    


class m_accrued_interest_typesInfoCreate(m_accrued_interest_typesInfoBase):
    pass

class m_accrued_interest_typesInfoUpdate(m_accrued_interest_typesInfoBase):
    pass

class m_accrued_interest_typesInfoInDBBase(m_accrued_interest_typesInfoBase):
    class Config:
        orm_mode = True

class m_accrued_interest_typesInfo(m_accrued_interest_typesInfoInDBBase):
    pass

