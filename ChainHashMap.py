# 3. zadanie: hashmap
# autor: Jana Oravcova
# datum: 1.11.2018
class ChainHashMap:
    class _Item:
        def __init__(self, key, value, next=None):
            self._key, self._value, self._next = key, value, next

        def __repr__(self):
            return repr(self._key) + ':' + repr(self._value)

    #------------------
    def __iter__(self):
        
        def iterate(current):
            while current.next is not None:
                next = current.next
                yield current
                current = next
            
        return iterate(self)

    def __init__(self, capacity=11):
        # kazdy prvok je bud None (volne),
        #   alebo je typu _Item (obsahuje key, value a nasledovnika)
        self._table = [None]*capacity
        self.keys=[]
        self.num=[]

    def _hash(self, key):
        return key % len(self._table)

    def valueof(self, key):
        # pre dany key vrati value alebo vyvola KeyError
        for bucket in self._table:
            while bucket:
                if bucket._key == key:
                    return bucket._value
                bucket = bucket._next
        raise KeyError

    def add(self, key, value=None):
        # ak existuje dany key, zmeni value
        # ak neexistuje, do tabulky prida dvojicu key, value
        # ak je tabulka viac ako na 90% obsadena, tabulka sa resize na dvojnasobok + 1
        k = self._hash(key)
        if k not in self.num:
            self.num.append(k)
        else:
            pass

        if key not in self.keys:
            self.keys.append(key)
            new = self._Item(key,value)
            temp = self._table[self._hash(key)]
            if temp is not None:
                new._next = temp
            self._table[self._hash(key)]=new
            item = self._table[self._hash(key)]
            while item:
                item = item._next

        else:
            for bucket in self._table:
                while bucket:
                    if bucket._key==key:
                        bucket._value = value
                    bucket = bucket._next
                    
        if len(self.keys)>0.9*len(self._table):
            self.resize(len(self._table)*2+1)


    def copy(self, table):
        for bucket in self._table:
            if bucket is not None:
                while bucket:
                    table.append(bucket)
                    bucket = bucket._next
                   
        return table
        
    def resize(self, n):
        old_table = self.copy([])
        self._table = [None]*n
        self.num=[]
        self.keys=[]
        for bucket in old_table:
            while bucket:
                self.add(bucket._key, bucket._value)
                bucket = bucket._next


    def _remove(self, item):
        ...

    def delete(self, key):
        # pre dany kluc vyhodi dvojicu key, value alebo vyvola KeyError
        for bucket in self._table:
            if bucket is not None:

                if bucket._key == key:
                    self._table[self._hash(key)] = bucket._next
                    self.keys.remove(bucket._key)
                    return
                while bucket._next:
                    if bucket._next._key == key:
                        #self._remove(bucket)
                        self.keys.remove(bucket._next._key)
                        temp = bucket._next._next
                        bucket._next = temp
                        return
                    bucket = bucket._next
        raise KeyError

    def __len__(self):
        # vrati pocet klucov
        return len(self.keys)


    def __iter__(self):
        for bucket in self._table:
            while bucket:
                yield bucket._key
                bucket = bucket._next
    
    def print(self):
        for index, bucket in enumerate(self._table):
            print(index, end=' ')
            while bucket:
                print(bucket, end=' -> ')
                bucket = bucket._next
            print(None)

if __name__ == '__main__':
    a = ChainHashMap(10)
    pole = [(55,'a'),(42,'b'),(15,'c'),(60,'d'),(78,'e'),
            (35,'f'),(22,'g'),(10,'h'),(11,'i'),(15,'j')]
    for key, value in pole:
        a.add(key, value)
    a.print()
    a.delete(78)
    a.print()
##    a = ChainHashMap(5)
##    d = {}
##    for i in 3, 16, 5, 11, 23, 25, 15, 18, 15, 14, 25:
##        try:
##            a.add(i, a.valueof(i) + 1)
##        except KeyError:
##            a.add(i, 1)
##        d[i] = d.get(i, 0) + 1
##    set1 = {(it, a.valueof(it)) for it in a}
##    set2 = set(d.items())
##    print('=== druhy test', set1 == set2)
##    a.print()
