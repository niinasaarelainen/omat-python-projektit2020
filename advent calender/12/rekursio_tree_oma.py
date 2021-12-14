

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes
 
  def add_child(self, child_node):
    self.children.append(child_node) 
    
  def add_children(self, children):
    self.children += children 
 
  def traverse(self, linjat):   #TODO linjat
    # moves through each node referenced from self downwards
    nodes_to_visit = [self]
    reitit = []
    nykyinen_reitti = []

    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()

      print("nykyinen_reitti", nykyinen_reitti)

      if current_node.value not in nykyinen_reitti:
        nykyinen_reitti.append(current_node.value)
        #print(current_node.value)
        nodes_to_visit += current_node.children
      
      if current_node.children == [] :
          reitit.append(nykyinen_reitti)
          print(nykyinen_reitti)
          nykyinen_reitti = []
          #nodes_to_visit = []

    return reitit
 
"""
    start
    /   \
c--A-----b--d
    \   /
     end
"""

start = TreeNode("start")
c = TreeNode("c")
a = TreeNode("A")
b = TreeNode("b")
d = TreeNode("d")
end = TreeNode("end")

start.add_children([a, b])
a.add_children([c, b, end])
b.add_children([a, d, end])
c.add_children([a])
d.add_children([b])

print(start.traverse([]))
