class Movie:
   def __init__(self, name, reviews, score):
      self.name = name
      self.reviews = reviews
      self.score = score
      

class Node:
    '''def __init__(self, data = None):
        self.data = data
        self.next = None'''
    def __init__(self, name = None, reviews = None, description = None, release_date = None, genre = None, in_theaters = None, score = None):
      self.name = name
      self.reviews = reviews
      self.description = description
      self.release_date = release_date
      self.genre = genre
      self.in_theaters = in_theaters
      self.score = score
      self.next = None
      
class linked_list:
    def __init__(self):
        self.head = Node()
        
    def append(self, name, reviews, description, release_date, genre, in_theaters, score):
        new_node = Node(name, reviews, description, release_date, genre, in_theaters, score)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.name)
        print (elems)
    
    def get(self, name):
        cur_idx = 0
        cur_node = self.head
        while cur_idx < self.length():
            if name == cur_node.name:
               print [cur_node.name, cur_node.reviews, cur_node.score]
            cur_node = cur_node.next
            cur_idx += 1
    
    def erase(self, name):
        cur_idx = -1
        cur_node = self.head
        while cur_idx < index:
            last_node = cur_node
            cur_node = cur_node.next
            cur_idx += 1
            if cur_idx == index:
                last_node.next = cur_node.next

list = linked_list()
list.append("Jurassic Park", "good", "dinosaurs", "3/3/3", "documentary", "Yes", .7)
list.display()
list.get("Jurassic Park")




