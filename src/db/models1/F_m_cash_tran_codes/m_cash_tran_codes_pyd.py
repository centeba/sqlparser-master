

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_cash_tran_codesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                tran_type : str
            
         
    
        
            
                tran_description : str
            
         
    
        
    


class m_cash_tran_codesInfoCreate(m_cash_tran_codesInfoBase):
    pass

class m_cash_tran_codesInfoUpdate(m_cash_tran_codesInfoBase):
    pass

class m_cash_tran_codesInfoInDBBase(m_cash_tran_codesInfoBase):
    class Config:
        orm_mode = True

class m_cash_tran_codesInfo(m_cash_tran_codesInfoInDBBase):
    pass

