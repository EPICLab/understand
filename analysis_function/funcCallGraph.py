#Save Call Graphs of Function in Working Directory

import understand
import sys

def drawCallGraphs(db):
  func = db.ents("function,method,procedure")[0]
  file = "callsPY_" + func.name() + ".png"
  print (func.longname(),"->",file)
  try:
    func.draw("Calls",file)
  except understand.UnderstandError as err:
    print("Error: {0}".format(err))
  

if __name__ == '__main__':
  # Open Database
  args = sys.argv
  db = understand.open(args[1])
  drawCallGraphs(db)     