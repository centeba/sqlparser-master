

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_l_loan_eligibilityInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                reason_code : str
            
         
    
        
            
                reason_desc : str
            
         
    
        
    


class p_l_loan_eligibilityInfoCreate(p_l_loan_eligibilityInfoBase):
    pass

class p_l_loan_eligibilityInfoUpdate(p_l_loan_eligibilityInfoBase):
    pass

class p_l_loan_eligibilityInfoInDBBase(p_l_loan_eligibilityInfoBase):
    class Config:
        orm_mode = True

class p_l_loan_eligibilityInfo(p_l_loan_eligibilityInfoInDBBase):
    pass

