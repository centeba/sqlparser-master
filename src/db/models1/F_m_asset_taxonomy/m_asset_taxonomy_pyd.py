

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class m_asset_taxonomyInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                level_1 : str
            
         
    
        
            
                level_2 : str
            
         
    
        
            
                level_3 : str
            
         
    
        
            
                descr : str
            
         
    
        
    


class m_asset_taxonomyInfoCreate(m_asset_taxonomyInfoBase):
    pass

class m_asset_taxonomyInfoUpdate(m_asset_taxonomyInfoBase):
    pass

class m_asset_taxonomyInfoInDBBase(m_asset_taxonomyInfoBase):
    class Config:
        orm_mode = True

class m_asset_taxonomyInfo(m_asset_taxonomyInfoInDBBase):
    pass

