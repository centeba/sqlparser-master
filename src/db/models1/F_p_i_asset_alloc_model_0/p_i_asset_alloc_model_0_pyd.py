

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_asset_alloc_model_0InfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                asset_alloc_type: Optional[int]
            
        
    
        
            
                asset_class: Optional[int]
            
        
    
        
            
                asset_class_strat : int
            
        
    
        
    
        
            
                model_status : int
            
        
    
        
             
                active_date : date
             
        
    
        
            
                model_type : int
            
        
    
        
            
                prog_id : int
            
        
    
        
            
                fa : str
            
         
    
        
            
                client : str
            
         
    
        
            
                account_id : int
            
        
    
        
    
        
    


class p_i_asset_alloc_model_0InfoCreate(p_i_asset_alloc_model_0InfoBase):
    pass

class p_i_asset_alloc_model_0InfoUpdate(p_i_asset_alloc_model_0InfoBase):
    pass

class p_i_asset_alloc_model_0InfoInDBBase(p_i_asset_alloc_model_0InfoBase):
    class Config:
        orm_mode = True

class p_i_asset_alloc_model_0Info(p_i_asset_alloc_model_0InfoInDBBase):
    pass

