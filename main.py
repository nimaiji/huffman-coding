import ds

#file input
# quantity = {}

#insert EOF
# quantity['EOF'] = 0

#reading file
# file = open('./input.txt','r')
# for line in file:
#     for index,char in enumerate(line):
#         #print(index,char)
#         if (char in quantity):
#             quantity.update({char:quantity[char]+1})
#         else:
#             quantity[char] = 1
#
#
#
# print(len(quantity))

#using min heap
# item = quantity.popitem()
# head = ds.node(item[0],item[1])
# minHeap = ds.minHeap(head)
# for n in quantity:
#     minHeap.insertNode(ds.node(n,quantity[n]))

# for x in minHeap.nodes:
#     print(x)

huffman = ds.huffman('./input.txt')
huffman.generateTree()
huffman.generateTable()
print(huffman.frequency)


# head = ds.node('head',20)
# n1 = ds.node('n1',17)
# n2 = ds.node('n2',5)
# n3 = ds.node('n3',10)
# n4 = ds.node('n4',4)
# n5 = ds.node('n3',12)
#
# minHeap = ds.minHeap(head)
# minHeap.insertNode(n1)
# minHeap.insertNode(n2)
# minHeap.insertNode(n3)
# minHeap.insertNode(n4)
# minHeap.insertNode(n5)
# for x in minHeap.nodes:
#     print(x.value)