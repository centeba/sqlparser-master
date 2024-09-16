

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class custodian_wf_accounts_extInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                attr_acct : str
            
         
    
        
            
                attr_data : str
            
         
    
        
            
                attr_data_types : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class custodian_wf_accounts_extInfoCreate(custodian_wf_accounts_extInfoBase):
    pass

class custodian_wf_accounts_extInfoUpdate(custodian_wf_accounts_extInfoBase):
    pass

class custodian_wf_accounts_extInfoInDBBase(custodian_wf_accounts_extInfoBase):
    class Config:
        orm_mode = True

class custodian_wf_accounts_extInfo(custodian_wf_accounts_extInfoInDBBase):
    pass

