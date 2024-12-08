class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"{self.value}"
        return f"({self.left} {self.value} {self.right})"

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

j_squared = ExpressionNode("^", j, two)
i_plus_j_squared = ExpressionNode("+", i, j_squared)
g_times_i_plus_j_squared = ExpressionNode("*", g, i_plus_j_squared)
d_plus_e_plus_f = ExpressionNode("+", ExpressionNode("+", d, e), f)
c_times_d_plus_e_plus_f = ExpressionNode("*", c, d_plus_e_plus_f)
c_plus_g = ExpressionNode("+", c_times_d_plus_e_plus_f, g_times_i_plus_j_squared)
a_plus_b = ExpressionNode("+", a, b)

expression_tree = ExpressionNode("*", a_plus_b, c_plus_g)

print("Expression Tree Representation:")
print(repr(expression_tree))