from functions import getNNvalues, NNpredict

values = getNNvalues("IL", "White", 2000.0, "Male")
print(NNpredict(values))
