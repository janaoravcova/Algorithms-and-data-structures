# 1. zadanie: tree
# autor: Jana Oravcova
# datum: 31.10.2018

from tree import Tree

class ParentTree(Tree):

    class Node:
        def __init__(self, data, parent=None):
            self._data = data
            self._parent = parent

    #----------------------------------

    def __init__(self):
        self._all = set()

    def add_node(self, data, parent=None):
        node = self.Node(data, parent)
        self._all.add(node)
        return node
    
    def root(self):
        for p in self._all:
            if p._parent==None:
                return p
        return None

   
    def parent(self, node):
        for p in self._all:
            if p==node:
                return p._parent
        return None


    def children(self, node):
        s=[]
        for p in self._all:
          
            if p._parent==node:
                yield p


    def num_children(self, node):
        i=0
        for p in self._all:
            if p._parent==node:
                i+=1
        return i


    def siblings(self, node):
        s=[]
        for p in self._all:
            if p._parent==node._parent and p!=node:
                yield p

   
    def __len__(self):
        return len(self._all)


    def data(self, node):
        return node._data


    def __iter__(self):
        for p in self._all:
            yield p

 
    def preorder(self):

        def subtree_preorder(node):
            yield node
            for n in self.children(node):
                yield from subtree_preorder(n)

        if not self.is_empty():
            yield from subtree_preorder(self.root())

    def postorder(self):

        def subtree_postorder(node):
            for n in self.children(node):
                yield from subtree_postorder(n)
            yield node

        if not self.is_empty():
            yield from subtree_postorder(self.root())
    def breadthfirst(self):
        stack =[]
        all_nodes = []
        r = self.root()
        stack.append(r)
        yield r
        for ch in self.children(r):
            stack.append(ch)
            if ch not in all_nodes:
                yield ch
        stack.pop(0)
        while stack:
            nod = stack[0]
            for ch in self.children(nod):
                stack.append(ch)
                if ch not in all_nodes:
                    yield ch
            stack.pop(0)


    def leaves(self):
        
        def f(node):
            for n in self.children(node):
                yield from f(n)
            if self.is_leaf(node):
                yield node

        res = []
        if not self.is_empty():
            yield from   f(self.root())
      

            
if __name__ == '__main__':
    t = ParentTree()
    r = t.add_node('a')
    v1 = t.add_node('b', r)
    v2 = t.add_node('c', v1)
    v3 = t.add_node('d', v1)
    v4 = t.add_node('e', r)
    v5 = t.add_node('f', v1)
    v6 = t.add_node('g', v5)
    v7 = t.add_node('h', v3)
    v8 = t.add_node('i', v4)
    v9 = t.add_node('j', v5)
    v10 = t.add_node('k', v4)
    v11 = t.add_node('l', v7)
    v12 = t.add_node('m', v7)

    print('preorder =', *(t.data(n) for n in t.preorder()))
    print('postorder =', *(t.data(n) for n in t.postorder()))
    print('breadthfirst =', *(t.data(n) for n in t.breadthfirst()))
    print('leaves =', *(t.data(n) for n in t.leaves()))
    print('iter =', *(t.data(n) for n in t))

    for node in t:
        print(t.data(node), t.height(node), t.depth(node), t.is_leaf(node))
    for s in t.siblings(v2):
        print(t.data(s))
