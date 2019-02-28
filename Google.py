#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:23:01 2019

@author: elisa
"""

import numpy as np

def weight(tags1, tags2):
    counter = 0
    for i in tags1:
        if i in tags2:
            counter += 1
    
    w = min([counter, len(tags1)-counter, len(tags2)-counter])
    if(w is not 0):
        m = 1./w * 10000
    else:
        m = 9999999999
    
    return int(m)

def build_slides(input):
    file = open("c_memorable_moments.txt")
    
    # slides[0] = number of tags
    # slides[1] = tags
    # slides[2] = number of images
    # slides[3] = image ids
    
    slides = []
    v_images = []
    
    counter = 0
    for line in file:
        if(counter is 0):
            counter += 1
            continue
        line = line.strip()
        attributes = line.split(None, 2)
        attributes.append(1)
        attributes.append([counter])
        counter += 1
        attributes[1] = int(attributes[1])
        attributes[2] = attributes[2].split()
        if(attributes[0] is "H"):
            del(attributes[0])
            slides.append(attributes)
        else:
            del(attributes[0])
            v_images.append(attributes)
            
    for i in range(0, len(v_images), 2):
        tags = []
        for j in v_images[i][1]:
            tags.append(j)
        for j in v_images[i+1][1]:
            if j not in tags:
                tags.append(j)
                
        slides.append([len(tags), tags, 2, [i, i+1]])


def pair_V():
  file = open("c_memorable_moments.txt")   
  
  slides = []
  v_images = []
  
  counter = 0
  for line in file:
        if(counter is 0):
            counter += 1
            continue
        line = line.strip()
        attributes = line.split(None, 2)
        attributes.append(1)
        attributes.append([counter])
        counter += 1
        attributes[1] = int(attributes[1])
        attributes[2] = attributes[2].split()
        if(attributes[0] is "H"):
            del(attributes[0])
            slides.append(attributes)
        else:
            del(attributes[0])
            v_images.append(attributes)
  values = []
  for i in range (len(v_images)):
     c = [a for a, b in zip(v_images[0][1],v_images[i][1]) if a==b]
     values.append(len(c))
  index = np.argmin(values)
  print(index) 
  del v_images[0]
  del v_images[index - 1]
  couple = [v_images[0],v_images[index]]
  print(len(v_images))
  return v_images, couple


couples = []

#for i in range ():
v_images, couple = pair_V()
  #couples.append(couple)




#c = [1,2,3,4]
#c = np.asarray(c)
#d = [4,5,6,7]
#d = np.asarray(d)

#print(c & d)
