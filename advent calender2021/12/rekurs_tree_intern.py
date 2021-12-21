

class TreeNode:
  def __init__(self, value):
    self.value = value # data
    self.children = [] # references to other nodes
 
  def add_child(self, child_node):
    # creates parent-child relationship
    self.children.append(child_node) 
    
 
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
        print(current_node.value)
        nodes_to_visit += current_node.children
      if current_node.children == []:
          reitit.append(nykyinen_reitti)
          nykyinen_reitti = []

    return reitit
 
 

parent = TreeNode("isi")
l1 = TreeNode("lapsi1")
l2 = TreeNode("lapsi2")
l3 = TreeNode("lapsi3")

ll1 = TreeNode("lapsenlapsi1")

parent.add_child(l1)
parent.add_child(l2)
parent.add_child(l3)

ll1.add_child(l1)


l1.add_child(ll1)
#l2.add_child(ll1)
l3.add_child(TreeNode("lapsenlapsi3"))

print(parent.traverse([]))
