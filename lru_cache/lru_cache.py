# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head:
            current_head = self.head
            current_head.insert_before(value)
            self.head = current_head.prev
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        current_head = self.head
        if current_head is None:
            return None

        if current_head.next is not None:
            self.head = current_head.next
        else:
            self.head = None
            self.tail = None
        self.length -= 1

        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.tail:
            current_tail = self.tail
            current_tail.insert_after(value)
            self.tail = current_tail.next
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail:
            current_tail = self.tail
            current_tail.delete()
            self.length -= 1

            if current_tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.tail = current_tail.prev

            return current_tail.value
        else:
            return None

    def contains(self, node):
        current_node = self.head
        while current_node:
            if current_node == node:
                return True
            current_node = current_node.next
        return False

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
            # Check if node exists in the linked list
        if self.contains(node):
            self.add_to_head(node.value)
            self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.contains(node):
            self.add_to_tail(node.value)
            self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.contains(node):
            if node == self.head:
                self.remove_from_head()
            elif node == self.tail:
                self.remove_from_tail()
            else:
                node.delete()
                self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        max_val = self.head.value
        current = self.head

        while current is not None:
            max_val = max(current.value, max_val)
            current = current.next
        return max_val


class LRUCache:
    """
    Our LRUCache class keeps track of: 
    the max number of nodes it can hold, 
    the current number of nodes it is holding, 
    a doubly-linked list that holds the key-value entries in the correct order, 
    as well as a storage dict that provides fast access to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.dll = DoublyLinkedList()
        self.hash = {}
        self.limit = limit
        self.length = len(self.dll)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.hash:
          found_node = self.search_for_key(key)
          if found_node is not None:
            self.dll.move_to_front(found_node)
          else: 
            return None
          return self.hash[key]
        else:
          return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.hash:
          self.hash[key] = value 
          
          found_node = self.search_for_key(key)

          if found_node is not None:
            self.dll.move_to_front(found_node)
          else: 
            return None
        else:
          if self.length + 1 > self.limit:
            current_key = self.dll.remove_from_tail()

            self.hash = {k: v for k, v in self.hash.items() if k != current_key}

          self.dll.add_to_head(key)
          self.length += 1
          self.hash[key] = value

    def search_for_key(self, key):
      current_node = self.dll.head

      while current_node.value:
        if current_node.value == key:
          return current_node
        current_node = current_node.next
      return None



