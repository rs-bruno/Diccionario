class WordNode:
    text = ''
    parentNode = None
    childNodes = []
    
    def __init__(self, text = '', parent = None, childs = []):
        self.text = text
        self.parentNode = parent
        self.childNodes = childs
    
    def addChild(self, otherWordNode):
        self.childNodes.append(otherWordNode)
