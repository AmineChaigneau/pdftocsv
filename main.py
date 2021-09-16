#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:04:36 2021

@author: aminechaigneau
"""


OUT_filename = "OG2020-_HBL_C69_HBLWTEAM7-------------FNL-000100--.csv"

# Import the required Module
import tabula
from os import listdir, remove, replace
from os.path import isfile, join

files = [f for f in listdir('./pdf') if isfile(join('./pdf', f))]

for IN_filename in files :
    OUT_filename = IN_filename[:-4] + '.csv'

    # convert PDF into CSV
    tabula.convert_into('./pdf/' + IN_filename, './output/' + OUT_filename, output_format="csv", pages='all')

    # delete
    # remove('./pdf/' +  IN_filename)

    # replace
    replace('./pdf/' +  IN_filename, './pdf_done/' +  IN_filename)

    print(OUT_filename)

print('All files from "./pdf" have been converted')
