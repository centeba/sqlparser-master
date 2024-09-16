

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class managed_futuresInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                valuation_type : int
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class managed_futuresInfoCreate(managed_futuresInfoBase):
    pass

class managed_futuresInfoUpdate(managed_futuresInfoBase):
    pass

class managed_futuresInfoInDBBase(managed_futuresInfoBase):
    class Config:
        orm_mode = True

class managed_futuresInfo(managed_futuresInfoInDBBase):
    pass

