

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class c_acct_wire_instructionsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                currency_code : int
            
        
    
        
            
                aba_num : str
            
         
    
        
            
                bank_routing_num : str
            
         
    
        
            
                bank_name : str
            
         
    
        
            
                bank_address : str
            
         
    
        
            
                bank_address_2 : str
            
         
    
        
            
                bank_address_3 : str
            
         
    
        
            
                bank_city_name : str
            
         
    
        
            
                bank_state_code : str
            
         
    
        
            
                bank_country_code : str
            
         
    
        
            
                cust_account_id : int
            
        
    
        
            
                cust_account_name : str
            
         
    
        
            
                fee_tag : str
            
         
    
        
            
                obi_name : str
            
         
    
        
            
                obi_account_id : int
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class c_acct_wire_instructionsInfoCreate(c_acct_wire_instructionsInfoBase):
    pass

class c_acct_wire_instructionsInfoUpdate(c_acct_wire_instructionsInfoBase):
    pass

class c_acct_wire_instructionsInfoInDBBase(c_acct_wire_instructionsInfoBase):
    class Config:
        orm_mode = True

class c_acct_wire_instructionsInfo(c_acct_wire_instructionsInfoInDBBase):
    pass

