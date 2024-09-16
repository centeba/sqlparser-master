

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_mortgage_typesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                loan_type : str
            
         
    
        
            
                type_desc : str
            
         
    
        
    


class m_mortgage_typesInfoCreate(m_mortgage_typesInfoBase):
    pass

class m_mortgage_typesInfoUpdate(m_mortgage_typesInfoBase):
    pass

class m_mortgage_typesInfoInDBBase(m_mortgage_typesInfoBase):
    class Config:
        orm_mode = True

class m_mortgage_typesInfo(m_mortgage_typesInfoInDBBase):
    pass

