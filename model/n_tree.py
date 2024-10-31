
class NaryTreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent

    def __str__(self):
        return f"Node({self.data})"

class NaryTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, data, parent_data=None):

        parent_node = next((node for node in self.nodes if node.data == parent_data), None)
        new_node = NaryTreeNode(data, parent_node)
        self.nodes.append(new_node)
        return new_node

    def display(self):

        for node in self.nodes:
            parent_data = node.parent.data if node.parent else "None"
            print(f"{node} - Parent: {parent_data}")

if __name__ == '__main__':
    tree = NaryTree()
    root = tree.add_node("Root Person")
    child1 = tree.add_node("Child 1", "Root Person")
    child2 = tree.add_node("Child 2", "Root Person")


    grandchild1 = tree.add_node("Grandchild 1.1", "Child 1")
    grandchild2 = tree.add_node("Grandchild 1.2", "Child 1")


    tree.display()
