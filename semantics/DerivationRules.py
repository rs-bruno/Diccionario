from . import Words

class DerivationRule:
    preDerivations = []
    postDerivations = []

class SingleFileExtensionRule(DerivationRule):
    wordsFile = None
    derivedByPrimitive = 1

    def __init__(self, wordsFile, derivedByPrimitive):
        self.wordsFile = wordsFile
        self.derivedByPrimitive = derivedByPrimitive

    def derive(self, wordSet:dict):
        wordsFile = self.wordsFile
        derivedByPrimitive = self.derivedByPrimitive
        assert wordsFile != None
        assert len(list(self.wordsFile)) % derivedByPrimitive == 0
        wordsFile.seek(0)
        parentNode = None
        counter = 0
        for word in wordsFile:
            wordText = word.strip()
            wordNode = None
            if (wordText in wordSet):
                wordNode = wordSet[wordText]
            else:
                wordNode = Words.WordNode(wordText)
                wordSet[wordText] = wordNode
            if counter == 0:
                parentNode = wordNode
            elif wordNode.parentNode == None: # This ensures that there is only one derivation for wordNode
                parentNode.addChild(wordNode)
                wordNode.parentNode = parentNode
            counter = (counter + 1) % derivedByPrimitive
                        
class DoubleFileExtensionRule(DerivationRule):
    pass

class ComprehensionRule(DerivationRule):
    pass