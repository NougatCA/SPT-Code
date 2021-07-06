from .tokenizer import TokeNizer

TN = TokeNizer("Python")

code = [["a=0", "if a.isEmpty():"], ["print(\"hello\")"], [
    """
    a= b
    b=c
    c=0
    """]]
print(TN.getPureTokens(code[2][0]))
