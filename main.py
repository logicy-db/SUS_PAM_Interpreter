from antlr4 import *
from gen.PAMLexer import PAMLexer
from gen.PAMParser import PAMParser
from antlr4.tree.Trees import Trees
import nltk

def main(filename):
    input_stream = FileStream(filename)
    lexer = PAMLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PAMParser(stream)
    tree = parser.progr()
    treeString = Trees.toStringTree(tree, None, parser)
    tree = nltk.Tree.fromstring(treeString)
    tree.draw()

if __name__ == '__main__':
    main('source/sample.txt')