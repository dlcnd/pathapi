#!usr/bin/env python
#coding:utf8
import sys
import re


def project(path):
	"""
	경로를 넣으면 project 이름을 반환.
	"""
	p= re.findall('/prject/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project정보를가져 올 수 없습니다" 
	return p[0],None

def seq(path):
	"""
	경로를 넣으면seq 이름을 반환.
	"""
	p= re.findall('/shot/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를가져 올 수 없습니다" 
	return p[0],None

def shot(path):
	"""
	경로를 넣으면shot 이름을 반환.
	"""
	p= re.findall('/shot/\w/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를가져 올 수 없습니다" 
	return p[0],None

def task(path):
	"""
	경로를 넣으면task 이름을 반환.
	"""
	p= re.findall('/shot/\w/\w(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task 정보를가져 올 수 없습니다" 
	return p[0],None

def ver(path):
	"""
	경로를 넣으면version 반환.
	"""
	p= re.findall('_v(\d+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 version 정보를가져 올 수 없습니다" 
	return int(p[0]),None

def seqNum(path):
	"""
	경로를 넣으면sequence number 반환.
	"""
	p= re.findall('\.(\d+)\.',path.replace("\\","/"))
	if len(p) != -1:
		return "", "경로에서 sequence number 정보를가져 올 수 없습니다" 
	return int(p[0]),None


