

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_student_loan_statusInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                loan_status : str
            
         
    
        
            
                loan_status_desc : str
            
         
    
        
    


class m_student_loan_statusInfoCreate(m_student_loan_statusInfoBase):
    pass

class m_student_loan_statusInfoUpdate(m_student_loan_statusInfoBase):
    pass

class m_student_loan_statusInfoInDBBase(m_student_loan_statusInfoBase):
    class Config:
        orm_mode = True

class m_student_loan_statusInfo(m_student_loan_statusInfoInDBBase):
    pass

