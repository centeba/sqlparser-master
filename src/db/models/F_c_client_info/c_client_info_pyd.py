

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_client_infoInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                client_name: Optional[str]
            
         
    
        
            
                client_plating: Optional[str]
            
         
    
        
    


class c_client_infoInfoCreate(c_client_infoInfoBase):
    pass

class c_client_infoInfoUpdate(c_client_infoInfoBase):
    pass

class c_client_infoInfoInDBBase(c_client_infoInfoBase):
    class Config:
        orm_mode = True

class c_client_infoInfo(c_client_infoInfoInDBBase):
    pass

