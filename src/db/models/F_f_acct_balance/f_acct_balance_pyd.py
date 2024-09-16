

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_acct_balanceInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id : int
            
        
    
        
    
        
    
        
    
        
            
                name : str
            
         
    
        
    


class f_acct_balanceInfoCreate(f_acct_balanceInfoBase):
    pass

class f_acct_balanceInfoUpdate(f_acct_balanceInfoBase):
    pass

class f_acct_balanceInfoInDBBase(f_acct_balanceInfoBase):
    class Config:
        orm_mode = True

class f_acct_balanceInfo(f_acct_balanceInfoInDBBase):
    pass

