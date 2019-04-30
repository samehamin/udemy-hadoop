#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 03:19:58 2019

@author: samehamin
"""

from starbase import Connection

c = Connection("127.0.0.1", "8001")

ratings = c.table('ratings')

if (ratings.exists()):
    print("Dropping existing ratings table \n")
    # ratings.drop()

ratings.create('rating')
