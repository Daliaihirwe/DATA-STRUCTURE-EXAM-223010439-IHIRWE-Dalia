class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 4 + self.name)
        for child in self.children:
            child.display(level + 1)


root = TreeNode("Warehouse")
section_a = TreeNode("Section A")
section_b = TreeNode("Section B")
section_a.add_child(TreeNode("Item 1"))
section_a.add_child(TreeNode("Item 2"))
section_b.add_child(TreeNode("Item 3"))
root.add_child(section_a)
root.add_child(section_b)
root.display()