

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_l_loan_productsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                loan_type : str
            
         
    
        
             
                can_deduct_tax : bool
             
        
    
        
    
        
            
                loan_description : str
            
         
    
        
             
                penalty_prepay : bool
             
        
    
        
            
                loan_product : str
            
         
    
        
            
                coupon_adjustment_freq : str
            
         
    
        
    
        
            
                first_coupon_change : int
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    
        
            
                risk_rating : int
            
        
    
        
            
                underwriter : str
            
         
    
        
             
                prepay_penalty : bool
             
        
    
        
    
        
            
                accrual_method : str
            
         
    
        
            
                payment_freq : str
            
         
    
        
            
                fee_type : int
            
        
    
        
    
        
            
                note_type : int
            
        
    
        
            
                index_code : int
            
        
    
        
    
        
    
        
    
        
    
        
    
        
    


class p_l_loan_productsInfoCreate(p_l_loan_productsInfoBase):
    pass

class p_l_loan_productsInfoUpdate(p_l_loan_productsInfoBase):
    pass

class p_l_loan_productsInfoInDBBase(p_l_loan_productsInfoBase):
    class Config:
        orm_mode = True

class p_l_loan_productsInfo(p_l_loan_productsInfoInDBBase):
    pass

