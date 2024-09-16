

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_loanInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
            
                loan_type : str
            
         
    
        
             
                loan_start_date : date
             
        
    
        
             
                loan_end_date : date
             
        
    
        
    
        
            
                can_deduct_tax : int
            
        
    
        
    
        
    
        
             
                funding_date : date
             
        
    
        
    
        
    
        
            
                loan_description : str
            
         
    
        
            
                loannet_id : str
            
         
    
        
            
                loannet_product_code : str
            
         
    
        
    
        
            
                penalty_prepay : int
            
        
    
        
            
                loan_product : str
            
         
    
        
            
                coupon_adjustment_freq : str
            
         
    
        
    
        
             
                first_coupon_date_change : date
             
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
             
                late_charge_date : date
             
        
    
        
             
                last_maturity_date : date
             
        
    
        
    
        
            
                risk_rating : int
            
        
    
        
            
                underwriter : str
            
         
    
        
             
                last_payment_date : date
             
        
    
        
            
                prepay_penalty : int
            
        
    
        
    
        
            
                accrual_method : str
            
         
    
        
            
                payment_freq : str
            
         
    
        
             
                first_payment_date : date
             
        
    
        
            
                fee_type : int
            
        
    
        
    
        
            
                payment_status : int
            
        
    
        
            
                note_type : int
            
        
    
        
            
                index_code : int
            
        
    
        
    
        
    


class l_loanInfoCreate(l_loanInfoBase):
    pass

class l_loanInfoUpdate(l_loanInfoBase):
    pass

class l_loanInfoInDBBase(l_loanInfoBase):
    class Config:
        orm_mode = True

class l_loanInfo(l_loanInfoInDBBase):
    pass

