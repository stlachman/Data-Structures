import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        queue = Queue()
        queue.enqueue(self)
        while queue.len() > 0:
          current_node = queue.dequeue()
          if value > current_node.value:
            if current_node.right is None:
              current_node.right = BinarySearchTree(value)
            else:
              queue.enqueue(current_node.right)
          elif value < current_node.value:
            if current_node.left is None:
              current_node.left = BinarySearchTree(value)
            else:
              queue.enqueue(current_node.left)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_tree = self
        while current_tree is not None:
          if target == current_tree.value:
            return True
          elif target > current_tree.value:
            current_tree = current_tree.right
          elif target < current_tree.value:
            current_tree = current_tree.left 
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        while current_node.right is not None:
          current_node = current_node.right
        return current_node.value
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        current_node = self
        queue = Queue()
        queue.enqueue(current_node)
        while queue.len() > 0:
          current_node = queue.dequeue()

          cb(current_node.value)
          for item in [current_node.left, current_node.right]:
            if item is not None:
              queue.enqueue(item)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        def helper(node):
          if node:
            helper(node.left)
            print(node.value)
            helper(node.right)
        helper(node)

        # Iterative
        # current_node = node
        # stack = Stack()

        # while True:
        #   if current_node is not None:
        #     stack.push(current_node)
        #     current_node = current_node.left
        #   elif stack.len() > 0:
        #     current_node = stack.pop()
        #     print(current_node.value)
        #     current_node = current_node.right 
        #   else:
        #     break
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        current_node = node
        queue = Queue()
        queue.enqueue(current_node)
        while queue.len() > 0:
          current_node = queue.dequeue()

          print(current_node.value)
          for item in [current_node.left, current_node.right]:
            if item is not None:
              queue.enqueue(item)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        current_node = node 
        stack.push(current_node)

        while stack.len() > 0:
          current_node = stack.pop()
          print(current_node.value)
          if current_node.left is not None:
            stack.push(current_node.left)
          if current_node.right is not None:
            stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        def helper(node):
          if node:
            print(node.value)
            helper(node.left)
            helper(node.right)
        helper(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        def helper(node):
          if node:
            helper(node.left)
            helper(node.right)
            print(node.value)
        helper(node)