import os
import json


class Utils(object):
    def __init__(self):
        pass
    
    @staticmethod
    def saveConfigFile(data, path):
        print "save config file"
        if os.path.exists(path):
            cfg_file = os.path.join(path, "config.json")
            print "config file is %s" %(cfg_file)
            with open(cfg_file, 'w') as outfile:
                json.dump(data, outfile)
        
