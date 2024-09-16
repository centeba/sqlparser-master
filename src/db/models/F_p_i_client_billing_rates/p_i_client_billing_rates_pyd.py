

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_client_billing_ratesInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                rate_schedule_active : int
            
        
    
        
            
                price_group : str
            
         
    
        
            
                price_group_desc : str
            
         
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    


class p_i_client_billing_ratesInfoCreate(p_i_client_billing_ratesInfoBase):
    pass

class p_i_client_billing_ratesInfoUpdate(p_i_client_billing_ratesInfoBase):
    pass

class p_i_client_billing_ratesInfoInDBBase(p_i_client_billing_ratesInfoBase):
    class Config:
        orm_mode = True

class p_i_client_billing_ratesInfo(p_i_client_billing_ratesInfoInDBBase):
    pass

