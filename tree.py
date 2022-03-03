class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


class Tree:
  def __init__(self):
    self.root = None
    
  def pre_order(self):
    # root, left right
    #Pre-order: A, B, D, E, C, F
    results = []

    def walk(root):
      # Base Case of internal recursion function in a method
      if root is None:
        return

      results.append(root.value)
      walk(root.left)
      walk(root.right)
    walk(self.root)
    
    return results




  def in_order(self):
    pass

  def post_order(self):
    pass


if __name__=='__main__':
  input_values = ['A', 'B', 'C', 'D', 'E', 'F']
  T = Tree()
  T.root = Node('A')
  T.root.left = Node('B')
  T.root.right = Node('C')
  T.root.left.left = Node('D')
  T.root.right.left = Node('F')
  T.root.left.right = Node('E')
  print(T.pre_order())
  