

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_liabilitiesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
            
                apr_type : int
            
        
    
        
    
        
    
        
            
                is_overdue : int
            
        
    
        
    
        
             
                last_pymt_date : date
             
        
    
        
    
        
    
        
    
        
    


class l_liabilitiesInfoCreate(l_liabilitiesInfoBase):
    pass

class l_liabilitiesInfoUpdate(l_liabilitiesInfoBase):
    pass

class l_liabilitiesInfoInDBBase(l_liabilitiesInfoBase):
    class Config:
        orm_mode = True

class l_liabilitiesInfo(l_liabilitiesInfoInDBBase):
    pass

