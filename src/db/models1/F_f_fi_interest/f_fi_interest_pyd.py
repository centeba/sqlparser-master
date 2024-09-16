

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_fi_interestInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_no: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                curr_local : int
            
        
    
        
    
        
    


class f_fi_interestInfoCreate(f_fi_interestInfoBase):
    pass

class f_fi_interestInfoUpdate(f_fi_interestInfoBase):
    pass

class f_fi_interestInfoInDBBase(f_fi_interestInfoBase):
    class Config:
        orm_mode = True

class f_fi_interestInfo(f_fi_interestInfoInDBBase):
    pass

