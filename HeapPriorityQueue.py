# 2. zadanie: heap
# autor: Jana Oravcova
# datum: 31.10.2018

class EmptyError(Exception): pass

class HeapPriorityQueue:
    class Item:
        def __init__(self, key, value=None):
            self.key, self.value = key, value

        def __lt__(self, other):
            return self.key < other.key

        def __repr__(self):
            if self.value is None:
                return repr(self.key)
            return str((self.key, self.value))

    def __init__(self, reverse=False):
        self.data = []
        self.reverse = reverse

    def __len__(self):
        p=0
        for _list in self.data:
            p+=len(_list)
        return p

    def is_empty(self):
        if len(self.data)==0:
            return True
        if len(self.data)==1 and len(self.data[0])==0:
            return True
        else:
            return False
        

    def add(self, key, value=None):
        l = len(self.data)
        if not self.is_empty() and len(self.data[-1])<(2**(l-1)):
            self.data[-1].append(self.Item(key,value))
            i=len(self.data)-1
            j=len(self.data[-1])-1
        else:
            self.data.append([self.Item(key,value)])
            j=0
            i=len(self.data)-1
        self.heap_up(i,j)

    def min(self):
        if self.is_empty():   # vrati dvojicu alebo EmptyError
            raise EmptyError
        else:
            print(self.data[0][0].key, self.data[0][0].value)
            return self.data[0][0].key, self.data[0][0].value

    def remove_min(self):
        if self.is_empty():
            print('empty')
            raise EmptyError

        else:
            self.data[0][0], self.data[-1][-1] = self.data[-1][-1], self.data[0][0]    # vrati dvojicu alebo EmptyError
            k,v = self.data[-1][-1].key, self.data[-1][-1].value
            self.data[-1].pop()

            if len(self.data[-1])==0:
                self.data.pop()
            self.heap_down(0,0)

            return tuple((k,v))

    
    def heapify(self, seq):
        for element in seq:
            l = len(self.data)
            if not self.is_empty() and len(self.data[-1])<(2**(l-1)):
                self.data[-1].append(self.Item(element[0], element[1]))
                i=len(self.data)-1
                j=len(self.data[-1])-1
            else:
                self.data.append([self.Item(element[0],element[1])])
                j=0
                i=len(self.data)-1
        
        for i in range(len(self.data)-1, 0, -1):
            for j in range(len(self.data[i])-1,0,-1):
                print(*self.data, sep='\n')
                self.data[i][j],self.data[0][0] = self.data[0][0], self.data[i][j]
                self.heap_down(0,0)
                print(*self.data, sep='\n')
        

    def heap_up(self, i,j): #i=stupen stromu, j=prvok stupna
        if not self.reverse:
            
            while i>0 and self.data[i][j]<self.data[i-1][j//2]:
                self.data[i-1][j//2],self.data[i][j] = self.data[i][j], self.data[i-1][j//2]
                i,j = i-1, j//2
        else:
            while i>0 and self.data[i-1][j//2]< self.data[i][j]:
                self.data[i-1][j//2],self.data[i][j] = self.data[i][j], self.data[i-1][j//2]
                i,j = i-1, j//2
        #print(*self.data, sep='\n')

    def levels(self):
        p=0
        for l in self.data:
            p+=1
        return p
    def is_left(self, i, j):
        try:
            left =  self.data[i+1][j*2]
            return i+1, j*2
        except IndexError:
            return False
        
    def is_right(self, i, j):
        try:
            right =  self.data[i+1][j*2+1]
            return i+1, j*2+1
        except IndexError:
            return False

    def swap(self, i,j, k,l):
        self.data[i][j] = self.data[k][l]
        
    def heap_down(self, i, j):
        if not self.reverse:
            pi,pj = None, None
            li,lj = None, None
            while True:
                if i>=self.levels()-1:
                    break
                if self.is_left(i,j): #existuje lavy syn 
                    li,lj = i+1, j*2
                if self.is_right(i,j): #existuje pravy syn 
                    pi, pj = i+1, j*2+1

                if (pi,pj)!=(None,None) and (li,lj)!=(None,None):# existuju obaja, porovnam a prehodim
                    if self.data[pi][pj]<self.data[li][lj]:
                        mi,mj = pi,pj 
                    else:
                        mi, mj = li,lj
            
                    if self.data[mi][mj]<self.data[i][j]:
                        self.data[i][j], self.data[mi][mj] = self.data[mi][mj], self.data[i][j]
       
                        i,j = mi, mj
                        pi,pj,li,lj = None,None,None,None

                    else:
                        break
                elif (pi,pj)!=(None,None) and (li,lj)==(None,None): # je len pravy
                            
                    if self.data[pi][pj]<self.data[i][j]:
                        self.data[i][j], self.data[pi][pj] = self.data[pi][pj], self.data[i][j]
                   
                        i,j = pi, pj
                        pj,pi = None,None
                    else:
                        break
                    
                elif (pi,pj)==(None,None) and (li,lj)!=(None,None): # je len lavy
                            
                    if self.data[li][lj]<self.data[i][j]:
                        self.data[i][j], self.data[li][lj] = self.data[li][lj], self.data[i][j]
                      
                        i,j = li, lj
                        li,lj = None,None

                    else:
                        break
                else:
                    break
        else:
            pi,pj = None, None
            li,lj = None, None
            while True:
                if i>=self.levels()-1:
                    break
                if self.is_left(i,j): #existuje lavy syn 
                    li,lj = i+1, j*2
                if self.is_right(i,j): #existuje pravy syn 
                    pi, pj = i+1, j*2+1

                if (pi,pj)!=(None,None) and (li,lj)!=(None,None):# existuju obaja, porovnam a prehodim
                    if self.data[pi][pj]<self.data[li][lj]:
                        mi,mj = li,lj 
                    else:
                        mi, mj = pi,pj
            
                    if self.data[i][j]<self.data[mi][mj]:
                        self.data[i][j], self.data[mi][mj] = self.data[mi][mj], self.data[i][j]
       
                        i,j = mi, mj
                        pi,pj,li,lj = None,None,None,None

                    else:
                        break
                elif (pi,pj)!=(None,None) and (li,lj)==(None,None): # je len pravy
                            
                    if self.data[i][j]<self.data[pi][pj]:
                        self.data[i][j], self.data[pi][pj] = self.data[pi][pj], self.data[i][j]
                   
                        i,j = pi, pj
                        pj,pi = None,None
                    else:
                        break
                    
                elif (pi,pj)==(None,None) and (li,lj)!=(None,None): # je len lavy
                            
                    if self.data[i][j]<self.data[li][lj]:
                        self.data[i][j], self.data[li][lj] = self.data[li][lj], self.data[i][j]
                      
                        i,j = li, lj
                        li,lj = None,None

                    else:
                        break
                else:
                    break
            
            

    def heapify(self,seq):
        for element in seq:
            l = len(self.data)
            if not self.is_empty() and len(self.data[-1])<(2**(l-1)):
                self.data[-1].append(self.Item(element[0], element[1]))
                i=len(self.data)-1
                j=len(self.data[-1])-1
            else:
                self.data.append([self.Item(element[0],element[1])])
                j=0
                i=len(self.data)-1

        max_i, max_j = self.levels()-1, len(self.data[self.levels()-1])-1
        start_i,start_j = max_i-1, max_j//2

        for i in range(start_i, -1, -1):
            for j in range( len(self.data[i])-1, -1, -1):
                #print(i,j)
                self.heap_down(i,j)
                
            
        
        
                

if __name__ == '__main__':

    h = HeapPriorityQueue(True)
    pp = (8, 13, 7, 10, 5, 15, 12, 17, 9, 14, 4, 11, 18, 16, 6)
    for i in pp:
        h.add(i)
    print(*h.data, sep='\n')
    for i in range(len(pp)):
        print(h.remove_min())
    print('==================================')
    p = []
    while not h.is_empty():
        p.append(h.remove_min())
    print(p == sorted(p, key=lambda x: x[0]))
    h = HeapPriorityQueue()
    h.heapify(zip(pp, 'programujeme v pythone'))
    print(*h.data, sep='\n')
