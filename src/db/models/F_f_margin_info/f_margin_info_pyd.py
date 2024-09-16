

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_margin_infoInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class f_margin_infoInfoCreate(f_margin_infoInfoBase):
    pass

class f_margin_infoInfoUpdate(f_margin_infoInfoBase):
    pass

class f_margin_infoInfoInDBBase(f_margin_infoInfoBase):
    class Config:
        orm_mode = True

class f_margin_infoInfo(f_margin_infoInfoInDBBase):
    pass

