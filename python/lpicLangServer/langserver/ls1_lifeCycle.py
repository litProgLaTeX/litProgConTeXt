import os
import tomllib

from contextLangServer.langserver.dispatcher import Dispatcher

##############################################################################
# Lifecycle Messages
# https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#lifeCycleMessages

##############################################################################
# Initialize
# https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#initialize
#
@Dispatcher.lsRequest('initialize', file=__file__) # all parameters in kwargs
async def initialize(disp, ctx, params, kwargs) :
  if disp.debugIO : 
    disp.debugIO.write("lsRequest: initialize\n")
  
  # load the python project description
  here = os.path.abspath(__file__) # python/contextLangServer/langserver/ls1_lifeCycle.py
  #here = os.path.dirname(here)     # python/contextLangServer/langserver
  #here = os.path.dirname(here)     # python/contextLangServer
  #here = os.path.dirname(here)     # python
  prjDict = {}
  #with open(os.path.join(here, 'pyproject.toml')) as tomlFile :
  #  prjDict = tomllib.loads(tomlFile.read())
  version = 'unknown'
  if prjDict : version = prjDict['project']['version']

  # return our capabilities
  return {
    'here' : here,
    'serverInfo' : {
      'name'    : "ConTeXtLS",
      'version' : version
    }
  }