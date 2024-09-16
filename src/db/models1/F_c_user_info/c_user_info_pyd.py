

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_user_infoInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                first_name: Optional[str]
            
         
    
        
            
                last_name: Optional[str]
            
         
    
        
            
                mobile_number : str
            
         
    
        
            
                mobile_country_code : int
            
        
    
        
    


class c_user_infoInfoCreate(c_user_infoInfoBase):
    pass

class c_user_infoInfoUpdate(c_user_infoInfoBase):
    pass

class c_user_infoInfoInDBBase(c_user_infoInfoBase):
    class Config:
        orm_mode = True

class c_user_infoInfo(c_user_infoInfoInDBBase):
    pass

