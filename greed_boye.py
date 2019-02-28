# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:17:18 2019

@author: Uni
"""

import numpy as np
import random

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
    file = open(input)
    
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
    return slides

s = build_slides("c_memorable_moments.txt")
path = []
start = random.randrange(len(s))
path.append(start)
