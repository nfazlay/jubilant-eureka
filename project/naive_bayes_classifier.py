import math
import sys
sys.path.append(".")
from .modules.letter import Letter

def pdFunc(x,a,b):
  """Probability density function for Normal Distribution
  
  Args:
    x (double): The value to compare against
    a (double): The Mean
    b (int): The Standard Deviation
  
  Returns:
    the probability density
   """
  den = math.sqrt(2*math.pi*(b**2))
  y = (x-a)/b
  num = math.exp(-0.5*(y**2))
  return num/den
    
def naive_bayes_classifier(input_filepath):
  """Recognize letters from black-and-white images using Naive Bayes
  
  Args:
    input_filepath (str): full file path to a CSV file containing a matrix representation of a black-and-white image

  Returns:
    most_likely_class (str) : String indicating the most likely class, either "A", "B", "C", "D", or "E"
    class_probabilities (:double: `list) : Probability of each class in the order 
      [A probability, B probability, C probability, D probability, E probability]

  """
  classArray = ['A', 'B', 'C', 'D', 'E']
  class_probabilities = []
  input = Letter(input_filepath)

  #r probability of each letter (following rough frequencies of use in the English language):
  probabilities = {
    'A' : 0.28,
    'B' : 0.05,
    'C' : 0.10,
    "D" : 0.15,
    "E" : 0.42
  }

  # Calculating probability using Naive Bayes Classification
  for letter in classArray:
    match letter:
      case 'A':
        prob = pdFunc(input.propBlack, 0.38, 0.06) * pdFunc(input.topProp, 0.46, 0.12) * pdFunc(input.leftProp, 0.50, 0.09)
        class_probabilities.append(prob*probabilities['A'])
      case 'B':
        prob = pdFunc(input.propBlack, 0.51, 0.06) * pdFunc(input.topProp, 0.49, 0.12) * pdFunc(input.leftProp, 0.57, 0.09)
        class_probabilities.append(prob*probabilities['B'])
      case 'C':
        prob = pdFunc(input.propBlack, 0.31, 0.06) * pdFunc(input.topProp, 0.37, 0.09) * pdFunc(input.leftProp, 0.64, 0.06)
        class_probabilities.append(prob*probabilities['C'])
      case 'D':
        prob = pdFunc(input.propBlack, 0.39, 0.06) * pdFunc(input.topProp, 0.47, 0.09) * pdFunc(input.leftProp, 0.57, 0.03)
        class_probabilities.append(prob*probabilities['D'])
      case 'E':
        prob = pdFunc(input.propBlack, 0.43, 0.12) * pdFunc(input.topProp, 0.45, 0.15) * pdFunc(input.leftProp, 0.65, 0.09)
        class_probabilities.append(prob*probabilities['E'])

  #argmax
  most_likely_class = classArray[class_probabilities.index(max(class_probabilities))]
  
  den  = 0
  for i in range(len(classArray)):
    den += class_probabilities[i]#calculation summation

  for i in range(len(class_probabilities)):
    class_probabilities[i] =class_probabilities[i]/den



  return most_likely_class, class_probabilities

