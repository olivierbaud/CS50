

exp = input("Expression: ")

x, y, z = exp.split(" ")

match y:
    case "+":
        result = int(x) + int(z)
    case "-":
        result = int(x) - int(z)
    case "*":
        result = int(x) * int(z)
    case "/":
        result = int(x) / int(z)

print (f"{result:.1f}")
