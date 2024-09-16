

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class f_transaction_infoInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
             
                date_transaction: Optional[date]
            
        
    
        
             
                date_effective: Optional[date]
            
        
    
        
             
                date_trade: Optional[date]
            
        
    
        
             
                date_settle: Optional[date]
            
        
    
        
            
                security_id: Optional[int]
            
        
    
        
            
                buy_or_sell: Optional[int]
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                tran_exchange: Optional[int]
            
        
    
        
            
                tran_broker: Optional[int]
            
        
    
        
            
                tran_reinvest_code: Optional[int]
            
        
    
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class f_transaction_infoInfoCreate(f_transaction_infoInfoBase):
    pass

class f_transaction_infoInfoUpdate(f_transaction_infoInfoBase):
    pass

class f_transaction_infoInfoInDBBase(f_transaction_infoInfoBase):
    class Config:
        orm_mode = True

class f_transaction_infoInfo(f_transaction_infoInfoInDBBase):
    pass

