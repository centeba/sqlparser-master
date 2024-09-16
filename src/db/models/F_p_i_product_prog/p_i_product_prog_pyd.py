

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_product_progInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                prog_id: Optional[int]
            
        
    
        
            
                product_id: Optional[int]
            
        
    
        
            
                product_status : int
            
        
    
        
            
                asset_classification : int
            
        
    
        
             
                status_date : date
             
        
    
        
    
        
    
        
    


class p_i_product_progInfoCreate(p_i_product_progInfoBase):
    pass

class p_i_product_progInfoUpdate(p_i_product_progInfoBase):
    pass

class p_i_product_progInfoInDBBase(p_i_product_progInfoBase):
    class Config:
        orm_mode = True

class p_i_product_progInfo(p_i_product_progInfoInDBBase):
    pass

