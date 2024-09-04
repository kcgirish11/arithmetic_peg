from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

# Define the PEG grammar for basic arithmetic expressions with addition, subtraction, multiplication, and division
grammar = Grammar(
    """
    expr    = term (addsub term)*
    term    = factor (muldiv factor)*
    factor  = number
    addsub  = ("+" / "-")
    muldiv  = ("*" / "/")
    number  = ~"[0-9]+(\.[0-9]+)?"
    """
)

# NodeVisitor class to evaluate the parsed expression
class ArithmeticVisitor(NodeVisitor):
    def visit_expr(self, node, visited_children):
        term, rest = visited_children[0], visited_children[1]
        result = term
        for operator, next_term in rest:
            if operator == '+':
                result += next_term
            elif operator == '-':
                result -= next_term
        return result

    def visit_term(self, node, visited_children):
        factor, rest = visited_children[0], visited_children[1]
        result = factor
        for operator, next_factor in rest:
            if operator == '*':
                result *= next_factor
            elif operator == '/':
                result /= next_factor
        return result

    def visit_factor(self, node, visited_children):
        return visited_children[0]  # Return the number

    def visit_addsub(self, node, visited_children):
        return node.text.strip()  # Return '+' or '-'

    def visit_muldiv(self, node, visited_children):
        return node.text.strip()  # Return '*' or '/'

    def visit_number(self, node, visited_children):
        return float(node.text)  # Convert number text to float

    def visit_ws(self, node, visited_children):
        # Ignore whitespace; return nothing
        pass

    def generic_visit(self, node, visited_children):
        return visited_children or node

# Function to parse and evaluate an arithmetic expression
def evaluate(expression):
    tree = grammar.parse(expression)
    return ArithmeticVisitor().visit(tree)

# Example usage
expression = "3+5*2-8/4"
result = evaluate(expression)
print(f"The result of '{expression}' is {result}")
