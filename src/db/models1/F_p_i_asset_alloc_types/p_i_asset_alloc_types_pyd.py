

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_asset_alloc_typesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                aa_type : int
            
        
    
        
            
                aa_type_desc : str
            
         
    
        
    


class p_i_asset_alloc_typesInfoCreate(p_i_asset_alloc_typesInfoBase):
    pass

class p_i_asset_alloc_typesInfoUpdate(p_i_asset_alloc_typesInfoBase):
    pass

class p_i_asset_alloc_typesInfoInDBBase(p_i_asset_alloc_typesInfoBase):
    class Config:
        orm_mode = True

class p_i_asset_alloc_typesInfo(p_i_asset_alloc_typesInfoInDBBase):
    pass

