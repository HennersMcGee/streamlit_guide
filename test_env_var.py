# -*- coding: utf-8 -*-
'''
    File name: test_env_var.py
    Author: Henry Letton
    Date created: 2020-10-28
    Python Version: 3.8.3
    Desciption: Testing enviroment variables on Heroku.
        This is may be required for holding database login credentials
'''

import os

def env_var_exist(var):
    
    value = os.environ.get(var)
    
    if value:
        print("Does exist")
        print(f"The variable {var} has a value: {value}")
    else:
        print("Doesn't exist")


#%% Testing
"""
print(os.environ)

os.environ.get('no_exist')

os.environ['test_var1'] = 'one'

os.environ.get('test_var1')

if os.environ.get('test_var1'):
    print("Does exist")
else:
    print("Doesn't exist")


os.environ.pop('test_var1')

env_var_exist('no_exist')
env_var_exist('test_var1')
"""