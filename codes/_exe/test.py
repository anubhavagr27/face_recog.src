# -*- coding: utf-8 -*-
import os, glob
import random

all_folder= "extYaleB/" # DataSet directory
model= "extYaleB.SRC" # SRCModel
n_train= 30 # Each person's training image number (randomly selected)
train_list= "extYaleB.train_list" # Training image list to ensure that each person's training image appears continuously
test_list= "extYaleB.test_list" # Test image List
sci_t= 0 # SCI Thresholds, specific explanations see Pami-face.pdf file

w= 10 # SRC Use facial image width (bilinear interpolation)
h= 12 # SRC Use face image height

train_cmdline= "train.exe %s %d %d %d %s" % (train_list, n_train, w, h, model) # Training Command Line
test_cmdline= "test.exe %s %s %f" % (model, test_list, sci_t) # Test command line

def UnrepeatedIntRandom(lower, upper, count):
	"""Uniformly distributed COUNT integer randoms
	[LOWER, UPPER]
	COUNT must be <= (UPPER-LOWER+1)
	"""
	
	n= upper-lower+1
	if count>n:
		print "[error : UnrepeatedIntRandom], COUNT must be <= (UPPER-LOWER+1)."
		exit(-1)
	x= range(lower, upper+1)
	urdm= []
	for i in range(0, count):
		t= random.randint(i, n-1)
		tmp= x[i]
		x[i]= x[t]
		x[t]= tmp
		urdm.append(x[i])
	return urdm

def Filename2Id(path):
	idx= path.find("yaleB")
	return path[idx:idx+7]

def SplitTrainTest():
	train_f= open(train_list, "w")
	test_f= open(test_list, "w")
	prev_id= ""
	subject_samples= []
	for path in glob.glob(all_folder+"*.pgm"):
		id= Filename2Id(path)
		print id
		if prev_id==id:
			subject_samples.append(path)
		elif prev_id!="":
			train_samples= UnrepeatedIntRandom(0, len(subject_samples)-1, n_train)
			for i in range(0, len(subject_samples)):
				if i in train_samples:
					train_f.write(subject_samples[i])
					train_f.write("\n")
				else:
					test_f.write(subject_samples[i])
					test_f.write("\n")
			prev_id= id
			subject_samples= []
			subject_samples.append(path)
		else:
			prev_id= id
			subject_samples.append(path)
	train_samples= UnrepeatedIntRandom(0, len(subject_samples)-1, n_train)
	for i in range(0, len(subject_samples)):
		if i in train_samples:
			train_f.write(subject_samples[i])
			train_f.write("\n")
		else:
			test_f.write(subject_samples[i])
			test_f.write("\n")
	train_f.close()
	test_f.close()
	
def Train():
	os.system(train_cmdline)
	
def Test():
	os.system(test_cmdline)

if __name__=='__main__':
	SplitTrainTest()
	Train()
	Test()
