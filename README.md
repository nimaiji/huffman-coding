# Huffman coding
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.

write your file path and ready for huffman coding ...

## Usage
```python
import ds

huffman = ds.huffman('./input.txt')
#generate huffman tree
huffman.generateTree()

#then generate table
huffman.generateTable()
```

sample Huffman table in 'huffman.txt':
```
Character bits  code
C       4	    0010
H       5	    00101
m       3	    010
e       4	    0101
        2	    10
!       3	    101
```

## MinHeap

you also can generate min-heap tree for huffman tree but remember in huffman class min-heap tree automatically generated for huffman-tree
```python
value = 20
name = 'head'
headNode = ds.node(name,value)
minHeap = ds.minHeap(headNode,'min heap name')
#out minHeap will automatically heapify itself
minHeap.insertNode(ds.node('n1',2))
minHeap.insertNode(ds.node('n2',13))
```


