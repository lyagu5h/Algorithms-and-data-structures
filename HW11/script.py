class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"({self.left} {self.value} {self.right})"

# Construct the expression tree based on the given expression
# (a + b) * (c * (d + e + f) + g * (i + j^2))

# Leaf nodes
a = ExpressionNode("a")
b = ExpressionNode("b")
c = ExpressionNode("c")
d = ExpressionNode("d")
e = ExpressionNode("e")
f = ExpressionNode("f")
g = ExpressionNode("g")
i = ExpressionNode("i")
j = ExpressionNode("j")
two = ExpressionNode("2")

# Subtree for j^2
j_squared = ExpressionNode("^", j, two)

# Subtree for i + j^2
i_plus_j_squared = ExpressionNode("+", i, j_squared)

# Subtree for g * (i + j^2)
g_times_i_plus_j_squared = ExpressionNode("*", g, i_plus_j_squared)

# Subtree for d + e + f
d_plus_e_plus_f = ExpressionNode("+", ExpressionNode("+", d, e), f)

# Subtree for c * (d + e + f)
c_times_d_plus_e_plus_f = ExpressionNode("*", c, d_plus_e_plus_f)

# Subtree for c * (d + e + f) + g * (i + j^2)
c_plus_g = ExpressionNode("+", c_times_d_plus_e_plus_f, g_times_i_plus_j_squared)

# Subtree for (a + b)
a_plus_b = ExpressionNode("+", a, b)

# Final tree for (a + b) * (c * (d + e + f) + g * (i + j^2))
expression_tree = ExpressionNode("*", a_plus_b, c_plus_g)

# Verify the expression tree by converting it back to string
print("Expression Tree Representation:")
print(repr(expression_tree))