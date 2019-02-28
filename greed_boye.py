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
    
    return w

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

s = build_slides("a_example.txt")
nodes = []

counter = 0
for i in s:
    counter += 1
    i.append(counter)
    nodes.append(i)
    
print(nodes)

path = []

start = random.randrange(len(s))
path.append(nodes[start][3])
del(nodes[start])

sum_weights = 0
sample_size = 100

while(True):
    weights = []
    
    if(len(nodes) > 2*sample_size):
        l = random.sample(nodes, sample_size)
    
    for i in range(len(l)):
        w = weight(s[start][1], l[i][1])
        weights.append([w, l[i][3]])
        
    if len(weights) is 0:
        break
    
    largest = -1
    largest_index = 0
    for i in range(len(weights)):
        if weights[i][0] > largest:
            largest = weights[i][0]
            largest_index = weights[i][1]
    
    start = largest_index
    path.append(nodes[start][3])
    del(nodes[start])
    sum_weights += largest
    print(len(nodes))
    
print(path)
print(sum_weights)