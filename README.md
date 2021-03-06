# Huffman coding
📎In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression.

Write your file path and ready for encoding ...

## 📖Usage
```python
import ds

huffman = ds.huffman('./input.txt')

#generate huffman tree
#this function automatically generate frequency and min heap for generating huffman tree
huffman.generateTree()

#then generate table
huffman.generateTable()

#export zipped file
huffman.tableToDict() #convert huffman codes(huffman.txt or any huffman codes) to dict
huffman.exportZipped('./zipped.txt')

#import zipped
#if you generated huffman codes and zipped file before you can just import them and see what 's behind
huffman.importZipped('./decoded.txt','./zippedd.txt','./huffman.txt')
```

Sample Huffman table in 'huffman.txt':
```
Character bits  code
C         4      0010
H         5      00101
m         3      010
e         4      0101
          2      10
!         3      101
```

## Debug Mode
You can turn debug mode on and see what 's happening in the background for your huffman tree ...
open ds.py file and turn DEBUG = True
```python
...

#config
DEBUG = True
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s:  %(message)s', datefmt='%M:%S')

...
```

## MinHeap

You can also generate min-heap tree for huffman tree but remember in huffman class min-heap tree automatically generated for huffman-tree
```python
value = 20
name = 'head'
headNode = ds.node(name,value)
minHeap = ds.minHeap(headNode,'min heap name')
#out minHeap will automatically heapify itself
minHeap.insertNode(ds.node('n1',2))
minHeap.insertNode(ds.node('n2',13))
```


