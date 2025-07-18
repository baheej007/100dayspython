superset=[1,2,3]
subset = [[]]
for i in superset:

    subset += [x + [i] for x in subset]
    print(subset)
print(subset)