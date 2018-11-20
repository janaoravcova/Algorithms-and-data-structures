from abc import ABC, abstractmethod

class Tree(ABC):

    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self, node):
        pass

    @abstractmethod
    def children(self, node):
        pass

    @abstractmethod
    def num_children(self, node):
        pass

    @abstractmethod
    def siblings(self, node):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def data(self, node):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_root(self, node):
        return self.root() == node

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, node):
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))

    def height(self, node=None):
        if node is None:
            node = self.root()
        if node is None or self.is_leaf(node):
            return 0
        return 1 + max(self.height(n) for n in self.children(node))

    @abstractmethod
    def preorder(self):
        pass

    @abstractmethod
    def postorder(self):
        pass

    @abstractmethod
    def breadthfirst(self):
        pass

    @abstractmethod
    def leaves(self):
        pass
