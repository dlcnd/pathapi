#!usr/bin/env python
#coding:utf
import sys
import re

path = "/project/circle/shot/FOO/0010/comp/FOO_0010_comp_v001.nk"

def project(path):
	"""
	경로를 넣으면 project 이름을 반환.
	"""
	p= re.findall('/prject/(\S[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project정보를가져 올 수 없습니다" 
	return p[0],None

def shot(path):
	"""
	경로를 넣으면shot 이름을 반환.
	"""
	p= re.findall('/shot/(\S[^/]+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를가져 올 수 없습니다" 
	return p[0],None

if __name__ == "__main__":
	projectName, err = project(path)
	if err:
		print err
	print projectName
	
	shotName, err = project(path)
	if err:
		print err
	print shotName

