

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_security_typesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                sec_type : str
            
         
    
        
            
                sec_description : str
            
         
    
        
    


class m_security_typesInfoCreate(m_security_typesInfoBase):
    pass

class m_security_typesInfoUpdate(m_security_typesInfoBase):
    pass

class m_security_typesInfoInDBBase(m_security_typesInfoBase):
    class Config:
        orm_mode = True

class m_security_typesInfo(m_security_typesInfoInDBBase):
    pass

