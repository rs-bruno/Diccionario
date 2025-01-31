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
        assert len(list(wordsFile)) % derivedByPrimitive == 0
        wordsFile.seek(0)
        parentNode = None
        counter = 0
        for word in wordsFile:
            wordText = word.strip()
            wordNode = None
            if wordText in wordSet:
                wordNode = wordSet[wordText]
            else:
                wordNode = Words.WordNode(wordText)
                wordSet[wordText] = wordNode
            if counter == 0:
                parentNode = wordNode
            else:
                parentNode.addChild(wordNode)
                if wordNode.parentNode == None: # This ensures that there is only one derivation for wordNode
                    wordNode.parentNode = parentNode
            counter = (counter + 1) % derivedByPrimitive
                        
class DoubleFileExtensionRule(DerivationRule):
    primitiveFile = None
    derivedFile = None

    def __init__(self, primitiveFile, derivedFile):
        self.primitiveFile = primitiveFile
        self.derivedFile = derivedFile
    
    def derive(self, wordSet:dict):
        primitiveFile = self.primitiveFile
        derivedFile = self.derivedFile
        assert primitiveFile != None
        assert derivedFile != None
        pfLen = len(list(primitiveFile))
        dfLen = list(derivedFile).count('\n')
        assert pfLen - 1 <= dfLen # Last primitive word doesn't need to separate its derived words with a blank line
        primitiveFile.seek(0)
        derivedFile.seek(0)
        for primitive in primitiveFile:
            primitiveText = primitive.strip()
            primitiveNode = None
            if primitiveText in wordSet:
                primitiveNode = wordSet[primitiveText]
            else:
                primitiveNode = Words.WordNode(primitiveText)
                wordSet[primitiveText] = primitiveNode
            while True:
                derivedText = derivedFile.readline().strip()
                if derivedText == "":
                    break
                derivedNode = None
                if derivedText in wordSet:
                    derivedNode = wordSet[derivedText]
                else:
                    derivedNode = Words.WordNode(derivedText)
                    wordSet[derivedText] = derivedNode
                primitiveNode.addChild(derivedNode)
                if derivedNode.parentNode == None: # Ensure that it doesn't already exist a derivation for derivedText
                    derivedNode.parentNode = primitiveNode

class ComprehensionRule(DerivationRule):
    predicate = None
    generator = None
        
    def __init__(self, predicate, generator):
        self.predicate = predicate
        self.generator = generator

    def derive(self, wordSet:dict):
        primitiveWords = {k: v for k, v in wordSet.items() if self.predicate(k)}
        for pWord, pNode in primitiveWords.items():
            derivedWords = self.generator(pWord)
            for dWord in derivedWords:
                dNode = None
                if dWord in wordSet:
                    dNode = wordSet[dWord]
                else:
                    dNode = Words.WordNode(dWord)
                    wordSet[dWord] = dNode
                pNode.addChild(dNode)
                if dNode.parentNode == None: # Ensure that it doesn't already exist a derivation for derivedText
                    dNode.parentNode = pNode
