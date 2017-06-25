import os
import random

class Worker(object):
    def __init__(self, cfg_dict):
        self.prj_name = cfg_dict['prj_name']
        self.prj_path = cfg_dict['prj_path']
        self.partion_num = int(cfg_dict['partion_num'])
    
    # route the data into the proper partion.
    def route(self, data):
        pass
