class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(expression):
    
    tokens = expression.split()
    return recursive_build_tree(tokens, [0])

def recursive_build_tree(tokens, index):

    stack = []
    while index[0] < len(tokens):
        token = tokens[index[0]]

        if token == '(': # we need to go down a level
            index[0] += 1
            node = recursive_build_tree(tokens, index)
            stack.append(node)

        elif token.isdigit(): # this is a leaf node, so store it in the stack and find its parent
            stack.append(Node(int(token)))
            index[0] += 1

        elif token in '+-*/': # this node has children, so assign the left one from the stack and find the right one
            operator_node = Node(token)
            index[0] += 1
            right = recursive_build_tree(tokens, index)
            operator_node.right = right
            operator_node.left = stack.pop()
            return operator_node
        
        elif token == ')': # we need to go up a level
            index[0] += 1
            return stack.pop()
        
        else:
            index[0] += 1
    return stack.pop()

def recursive_solve_tree(node):

    if node.left is None and node.right is None: # node is leaf -> node is an integer
        return node.data
    
    # otherwise, node is not an integer, and therefore must have a left AND right child.
    # no need to check for either side.
    left_child = recursive_solve_tree(node.left) 
    right_child = recursive_solve_tree(node.right)
    
    if node.data == '+':
        return left_child + right_child
    elif node.data == '-':
        return left_child - right_child
    elif node.data == '*':
        return left_child * right_child
    elif node.data == '/':
        return left_child / right_child

test = "5"
print(recursive_solve_tree(build_tree(test))) # prints 5 (:


test = "( ( 1 + ( 4 * 9 ) ) - 4 )"
print(recursive_solve_tree(build_tree(test))) # prints 33 (:


test = "( ( 8 * ( 9 / 3 ) ) + 6 )"
print(recursive_solve_tree(build_tree(test))) # prints 30.0 (cause of the division) (: