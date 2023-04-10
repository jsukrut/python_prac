dictio = { 'Epsilon':5, 'alpha':1, 'Gamma':3, 'beta':2, 'delta':4 }
sortedDict = dict( sorted(dictio.items(), key=lambda x: x[0]) )
print(sortedDict)
