

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class org_pos_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_name : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_type : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class org_pos_extInfoCreate(org_pos_extInfoBase):
    pass

class org_pos_extInfoUpdate(org_pos_extInfoBase):
    pass

class org_pos_extInfoInDBBase(org_pos_extInfoBase):
    class Config:
        orm_mode = True

class org_pos_extInfo(org_pos_extInfoInDBBase):
    pass

