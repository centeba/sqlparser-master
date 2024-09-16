

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class custodian_sc_pos_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_name : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_type : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class custodian_sc_pos_extInfoCreate(custodian_sc_pos_extInfoBase):
    pass

class custodian_sc_pos_extInfoUpdate(custodian_sc_pos_extInfoBase):
    pass

class custodian_sc_pos_extInfoInDBBase(custodian_sc_pos_extInfoBase):
    class Config:
        orm_mode = True

class custodian_sc_pos_extInfo(custodian_sc_pos_extInfoInDBBase):
    pass

