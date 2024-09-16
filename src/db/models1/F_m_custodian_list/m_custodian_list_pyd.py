

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_custodian_listInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                cust_code: Optional[str]
            
         
    
        
            
                cust_name: Optional[str]
            
         
    
        
    


class m_custodian_listInfoCreate(m_custodian_listInfoBase):
    pass

class m_custodian_listInfoUpdate(m_custodian_listInfoBase):
    pass

class m_custodian_listInfoInDBBase(m_custodian_listInfoBase):
    class Config:
        orm_mode = True

class m_custodian_listInfo(m_custodian_listInfoInDBBase):
    pass

