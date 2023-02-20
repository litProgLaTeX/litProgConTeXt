
import argparse
import pprint
import yaml

from .save import saveGrammar
from .extract import extractFrom

def cli() :

  argParser  = argparse.ArgumentParser()
  subParsers = argParser.add_subparsers(dest='subCommand')

  subParser_extract = subParsers.add_parser('extract',
    help="Extract the embedded code and artifacts")
  subParser_extract.add_argument('file',
    help="The base ConTeXt file from which to extract code and artifacts")
  
  subParser_saveSyntax = subParsers.add_parser('save',
    help="Save a full LPiC tmLanguage syntax for use with VScode")
  subParser_saveSyntax.add_argument('file',
    help="The path to the new tmLanguage file")
  cliArgs = vars(argParser.parse_args())

  if cliArgs['subCommand'] == 'save' : 
    saveGrammar(cliArgs['file'])
  elif cliArgs['subCommand'] == 'extract' :
    extractFrom(cliArgs['file'])
