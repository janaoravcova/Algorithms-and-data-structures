# 4. zadanie: mnozina AVL stromov
# autor: Jana Oravcova
# datum: 14.11.2018
class BST:
    class Node:
        def __init__(self, data):
            self.data, self.left, self.right = data, None, None
            
    def __init__(self, arr=None):
        self.root = None
            
    def __eq__(self, other):
        return self.compare(self.root, other.root)
    
    def compare(self,a,b):
        if a is None and b is None: 
            return True 
        if a is not None and b is not None: 
            return ((a.data == b.data) and self.compare(a.left, b.left) and self.compare(a.right, b.right))  
        return False
    
    def __repr__(self):
        return str(self.preorder())
    
    def preorder(self):
        def preorder_rek(node):
            if node is not None:
                l.append(node.data)
                preorder_rek(node.left)
                preorder_rek(node.right)
                

        l = []
        preorder_rek(self.root)
        return tuple(l)
    
    def __hash__(self):
        count=""
        pole=self.preorder()
        for p in pole:
            count+=str(ord(str(p)))
        return int(count)
    
    def insert(self, data):
 
        if self.root is None:
            self.root=self.Node(data)
        else:
            _root=self.root
            while True:
                if _root.data>=data:
                    if _root.left is None:
                        _root.left=self.Node(data)
                        break
                    else:
                        _root = _root.left
                        
                else:
                    if _root.right is None:
                        _root.right=self.Node(data)
                        break
                    else:
                        _root = _root.right

    def height(self,root):
        if root is None: 
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def is_balanced(self,root):
        if root is None: 
            return True
 
        lh = self.height(root.left) 
        rh = self.height(root.right) 

        if (abs(lh - rh) <= 1) and self.is_balanced(root.left) is True and self.is_balanced( root.right) is True: 
            return True

        return False
  
                    
                    
    def avl(self):
        return self.is_balanced(self.root)
        
        

class AVLSet:
    def __init__(self):
        self.set = set()
        
    def add(self, seq):
        b=BST()
        for s in seq:
            b.insert(s)
            if not b.avl():
                return 
        if b.avl():
            self.set.add(b)
        
    def __iter__(self):
        yield from self.set
        
    def __len__(self):
        return len(self.set)

    def all(self, seq):
        def permutations(seq,k,n):
            if k==n:
                _all.append(seq[:])
            else:
                for i in range(k,n+1):
                    seq[k],seq[i] = seq[i],seq[k]
                    permutations(seq,k+1, n)
                    seq[k],seq[i] = seq[i],seq[k]
        _all=[]
        permutations(list(seq), 0, len(seq)-1)
        for s in _all:
            self.add(tuple(s))

if __name__ == '__main__':
    t0 = BST()
    for i in ('p','y','t','h','o','n'):
        t0.insert(i)
    print(t0)
    print('avl =', t0.avl())
    t1 = BST()
    for i in (1, 2,3,4,5):
        t1.insert(i)
    print(t1)
    print('avl =', t1.avl())
    t2 = BST()
    for i in (2, 4, 3, 1):
        t2.insert(i)
    print(t2)
    print('avl =', t2.avl())
    t3 = BST()
    for i in (1, 2, 4, 3):
        t3.insert(i)
    print('eq =', t2 == t3)
    print(hash(t2)==hash(t3))
    mn = AVLSet()
    mn.add((1, 2, 3, 4))
    mn.add((2, 4, 3, 1))
    mn.add((2, 1, 4, 3))
    mn.add((2, 4, 1, 3))
    print('set:')
    for t in mn:
        print(t)
    print('all:')
    mn = AVLSet()
    mn.all((1, 2, 3, 4))
    print(*mn, sep='\n')
    mn = AVLSet()
    mn.all(range(5))
    print('all range(5) =', len(mn))
