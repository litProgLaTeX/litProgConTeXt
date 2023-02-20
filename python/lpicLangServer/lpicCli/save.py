

from contextLangServer.processor.grammar import Grammar

def saveGrammar(filePath) :
  gram = Grammar()
  gram.loadFromResourceDir('contextLangServer.context.syntax')
  gram.loadFromResourceDir('lpicLangServer.lpic.syntax')

  gram.saveToFile(filePath)