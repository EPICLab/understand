#Takes an Understand database file (.udb) as the first argument

import understand
import sys

def printArchs(arch,depth=0):
  string = ("| "* depth);
  string = string + arch.name()
  print (string)
  for ent in arch.ents(True):
    string = ("| "* depth)
    print(string,"*",ent)
  for child in arch.children():
    printArchs(child,depth+1)

  
if __name__ == '__main__':
  # Open Database
  #args = sys.argv
  a="/Users/steve/Desktop/test/125ca0e3a0457f0e516ce51046054253009a82cd.und"
  db = understand.open(a)
  #***************************Code Body***********************
  for root in db.root_archs():
    printArchs(root)
    
  #***************************End Main Body ******************
    
