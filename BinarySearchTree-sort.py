# 5. zadanie: tree_sort
# autor: Jana Oravcova
# datum: 16.11.2018
class BVS:
    def __init__(self, pole):
        self.pole = pole
        self.left = [None]
        self.right = [None]

    

    def insert(self, index):
        px = 0
        while True:
            if self.pole[px]<=self.pole[index]:
                if self.right[px] is None: # finish the loop, can insert a node
                    self.right[px] = index
                    self.right.append(None)
                    self.left.append(None)
                    break
                else:
                    px = self.right[px]
            else:
                if self.left[px] is None:#finish the loop
                    self.left[px] = index
                    self.left.append(None)
                    self.right.append(None)
                    break
                else:
                    px = self.left[px]
                    
                    
        
    def inorder(self, reverse=False):
        stack=[]
        current = 0
        if not reverse:
            while True:
                if current is not None:
                    stack.append(current)
                    current = self.left[current]
                else:
                    if len(stack)>0:
                        node = stack.pop()
                        yield self.pole[node]
                        current = self.right[node]
                    else:
                        break
        else:
            while True:
                if current is not None:
                    stack.append(current)
                    current = self.right[current]
                else:
                    if len(stack)>0:
                        node = stack.pop()
                        yield self.pole[node]
                        current = self.left[node]
                    else:
                        break
        
def tree_sort(pole, reverse=False):
    tree = BVS(pole)
    for i in range(1, len(pole)):
        tree.insert(i)

    return tree.inorder(reverse)

if __name__ == '__main__':
    p = (27, 25, 34, 23, 25, 31, 28, 21)
    print(*tree_sort(p))
    print(*tree_sort(p, reverse=True))
