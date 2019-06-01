import ds

head = ds.node('head',0)
tree = ds.tree(head,'min_heap')

min = ds.minHeap(head)
print(min.name)