# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:38:56 2021

@author: Shukla
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Shukla\Documents/ds_salary_proj/chromedriver"
df = gs.get_jobs('data scientist',15, False, path,15)
df