from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))

class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if  key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def _removemin(self, node):
        if node.left is None:
            return node.right
        node.left =  self._removemin(node.left)
        node.size =  1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if node is None:
            raise KeyError(f'key not found: {key}')
        else:
            cmp = key - node.key
            # search for the key and recursively call remove
            if cmp < 0:
                node.left = self._remove(node.left, key)
            elif cmp > 0:
                node.right = self._remove(node.right, key)
            else:
                # if no right child
                if node.right is None:
                    return node.left
                # if no left child
                if node.left is None:
                    return node.right
                # if has both left and right, find min of right node as the new curr node
                temp = node
                node = self._min(temp.right)
                node.right = self._removemin(temp.right)
                node.left = temp.left

            # update size
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node

    # find the min node in a subtree
    def _min(self, node):
        if node.left is None:
            return node
        else:
            return self._min(node.left)

    @staticmethod
    def _size(node):
        return node.size if node else 0


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree
        self.traversalType = traversalType
        self.traversalLst = []
        # Decide traverser and store the traversal result into self.traversalLst
        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif self.traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif self.traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.traversalLst) == 0:
            raise StopIteration()
        return self.traversalLst.pop(0)


    def preorder(self, bst: BSTTable):
        def _traverse(node):
            if node is None:
                return
            self.traversalLst.append(node)
            _traverse(node.left)
            _traverse(node.right)

        _traverse(bst._root)

    def inorder(self, bst: BSTTable):
        def _traverse(node):
            if node is None:
                return
            _traverse(node.left)
            self.traversalLst.append(node)
            _traverse(node.right)

        _traverse(bst._root)


    def postorder(self, bst: BSTTable):
        def _traverse(node):
            if node is None:
                return
            _traverse(node.left)
            _traverse(node.right)
            self.traversalLst.append(node)

        _traverse(bst._root)




# Tree and Removal demo
# t = BSTTable()
# t.put(5, 'a')
# t.put(1, 'b')
# t.put(2, 'c')
# t.put(0, 'd')
# print(t._root)
# print(t._removemin(t._root))
# print(t._remove(t._root, 5))
# print(t._remove(t._remove(t._root, 5), 1))
# #print(t._remove(t._root, 10))


##  DFSTraversal
# iterator = DFSTraversal(t, DFSTraversalTypes.POSTORDER)
# for i in iterator:
#      print(i.key)

# input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
# bst = BSTTable()
# for key, val in input_array:
#     bst.put(key, val)
# traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
# for node in traversal:
#     print(str(node.key) + ', ' + node.val)
