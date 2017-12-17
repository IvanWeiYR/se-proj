class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)
def get_sorted_list(root):
    current = root 
    s = [] # initialze stack
    done = 0
    sorted_list = []
    while(not done):
        if current is not None:
            s.append(current)
            current = current.left 
        else:
            if(len(s) > 0):
                current = s.pop()
                sorted_list.append(current.data)
                current = current.right 
            else:
                done = 1
    return sorted_list
def sort(alist = None):
    if alist is None or len(alist) == 0:
        return 
    r = Node(alist[0])
    for i in range(1, len(alist)):
        binary_insert(r, Node(alist[i]))
    return get_sorted_list(r)


if __name__ == "__main__":
    x = [-1, 399, 3,4,5,1,2,8,3,7,6]
    print(x)
    sorted_list = sort(x)
    print(sorted_list)
    result = True
    for i in range(1,len(sorted_list)):
        if(sorted_list[i] < sorted_list[i-1]):
            result = False

    print(result)


