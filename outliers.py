# -*- coding: utf-8 -*-
"""
Write a python code to remove outliers

@author: Dell
"""
values=[89,105,7,4,12,23]
retval=sorted(values)
def removeOutliers(data,num_outliers):
    retval=sorted(data)
    for i in range(num_outliers):
        retval.pop(-1)
    return retval
removeOutliers(values,2)
    
