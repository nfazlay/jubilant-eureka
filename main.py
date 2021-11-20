import sys
sys.path.append(".")
from project.fuzzy_classifier import fuzzy_classifier
from project.naive_bayes_classifier import naive_bayes_classifier

print(fuzzy_classifier("./Examples/Example0/input.csv"))
print(fuzzy_classifier("./Examples/Example2/input.csv"))
print(fuzzy_classifier("./Examples/Example4/input.csv"))

print(naive_bayes_classifier("./Examples/Example0/input.csv"))
print(naive_bayes_classifier("./Examples/Example2/input.csv"))
print(naive_bayes_classifier("./Examples/Example4/input.csv"))