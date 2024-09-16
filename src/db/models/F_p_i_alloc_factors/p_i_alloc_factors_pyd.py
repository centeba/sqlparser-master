

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_alloc_factorsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                alloc_factor : int
            
        
    
        
            
                factor_desc : str
            
         
    
        
    


class p_i_alloc_factorsInfoCreate(p_i_alloc_factorsInfoBase):
    pass

class p_i_alloc_factorsInfoUpdate(p_i_alloc_factorsInfoBase):
    pass

class p_i_alloc_factorsInfoInDBBase(p_i_alloc_factorsInfoBase):
    class Config:
        orm_mode = True

class p_i_alloc_factorsInfo(p_i_alloc_factorsInfoInDBBase):
    pass

