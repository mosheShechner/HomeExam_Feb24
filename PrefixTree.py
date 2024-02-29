# ##########################################################################################
# module        PrefixTree
# ##########################################################################################
# path          ...\repository\???
# Purpose       data structure for strings
# description   this module is a data structure to store string keys. It consist of a tree
#               that with vertices of type 'PrefixTreeNode' (also implemented here) methods:
#               (1) insert(some_key) - inserts a key to the structure; If the key already
#               exists, it remains in the structure and no feedback is given.
#               (2) contains(key)    - query whether 'key' exists in the structure.
# additionally, in this file the PrefixTreeNode class is implemented and a short test bench is
# ##########################################################################################

class PrefixTreeNode:
    def __init__(self, val, is_key=False):
        self.val = val
        self.is_key = is_key
        self.child_list = []

    def __repr__(self):
        return "value = {0}; nof children = {1}".format(self.val, len(self.child_list))

    def add_child(self, child):
        if isinstance(child, PrefixTreeNode):
            self.child_list.append(child)
        else:
            print("wrong type")

#    def add_child_list(self, new_child_list):
#        for new_child in new_child_list:
#            self.add_child(new_child)
#
#    def is_leaf(self):
#        return len(self.child_list) == 0

    def get_is_key(self):
        return self.is_key

    def set_is_key(self, is_key):
        self.is_key = is_key

    def has_child(self, checked_val):
        for child in self.child_list:
            if child.val == checked_val: return True
        return False
    def get_child(self, checked_val):
        for child in self.child_list:
            if child.val == checked_val: return child
        return None

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode("", False)

    def __repr__(self):
        return self.print_PFtree(self.root)

    def print_PFtree(self, curr):
        children = ""
        for child in curr.child_list:
            if child.get_is_key():
                children += child.val + " key " + self.print_PFtree(child)
            else:
                children += child.val + " " + self.print_PFtree(child)
        return "[" + children + "]"

    def insert(self, element):
        curr = self.root
        char_list = list(element)
        for char in char_list:
            next = curr.get_child(char)
            if next == None:
                next = PrefixTreeNode(char)
                curr.add_child(next)
            curr = next
        curr.set_is_key(True)

    def contains(self, element):
        curr = self.root
        char_list = list(element)
        for char in char_list:
            next = curr.get_child(char)
            if next == None:
                return False
            else:
                curr = next
        return curr.get_is_key()

# ###############
# test bench
# ###############

prefixTree = PrefixTree()
prefixTree.insert("abc")
prefixTree.insert("aaa")
prefixTree.insert("a")
prefixTree.insert("abcdefghij")
prefixTree.insert("abcdef")
print(prefixTree)

print("expect True;  real = {0}".format(prefixTree.contains("a")))
print("expect False; real = {0}".format(prefixTree.contains("ab")))
print("expect True;  real = {0}".format(prefixTree.contains("abc")))
print("expect False; real = {0}".format(prefixTree.contains("aa")))
print("expect True;  real = {0}".format(prefixTree.contains("aaa")))
print("expect False; real = {0}".format(prefixTree.contains("d")))
print("expect False; real = {0}".format(prefixTree.contains("abcd")))
print("expect False; real = {0}".format(prefixTree.contains("abcf")))
print("expect False; real = {0}".format(prefixTree.contains("abcz")))
print("expect True;  real = {0}".format(prefixTree.contains("abcdef")))
print("expect True;  real = {0}".format(prefixTree.contains("abcdefghij")))
print("expect False; real = {0}".format(prefixTree.contains("abcdefghijk")))