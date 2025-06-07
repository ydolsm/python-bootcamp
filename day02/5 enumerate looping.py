items = ['a','b','c']

#enumerate function - similar with zip except that it's just numbers
for index, item in enumerate (items):
    print (index, item)

#if you want to start from index 1
for index, item in enumerate (items, start=1):
    print (index, item)
