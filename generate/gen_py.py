import os

project_name = input("Name of your project : \n")
main_dir = '.'
os.chdir(main_dir)

os.mkdir(project_name)
os.chdir(project_name)

filename = project_name+'.py'
f = open(filename, 'w')
f.write('#!/usr/bin/env python\n')
f.close()

