

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_pymt_schedulesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                type_code: Optional[int]
            
        
    
        
            
                type_desc : str
            
         
    
        
    


class m_pymt_schedulesInfoCreate(m_pymt_schedulesInfoBase):
    pass

class m_pymt_schedulesInfoUpdate(m_pymt_schedulesInfoBase):
    pass

class m_pymt_schedulesInfoInDBBase(m_pymt_schedulesInfoBase):
    class Config:
        orm_mode = True

class m_pymt_schedulesInfo(m_pymt_schedulesInfoInDBBase):
    pass

