

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class l_student_loansInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
             
                disbursement_date : date
             
        
    
        
            
                guarantor : int
            
        
    
        
            
                account_no_ext: Optional[str]
            
         
    
        
    
        
            
                is_overdue : int
            
        
    
        
             
                last_payment_date : date
             
        
    
        
    
        
            
                loan_name : str
            
         
    
        
            
                loan_status: Optional[int]
            
        
    
        
             
                end_date : date
             
        
    
        
    
        
            
                payment_ref_number : str
            
         
    
        
            
                repayment_plan : int
            
        
    
        
            
                servicer_address : str
            
         
    
        
            
                account_id: Optional[int]
            
        
    
        
    
        
    


class l_student_loansInfoCreate(l_student_loansInfoBase):
    pass

class l_student_loansInfoUpdate(l_student_loansInfoBase):
    pass

class l_student_loansInfoInDBBase(l_student_loansInfoBase):
    class Config:
        orm_mode = True

class l_student_loansInfo(l_student_loansInfoInDBBase):
    pass

