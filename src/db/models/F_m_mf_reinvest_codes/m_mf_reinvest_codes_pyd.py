

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_mf_reinvest_codesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                reinvest_code : int
            
        
    
        
            
                code_description : str
            
         
    
        
    


class m_mf_reinvest_codesInfoCreate(m_mf_reinvest_codesInfoBase):
    pass

class m_mf_reinvest_codesInfoUpdate(m_mf_reinvest_codesInfoBase):
    pass

class m_mf_reinvest_codesInfoInDBBase(m_mf_reinvest_codesInfoBase):
    class Config:
        orm_mode = True

class m_mf_reinvest_codesInfo(m_mf_reinvest_codesInfoInDBBase):
    pass

