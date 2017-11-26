from __future__ import print_function

import re
import sys

from antlr4 import *
from pcbLexer import pcbLexer
from pcbParser import pcbParser

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def print(self):
        print("(", self.name, " ", end="")
        [child.print() for child in self.children]
        print(" )")

    def getPosition(self):
        for child in self.children:
            if isinstance(child, Node) and child.name == 'at':
                return [float(x.content) for x in child.children]
        return None

    def getPositionNode(self):
        for child in self.children:
            if isinstance(child, Node) and child.name == 'at':
                return child
        return None

    def getReference(self):
        for child in self.children:
            if isinstance(child, Node) \
                    and child.name == 'fp_text' \
                    and child.children[0].content == 'reference':
                return child.children[1].content
        return None


    def getReferencePosition(self):
        for child in self.children:
            if isinstance(child, Node) \
                    and child.name == 'fp_text' \
                    and child.children[0].content == 'reference':
                return child.getPosition()
        return None


    def getReferencePositionNode(self):
        for child in self.children:
            if isinstance(child, Node) \
                    and child.name == 'fp_text' \
                    and child.children[0].content == 'reference':
                return child.getPositionNode()
        return None

    # Find the module whose fp_text reference is the given one.
    def findModule_(self, reference):
        if self.name != 'module':
            for child in self.children:
                if isinstance(child, Node):
                    result = child.findModule_(reference)
                    if result != None:
                        return result
            return None
        for child in self.children:
            if isinstance(child, Node) \
                    and child.name == 'fp_text' \
                    and child.children[0].content == 'reference' \
                    and child.children[1].content == reference:
                return self
        return None


    def findModule(self, reference):
        print("Looking for reference", reference)
        found = self.findModule_(reference)
        if found == None:
            print("Did not find reference", reference)
        return found


    def findModuleType_(self, typeRegex):
        if self.name != 'module':
            for child in self.children:
                if isinstance(child, Node):
                    for found in child.findModuleType_(typeRegex):
                        yield found
        else:
            for child in self.children:
                if isinstance(child, Node) and child.name == 'fp_text' \
                        and child.children[0].content == 'reference' \
                        and re.match(typeRegex, child.children[1].content):
                    yield self


    def findModuleType(self, prefix):
        pattern = re.compile(prefix + "[0-9]+")
        for found in self.findModuleType_(pattern):
            yield found


    def setReferencePosition(self, pos):
        self.getReferencePositionNode().children = [Word(str(x)) for x in pos]


    def setPosition(self, pos):
        self.getPositionNode().children = [Word(str(x)) for x in pos]


    def toFile(self, file):
        file.write(" (")
        file.write(self.name)
        [c.toFile(file) for c in self.children]
        file.write(")\n")



class Word(object):
    def __init__(self, content):
        self.content = content

    def print(self):
        print(self.content, " ", end="")

    def toFile(self, file):
        file.write(" ")
        file.write(self.content)


def handleContent(content):
    if content.WORD() != None:
        return Word(content.WORD().getText())
    if content.STRING() != None:
        return Word(content.STRING().getText())
    return handleNode(content.node())


def handleNode(node):
    children = list(node.getChildren())
    n = Node(node.WORD().getText())
    children = node.content()
    n.children = [handleContent(child) for child in children]
    return n


def reposition(root, prefix, prototypePos, prototypeRefPos):
    numPrototypes = len(prototypePos)
    for d in root.findModuleType(prefix):
        ref = d.getReference()
        num = int(ref[1:])
        if (num <= numPrototypes):
            continue
        pos = d.getPosition()
        section = (num - 1) / numPrototypes
        alias = (num - 1) % numPrototypes
        yoffset = section * 20
        pos = list(prototypePos[alias])
        pos[1] += yoffset
        print(ref, '->', pos[1])
        d.setPosition(pos)
        d.setReferencePosition(prototypeRefPos[alias])
        print("     ", d.getPosition())
        print("     ", d.getReferencePosition())

def main(argv):
    input = FileStream(argv[1])
    lexer = pcbLexer(input)
    stream = CommonTokenStream(lexer)
    parser = pcbParser(stream)
    print("Parsing")
    tree = parser.node()

    print("Noding")
    root = handleNode(tree)

    print("Finding")
    D = [root.findModule('D' + str(n)) for n in [1, 2]]
    Q = [root.findModule('Q' + str(n)) for n in [1, 2, 3, 4, 5]]
    R = [root.findModule('R' + str(n)) for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    C = [root.findModule('C' + str(n)) for n in [1, 2]]
    Dpos = [n.getPosition() for n in D]
    Qpos = [n.getPosition() for n in Q]
    Rpos = [n.getPosition() for n in R]
    Cpos = [n.getPosition() for n in C]
    Drefpos = [n.getReferencePosition() for n in D]
    Qrefpos = [n.getReferencePosition() for n in Q]
    Rrefpos = [n.getReferencePosition() for n in R]
    Crefpos = [n.getReferencePosition() for n in C]

    reposition(root, 'D', Dpos, Drefpos)
    reposition(root, 'Q', Qpos, Qrefpos)
    reposition(root, 'R', Rpos, Rrefpos)
    reposition(root, 'C', Cpos, Crefpos)

    with open(argv[1] + "2", "w") as file:
        root.toFile(file)


if __name__ == '__main__':
    main(sys.argv)
