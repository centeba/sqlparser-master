

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_restriction_catInfoBase(BaseModel):

    
        
            
                system_id : int
            
        
    
        
            
                res_cat : int
            
        
    
        
            
                res_cat_desc : str
            
         
    
        
    


class p_i_restriction_catInfoCreate(p_i_restriction_catInfoBase):
    pass

class p_i_restriction_catInfoUpdate(p_i_restriction_catInfoBase):
    pass

class p_i_restriction_catInfoInDBBase(p_i_restriction_catInfoBase):
    class Config:
        orm_mode = True

class p_i_restriction_catInfo(p_i_restriction_catInfoInDBBase):
    pass

