

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_card_authInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                card_no : str
            
         
    
        
            
                auth_response : str
            
         
    
        
             
                tran_date : date
             
        
    
        
    
        
            
                tran_type : int
            
        
    
        
            
                auth_acct_id : str
            
         
    
        
            
                tran_code : int
            
        
    
        
    
        
    
        
            
                location_code : str
            
         
    
        
            
                counterparty_name : str
            
         
    
        
    
        
            
                network_id : str
            
         
    
        
            
                pos_terminal : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class l_card_authInfoCreate(l_card_authInfoBase):
    pass

class l_card_authInfoUpdate(l_card_authInfoBase):
    pass

class l_card_authInfoInDBBase(l_card_authInfoBase):
    class Config:
        orm_mode = True

class l_card_authInfo(l_card_authInfoInDBBase):
    pass

