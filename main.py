from btree import *

def main():
	B = BTree(3)
	for i in range(10):
		B.insert(i)
	B.print_tree(B.root)
	print("\n")
	B.delete(B.root,49)
	if B.search(7) != None:
		x = B.search(7)
	else:
		print("Element not found!")
	print("\n")
	B.print_tree(B.root)

if __name__ == '__main__':
	main()