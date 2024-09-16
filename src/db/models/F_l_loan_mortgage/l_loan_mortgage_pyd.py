

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_loan_mortgageInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    
        
            
                has_pmi : int
            
        
    
        
            
                has_prepay_penalty : int
            
        
    
        
    
        
            
                rate_type : int
            
        
    
        
    
        
             
                last_pymt_date : date
             
        
    
        
            
                loan_type : int
            
        
    
        
    
        
             
                maturity_date : date
             
        
    
        
    
        
    
        
    
        
             
                next_monthly_pymt_date : date
             
        
    
        
             
                origination_date : date
             
        
    
        
    
        
    
        
            
                address : str
            
         
    
        
            
                balloon_loan : int
            
        
    
        
    
        
            
                home_insurance_co : str
            
         
    
        
    
        
            
                loan_purpose : int
            
        
    
        
            
                loan_doc_type : int
            
        
    
        
            
                pmi_insurance_code : int
            
        
    
        
    
        
    


class l_loan_mortgageInfoCreate(l_loan_mortgageInfoBase):
    pass

class l_loan_mortgageInfoUpdate(l_loan_mortgageInfoBase):
    pass

class l_loan_mortgageInfoInDBBase(l_loan_mortgageInfoBase):
    class Config:
        orm_mode = True

class l_loan_mortgageInfo(l_loan_mortgageInfoInDBBase):
    pass

