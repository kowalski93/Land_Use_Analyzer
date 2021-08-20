#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import os
from numpy import log,array,unique


# In[19]:


lu=gpd.read_file(input("Path to the land use dataset: "))
grid=gpd.read_file(input("Path to the grid dataset: "))
uid_lc=input("LC UID: ")
uid_grid=input("GRID UID: ")
temp_path=input("Temp path: ")


# In[2]:


class lum:
    def __init__(self,lu,grid,uid_lc,uid_grid,temp_path):
        self.lu=lu
        self.grid=grid
        self.uid_lc=uid_lc
        self.uid_grid=uid_grid
        self.temp_path=temp_path
    
    def intermediate(self):
        intersection=gpd.overlay(self.lu,self.grid,how='intersection')
        dissolved=intersection.dissolve(by=[self.uid_lc,self.uid_grid])
    
        dissolved['poly_area']=dissolved.area
        dissolved.to_file(os.path.join(self.temp_path,"dissolved.shp"))
    
        dissolved_new=gpd.read_file(os.path.join(self.temp_path,"dissolved.shp"))
        area_sum=dissolved_new[[self.uid_grid, "poly_area"]].groupby(self.uid_grid).sum()
    
        dissolved_new = dissolved_new.merge(area_sum, on=self.uid_grid)
        dissolved_new.rename(columns = {'poly_area_y':'total_area_cell'}, inplace = True) 
    
        ratios=(dissolved_new["poly_area_x"]/dissolved_new["total_area_cell"])
        
        return dissolved_new,ratios
    
    def entropy(self):
        dataset=self.intermediate()[0]
        ratios_c=self.intermediate()[1]
        log_ratios=log(ratios_c)
        dataset['area_perc_log']=log_ratios*ratios_c
        
        num_classes_per_grid_feature = dataset[[self.uid_grid, uid_lc]].groupby(self.uid_grid).count()
        ln_num_classes_per_grid_feature = log(num_classes_per_grid_feature)
        
        sum_logs = dataset[[self.uid_grid, "area_perc_log"]].groupby(self.uid_grid).sum()
        
        sum_logs_merged_ln_num_classes = sum_logs.merge(ln_num_classes_per_grid_feature,on=self.uid_grid)
        
        sum_logs_merged_ln_num_classes['entropy']=-1*(sum_logs_merged_ln_num_classes['area_perc_log']/sum_logs_merged_ln_num_classes[self.uid_lc])
        
        grid_final_entropy = (self.grid).merge(sum_logs_merged_ln_num_classes,on=self.uid_grid)
        
        return grid_final_entropy
    
    def hhi(self):
        dataset=self.intermediate()[0]
        ratios_c=self.intermediate()[1]
        hhi=((ratios_c))**2
        
        dataset['HHI']=hhi
        
        sum_squared_ratios = dataset[[self.uid_grid, "HHI"]].groupby(self.uid_grid).sum()
        grid_final_hhi = (self.grid).merge(sum_squared_ratios,on=selfuid_grid)
        
        return grid_final_hhi





