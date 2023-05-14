class Node:
    def _init_(self, data, prity):
        self.data = data
        self.prity = prity # 1 (tertinggi), 2, 3, 4, ...
        self.a = None

class PriorityQueueUnsorted:
    def _init_(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def is_empty(self):
        if self.sz == 0:
            return True
        else:
            return False

    def _len_(self):
        return self.sz
        
    def add(self, data, prity):
        new = Node(data, prity)
        if self.is_empty(): 
            self.head = new
            self.tail = new
        else: 
            self.tail.a = new
            self.tail = new
        self.sz = self.sz + 1

    def remove(self): 
        if not self.is_empty():
            if self.sz == 1:
                help = self.head
                self.head = None
                self.tail = None
                del help
            else:
                minpriority = self.head.prity

                de = self.head
                while de != None:
                    if de.prity < minpriority:
                        minpriority = de.prity
                    de = de.a
                de = self.head
                while de.prity != minpriority:
                    de = de.a

                if de == self.head:
                    self.head = self.head.a
                    del de
                else:
                    help = self.head
                    while help.a != de:
                        help = help.a

                    help.a = de.a
                    del de
                    self.tail = self.head

                    while self.tail.a != None:
                        self.tail = self.tail.a
        self.sz = self.sz - 1
    
    def peek(self): 
        if self.is_empty() == True:
            return None
        else:
            if self.sz == 1:
                return tuple([self.head.data, self.head.prity])
            else:
                minpriority = self.head