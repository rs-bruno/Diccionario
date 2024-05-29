from . import DerivationRules 
from . import Words
import importlib.resources

__all__ = [
    'DerivationRules',
    'Words',
]

# Paths definitions
base_words = r'palabras.txt'
sus_adj = r'sus_adj.txt'
reg_verb = r'reg_verb.txt'
irreg_verb_inf = r'irreg_verb_inf.txt'
irreg_verb_conj = r'irreg_verb_conj.txt'

resources = {
    base_words: None,
    sus_adj: None,
    reg_verb: None,
    irreg_verb_inf: None,
    irreg_verb_conj: None,
}

pkgRoot = importlib.resources.files(anchor=__name__)
txtTraversable = None
for subt in pkgRoot.iterdir():
    if (subt.name == 'txt'):
        txtTraversable = subt
        break
paths = list(resources.keys())
for text in txtTraversable.iterdir():
    if paths.count(text.name):
        resources[text.name] = text.open(encoding="UTF-8")

# Define predicates and generators for comprehension derivation rules
def predSufAble(word):
    if len(word) < 5:
        return False
    suf = word[len(word)-4:]
    if (suf == "able"):
        return True
    return False
def genSufAble(word):
    base = word[:len(word)-4]
    return [base + "abilidad"]

# Define derivation rules used to generate the final word set
rules = [
    DerivationRules.SingleFileExtensionRule(resources[sus_adj], 4),
    DerivationRules.SingleFileExtensionRule(resources[reg_verb], 53),
    DerivationRules.DoubleFileExtensionRule(resources[irreg_verb_inf], resources[irreg_verb_conj]),
    DerivationRules.ComprehensionRule(predSufAble, genSufAble),
]

words = {x: Words.WordNode(x) for x in [y.strip() for y in resources[base_words]]}

for rule in rules:
    rule.derive(words)

for path, resource in resources.items():
    resource.close()

def test():
    print(len(words))
    print(len([1 for x, v in words.items() if v.parentNode == None]))

def primitive(word):
    if (word not in words):
        return None
    node = words[word]
    if (node.parentNode == None):
        return word
    else:
        return primitive(node.parentNode.text)
