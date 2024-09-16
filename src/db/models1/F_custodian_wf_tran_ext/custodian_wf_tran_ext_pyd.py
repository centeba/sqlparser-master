

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class custodian_wf_tran_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_name : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_type : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class custodian_wf_tran_extInfoCreate(custodian_wf_tran_extInfoBase):
    pass

class custodian_wf_tran_extInfoUpdate(custodian_wf_tran_extInfoBase):
    pass

class custodian_wf_tran_extInfoInDBBase(custodian_wf_tran_extInfoBase):
    class Config:
        orm_mode = True

class custodian_wf_tran_extInfo(custodian_wf_tran_extInfoInDBBase):
    pass

