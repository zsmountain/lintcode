################################### List ###################################
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, l):
        if not l:
            self.head = None
            return
        head = ListNode(l[0])
        pre = head
        for i in range(1, len(l)):
            cur = ListNode(l[i])
            pre.next = cur
            pre = cur
        self.head = head

    def print(self):
        head = self.head
        while head:
            print(head.val, '->', end = ' ')
            head = head.next
        print('None')


################################### Graph ###################################
'''
How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/
'''


class DirectedGraphNode:
  def __init__(self, x):
      self.label = x
      self.neighbors = []

def createGraph(graph_str):
  if not graph_str:
    return {}

  nodes = {}
  nodes_str = graph_str.split('#')
  for node_str in nodes_str:
    values = node_str.split(',')
    node = DirectedGraphNode(values[0])
    nodes[values[0]] = node
  
  for node_str in nodes_str:
    values = node_str.split(',')
    for i in range(1, len(values)):
      nodes[values[0]].neighbors.append(nodes[values[i]])

  return [nodes[node] for node in nodes]
        
def printGraph(graph):
  for node in graph:
    print(node.label, [n.label for n in node.neighbors])
################################### Tree ###################################
from copy import deepcopy as deepcopy
import sys

class Queue(object):
  def __init__(self, items=None):
    if items is None:
      self.a = []
    else:
      self.a = items

  def enqueue(self, b):
    self.a.insert(0, b)

  def dequeue(self):
    return self.a.pop()

  def isEmpty(self):
    return self.a == []

  def size(self):
    return len(self.a)

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def visit(self):
    sys.stdout.write(self.val)

  def getNumNodes(self):
    total = 0
    if self.left:
      total += self.left.getNumNodes()
    if self.right:
      total += self.right.getNumNodes()
    return total + 1

  @classmethod
  def createTree(cls, depth):
    tree = TreeNode('X')
    cls.createTreeHelper(tree, depth, 1)
    return tree

  @classmethod
  def createTreeHelper(cls, node, depth, cur):
    if cur == depth:
      return
    node.left = TreeNode('X')
    node.right = TreeNode('XX')
    cls.createTreeHelper(node.left, depth, cur + 1)
    cls.createTreeHelper(node.right, depth, cur + 1)

  def getHeight(self):
    return TreeNode.getHeightHelper(self)

  @staticmethod
  def getHeightHelper(node):
    if not node:
      return 0
    else:
      return max(TreeNode.getHeightHelper(node.left), TreeNode.getHeightHelper(node.right)) + 1

  def fillTree(self, height):
    TreeNode.fillTreeHelper(self, height)

  def fillTreeHelper(node, height):
    if height <= 1:
      return
    if node:
      if not node.left:
          node.left = TreeNode(' ')
      if not node.right:
          node.right = TreeNode(' ')
      TreeNode.fillTreeHelper(node.left, height - 1)
      TreeNode.fillTreeHelper(node.right, height - 1)

  def prettyPrint(self):
    """
    """
    # get height of tree
    total_layers = self.getHeight()

    tree = deepcopy(self)

    tree.fillTree(total_layers)
    # start a queue for BFS
    queue = Queue()
    # add root to queue
    queue.enqueue(tree)  # self = root
    # index for 'generation' or 'layer' of tree
    gen = 1
    # BFS main
    while not queue.isEmpty():
      # copy queue
      #
      copy = Queue()
      while not queue.isEmpty():
        copy.enqueue(queue.dequeue())
      #
      # end copy queue

      first_item_in_layer = True
      edges_string = ""
      extra_spaces_next_node = False

      # modified BFS, layer by layer (gen by gen)
      while not copy.isEmpty():

        node = copy.dequeue()

        # -----------------------------
        # init spacing
        spaces_front = pow(2, total_layers - gen + 1) - 2
        spaces_mid = pow(2, total_layers - gen + 2) - 2
        dash_count = pow(2, total_layers - gen) - 2
        if dash_count < 0:
          dash_count = 0
        spaces_mid = spaces_mid - (dash_count*2)
        spaces_front = spaces_front - dash_count
        init_padding = 2
        spaces_front += init_padding
        if first_item_in_layer:
          edges_string += " " * init_padding
        # ----------------------------->

        # -----------------------------
        # construct edges layer
        edge_sym = "/" if node.left and node.left.val is not " " else " "
        if first_item_in_layer:
          edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
        else:
          edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
        edge_sym = "\\" if node.right and node.right.val is not " " else " "
        edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
        # ----------------------------->

        # -----------------------------
        # conditions for dashes
        if node.left and node.left.val == " ":
          dash_left = " "
        else:
          dash_left = "_"

        if node.right and node.right.val == " ":
          dash_right = " "
        else:
          dash_right = "_"
        # ----------------------------->

        # -----------------------------
        # handle condition for extra spaces when node lengths don't match or are even:
        if extra_spaces_next_node:
          extra_spaces = 1
          extra_spaces_next_node = False
        else:
          extra_spaces = 0
        # ----------------------------->

        # -----------------------------
        # account for longer val
        val_length = len(str(node.val))
        if val_length > 1:
          if val_length % 2 == 1:  # odd
            if dash_count > 0:
              dash_count -= ((val_length - 1)//2)
            else:
              spaces_mid -= (val_length - 1)//2
              spaces_front -= (val_length - 1)//2
              if val_length is not 1:
                extra_spaces_next_node = True
          else:  # even
            if dash_count > 0:
              dash_count -= ((val_length)//2) - 1
              extra_spaces_next_node = True
              # dash_count += 1
            else:
              spaces_mid -= (val_length - 1)
              spaces_front -= (val_length - 1)
        # ----------------------------->

        # -----------------------------
        # print node with/without dashes
        if first_item_in_layer:
          print((" " * spaces_front) + (dash_left * dash_count) + \
              str(node.val) + (dash_right * dash_count), end = '')
          first_item_in_layer = False
        else:
          print((" " * (spaces_mid-extra_spaces)) + (dash_left *
                                                    dash_count) + str(node.val) + (dash_right * dash_count), end = '')
        # ----------------------------->

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

      # print the fun squiggly lines
      if not queue.isEmpty():
        print("\n" + edges_string)

      # increase layer index
      gen += 1
    print()
    
def createTree(vals):
    if not vals:
        return None
    node_list = []
    root = TreeNode(vals[0])
    node_list.append(root)
    index = 0
    is_left = True
    for i in range(1, len(vals)):
        val = vals[i]
        if val != '#':
            node = TreeNode(val)
            if is_left:
                node_list[index].left = node
            else:
                node_list[index].right = node
            node_list.append(node)
        if not is_left:
            index += 1
        is_left = not is_left

    return root

def getSampleBstTree():
  return createTree([8, 3, 10, 1, 6, '#', 14, '#', '#', 4, 7, 13])

if __name__ == '__main__':
  # prep the tree...
  #
  # layer 1
  root = TreeNode('A')

  # layer 2
  root.left = TreeNode('B')
  root.right = TreeNode('C')

  # layer 3
  root.left.left = TreeNode('D')
  root.left.right = TreeNode('E')

  root.left.right.right = TreeNode.createTree(2)

  root.right.left = TreeNode('F')
  root.right.right = TreeNode('G')

  # layer 3
  root.left.left.left = TreeNode('H')
  root.left.left.right = TreeNode('I')
  root.left.right.left = TreeNode('J')
  # root.left.right.right = TreeNode('K')
  # root.right.left.left = TreeNode('L')
  # root.right.left.right = TreeNode('M')
  root.right.right.left = TreeNode('N')
  root.right.right.right = TreeNode('O')

  root.prettyPrint()
