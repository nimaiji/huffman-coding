import ds
import gui
import logger

huffman = ds.huffman('./input.txt')
huffman.generateTree()
huffman.generateTable('./huffman.txt')
huffman.tableToDict('./huffman.txt')
huffman.exportZipped('./zipped.txt')
huffman.importZipped('./decoded.txt','./zipped.txt','./huffman.txt')
