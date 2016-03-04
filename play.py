#!/usr/bin/python
import sys
import os
import inspect as i
import argparse
import re
import importlib

sys.path.insert(1, os.path.abspath(os.path.pardir+'/src'))

def main(file):
    module = i.getmodulename(file)
    print module
    mod = re.sub(r"\/",'.',file)
    mod = re.sub(r'.py','',mod)
    test = importlib.import_module(mod)
    dict1 = i.getmembers(test)
    # print dict1
    for name in dict1:
	key, val = list(name)
	# print key
	if 'test_' in key:
	    print key
    moddoc = i.getdoc(test)
    print "Module Document String:\n", moddoc

    #print dict1.pytestmark
    

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="Playground Python Module")
    PARSER.add_argument('filename', nargs="+", help="File Name of file")
    PARSER.add_argument('--debug', action='store_true', help='Changes log level to debug')
    ARGS = PARSER.parse_args()
    FILE_NAME = ARGS.filename

    for name in FILE_NAME:
	main(name)

