import os


class Worker(object):
    def __init__(self, cfg_dict):
        self.prj_name = cfg_dict['prj_name']
        self.prj_path = cfg_dict['prj_path']
        self.partion_num = cfg_dict['partion_num']
        self.file_name = cfg_dict['file_name']
    
    # route the data into the proper partion.
    def route(self, data):
        pass
