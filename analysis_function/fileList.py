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


repo = git.Repo('/Users/steve/Desktop/test')
shalist=repo.git.log('--pretty=%H').split('\n')


def projectMetrics(db):
    metrics = db.metric(db.metrics())
    if metrics:
        print("Project Metrics:\n")

        for key, value in metrics.items():
            print(f'\t{key}: {value}')
            
            
def fileList(db):
  for file in db.ents("File"):
    #If file is from the Ada Standard library, skip to next
    if file.library() != "Standard":
      print (file.name())


    
def create_understand_database(project_dir, und_path='/Applications/Understand.app/Contents/MacOS/Python'):
    for x in shalist:
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
            ['und', 'create', '-languages', 'python', 'java', 'add', project_dir, 'analyze', '-all', db_path],
            cwd=und_path
        )
        process.wait()
        address = str(db_path + ".und")
        #print(address)
        db = understand.open(address)
        projectMetrics(db)
    return db
    


#def revert_repo(shalist):
#    for x in shalist:
#        repo.git.reset('--hard', x)
#        print(repo.git.reset('--hard', x))
#        project_dir = "/Users/steve/Desktop/test/"
#        create_understand_database(project_dir)
#        #db = understand.open("/Users/steve/Desktop/test/tes.und")
#        #print(x)

    
if __name__ == '__main__':
  #revert_repo(shalist)
#  repo.git.reset('--hard', shalist[0])  ### revert back the repo, just incase for future use
  #project_dir = "/Users/steve/Desktop/test/"
  project_dir = "/Users/steve/Desktop/test/"
  create_understand_database(project_dir)
  #db = understand.open("/Users/steve/Desktop/test/tes.und")
  #fileList(db)
  repo.git.reset('--hard', shalist[0])


    


