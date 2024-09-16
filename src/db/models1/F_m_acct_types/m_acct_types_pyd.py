

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_acct_typesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                acct_category: Optional[str]
            
         
    
        
            
                acct_types: Optional[str]
            
         
    
        
            
                acct_type_desc : str
            
         
    
        
    


class m_acct_typesInfoCreate(m_acct_typesInfoBase):
    pass

class m_acct_typesInfoUpdate(m_acct_typesInfoBase):
    pass

class m_acct_typesInfoInDBBase(m_acct_typesInfoBase):
    class Config:
        orm_mode = True

class m_acct_typesInfo(m_acct_typesInfoInDBBase):
    pass

