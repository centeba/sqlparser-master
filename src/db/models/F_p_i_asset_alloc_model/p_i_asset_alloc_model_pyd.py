

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_asset_alloc_modelInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                asset_alloc_type: Optional[int]
            
        
    
        
            
                asset_class: Optional[int]
            
        
    
        
            
                asset_class_strat : int
            
        
    
        
    
        
            
                model_status : int
            
        
    
        
             
                active_date : date
             
        
    
        
            
                model_type : int
            
        
    
        
            
                prog_id : int
            
        
    
        
    
        
    


class p_i_asset_alloc_modelInfoCreate(p_i_asset_alloc_modelInfoBase):
    pass

class p_i_asset_alloc_modelInfoUpdate(p_i_asset_alloc_modelInfoBase):
    pass

class p_i_asset_alloc_modelInfoInDBBase(p_i_asset_alloc_modelInfoBase):
    class Config:
        orm_mode = True

class p_i_asset_alloc_modelInfo(p_i_asset_alloc_modelInfoInDBBase):
    pass

