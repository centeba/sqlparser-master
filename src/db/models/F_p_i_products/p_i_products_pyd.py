

from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional, Any

class p_i_productsInfoBase(BaseModel):

    
        
            
                system_id: Optional[int]
            
        
    
        
            
                strat_name : str
            
         
    
        
            
                strat_desc : str
            
         
    
        
            
                strat_code : str
            
         
    
        
            
                strat_type : int
            
        
    
        
            
                cusip : str
            
         
    
        
    
        
            
                res_rat : int
            
        
    
        
            
                status : int
            
        
    
        
            
                risk_cat : int
            
        
    
        
            
                benchmark_id : int
            
        
    
        
             
                benchmark_date : date
             
        
    
        
            
                fee_type : int
            
        
    
        
            
                fee_freq : int
            
        
    
        
            
                asset_classification : int
            
        
    
        
            
                mgr_name : str
            
         
    
        
    
        
    
        
            
                yield_targeted : int
            
        
    
        
            
                muni_strat : int
            
        
    
        
            
                alt_strat : int
            
        
    
        
            
                bal_strat : int
            
        
    
        
            
                sust_inv : int
            
        
    
        
            
                concentration_flag : int
            
        
    
        
            
                margin_flag : int
            
        
    
        
             
                fee_val : date
             
        
    
        
    


class p_i_productsInfoCreate(p_i_productsInfoBase):
    pass

class p_i_productsInfoUpdate(p_i_productsInfoBase):
    pass

class p_i_productsInfoInDBBase(p_i_productsInfoBase):
    class Config:
        orm_mode = True

class p_i_productsInfo(p_i_productsInfoInDBBase):
    pass

