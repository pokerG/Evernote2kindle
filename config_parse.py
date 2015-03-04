#coding:utf-8
import json

def ParseConfig():

	f = file("config.json") 
	config = json.load(f)
	f.close
	return config

if __name__ == '__main__':
	ParseConfig()
	print config	