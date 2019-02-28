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
    file = open("a_example.txt")
    
    # slides[0] = number of tags
    # slides[1] = tags
    # slides[2] = number of images
    # slides[3] = image ids
    
    h_images = []
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
            h_images.append(attributes)
        else:
            del(attributes[0])
            v_images.append(attributes)
                
    return (v_images, h_images)
                 
def coupling_V (v_images): 
  values = []          
  for i in range (len(v_images)):
     c = [a for a, b in zip(v_images[0][1],v_images[i][1]) if a==b]
     values.append(len(c))
  index = np.argmin(values)
  del v_images[0]
  del v_images[index-1]
  couple = [v_images[0],v_images[index]]
  return v_images, couple


couples = []
v_images, h_images = build_slides(input)
while len(v_images) > 3:
  v_images, couple = coupling_V(v_images)
  couples.append(couple)
couple = [v_images[0],v_images[1]]
couples.append(couple)

