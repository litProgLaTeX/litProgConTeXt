
import argparse
import pprint
import yaml

from contextLangServer.processor.grammar import Grammar
from contextLangServer.processor.documents import DocumentCache
#from .extract import extractFrom

def cli() :

  argParser  = argparse.ArgumentParser()
  argParser.add_argument('filePath',
    help="The base ConTeXt file to load OR the tmLanguage syntax file to save")
  argParser.add_argument('--save', action="store_true",
      help="Save a full tmLanguage syntax for use with VScode")  
  cliArgs = vars(argParser.parse_args())
  #print(yaml.dump(cliArgs))
  filePath = cliArgs['filePath']

  Grammar.loadFromResourceDir('contextLangServer.context.syntax')
  Grammar.loadFromResourceDir('lpicLangServer.lpic.syntax')

  if cliArgs['save'] : 
    print(f"Saving current syntax to the tmLanguage.json file:\n  {filePath}\n")
    Grammar.saveToFile(filePath)
    return
  
  print(f"Extracting LPiC code from:\n  {filePath}\n")
  doc = DocumentCache.loadFromFile(filePath)

  print("---document keys------------------------------------------")
  print(yaml.dump(list(DocumentCache.documents.keys())))
  print("---document-----------------------------------------------")
  print(yaml.dump(doc))
  print("----------------------------------------------------------")

