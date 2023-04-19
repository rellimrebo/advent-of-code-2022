# 7.1

class Node:
    def _init_(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_directory_tree(root_directory, new_directory):
    root = Node(root_directory)

    root_directory.add_child(new_directory)