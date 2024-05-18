from . import DerivationRules 
from . import Words
import importlib.resources
from importlib.resources import as_file

__all__ = ['DerivationRules', 'Words']

# Paths definitions
base_words = r'palabras.txt'
sus_adj = r'sus_adj.txt'

resources = {
    base_words: None,
    sus_adj: None,
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

# Define derivation rules used to instantiate
rules = [
    DerivationRules.SingleFileExtensionRule(resources[sus_adj], 4),
]

wordsList = [x.strip() for x in resources[base_words]]
words = {x:Words.WordNode(x) for x in wordsList}
wordsList.clear()

print(len(words))

for rule in rules:
    rule.derive(words)

for r in resources:
    resources[r].close()

def test():
    print(len(words))
    print(len([x for x in words.keys() if words[x].parentNode == None]))