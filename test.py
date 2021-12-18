#Print a list of the files in the project

import understand
import sys
import pandas as pd
import numpy
import datetime
import re
import matplotlib
import statistics
import json
import collections
from json import JSONDecodeError
import requests
from urllib.error import HTTPError
import time
import os
from datetime import datetime
from github import Github
import git
import understand
import sys
import os
import understand as und
import subprocess


repo = git.Repo('/Users/steve/Desktop/test') ## this is for repo analysis, if you run your code locally, please comment line 28 and 29.
shalist=repo.git.log('--pretty=%H').split('\n')


def projectMetrics(db):
#This function means to export the metrics, please check the manuel to see the kinds of metrics.
    metrics = db.metric(db.metrics())
    if metrics:
        print("Project Metrics:\n")

        for key, value in metrics.items():
            print(f'\t{key}: {value}')
            
            
def fileList(db):
#This function means to export the file list, please check the manuel to see the kinds of metrics.
  for file in db.ents("File"):
    #If file is from the Ada Standard library, skip to next
    if file.library() != "Standard":
      print (file.name())


    
def create_understand_database(project_dir, und_path='/Applications/Understand.app/Contents/MacOS/Python'): #if you are using MAC, you do not need to change path, but if you are using windows, please check the understand website for path
    for x in shalist:  # if you run your code locally, please comment this loop
        repo.git.reset('--hard', x)
        print(repo.git.reset('--hard', x))
        assert os.path.isdir(project_dir)
        assert os.path.isdir(und_path)
        db_name = x
        db_path = os.path.join(project_dir, db_name)
        assert os.path.exists(db_path) is False
    # An example of command-line is:
    # und create -languages c++ java add /Users/steve/Desktop/test analyze -all myDb.udb
    
        process = subprocess.Popen(
            ['und', 'create', '-languages', 'python', 'java', 'add', project_dir, 'analyze', '-all', db_path], #kindly change language as you need
            cwd=und_path
        )
        process.wait()
        address = str(db_path + ".und")
        #print(address)
        db = understand.open(address)
        projectMetrics(db) #call your analysis function
    return db
    

    
if __name__ == '__main__':
  project_dir = "/Users/steve/Desktop/test/"
  create_understand_database(project_dir)
