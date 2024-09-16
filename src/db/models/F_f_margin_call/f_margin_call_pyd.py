

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_margin_callInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
             
                date_trade : date
             
        
    
        
             
                date_settle : date
             
        
    
        
    
        
    
        
            
                in_violation : int
            
        
    
        
            
                margin_call_type : int
            
        
    
        
             
                date_extension : date
             
        
    
        
             
                date_sellout : date
             
        
    
        
    
        
    


class f_margin_callInfoCreate(f_margin_callInfoBase):
    pass

class f_margin_callInfoUpdate(f_margin_callInfoBase):
    pass

class f_margin_callInfoInDBBase(f_margin_callInfoBase):
    class Config:
        orm_mode = True

class f_margin_callInfo(f_margin_callInfoInDBBase):
    pass

