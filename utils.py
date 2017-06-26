#coding=utf-8
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
    @staticmethod
    def readConfigFile(path):
        print "read configuration from file"
        if os.path.exists(path):
            cfg_file = os.path.join(path, 'config.json')
            with open(cfg_file, 'r') as f:
                return json.load(f)
    
    @staticmethod
    def appendToFile(path, line):
        print "append patient information to file"
        print "path is %s" %(path)
        if os.path.exists(path):
            data_file = os.path.join(path, 'data.csv')
            print "write to file %s" %(data_file)
            with open(data_file, 'a') as f:
                f.write(line.encode('utf8'))
                f.write('\n')
        
