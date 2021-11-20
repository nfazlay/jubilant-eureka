import csv
import math

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

class Letter:
  """Class that reads input and parses data
  
  Attributes:
    raw: Stores the csv file as a list, ex ['0', 'X', 'G', ..].
    tPixels (int): Total number of pixels
    bPixels (int): Total number of black pixels
    tbPixels (int): Total number of Top Black Pixels
    lbPixels (int): Total number of Left Black Pixels
    propBlack (double): Proportion of black pixels
    topProp (double): Proportion of top Black pixels
    leftProp (double): Proportion of left Black pixels
    """
  def __init__(self, input_filepath):
    self.raw = self.parseFile(input_filepath)
    self.tPixels = len(self.raw)*len(self.raw[0])
    self.bPixels = None
    self.tbPixels = None
    self.lbPixels = None

    self.parseInfo()

    self.propBlack = self.bPixels/self.tPixels
    self.topProp = self.tbPixels/self.bPixels
    self.leftProp = self.lbPixels/self.bPixels

  def parseFile(self, input_filepath):
    """Opens the csv file and reads from it.
    
    Args:
      input_filepath (str): Path to csv file.
    """
    with open(input_filepath) as csvDataFile:
      csvReader = csv.reader(csvDataFile)
      return list(csvReader)
  
  def parseInfo(self):
    """Calculates the total number of black, top black and left black pixels"""
    bCounter = 0
    tbCounter = 0
    lbCounter = 0
    for i in range(len(self.raw)):
      for j in range(len(self.raw[i])):
        if self.raw[i][j] == "1":
          if i < len(self.raw)/2:#assumed upper bound for odd
            tbCounter += 1
          if j < len(self.raw[i])/2:
            lbCounter += 1
          bCounter += 1
    self.bPixels = bCounter
    self.tbPixels = tbCounter
    self.lbPixels = lbCounter
    
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

def fuzzyStuff(x,a,b,c,d):
  """Trapezoidial fuzzy membership function
  
  Calculates the value of f(x) given x
  
  Args:
    a,b,c,d (double): Points of Trapezium
    x (double): Proportion value
  
  Returns:
    F(x)
  """
  if x <= a:
    return 0
  elif x > a and x < b:
    return (x-a)/(b-a)
  elif x >= b and x <= c:
    return 1
  elif x > c and x < d:
    return (d-x)/(d-c)
  else:
    return 0

def s_norm(a, b):
  """Godel s_norm
  
  Args:
    a (double) : value to compare
    b (double) : value to compare

  Returns:
    Max of args

  """
  return max(a, b)

def t_norm(a, b):
  """Godel t_norm
  
  Args:
    a (double) : value to compare
    b (double) : value to compare

  Returns:
    Min or args

  """
  return min(a, b)


def fuzzy_classifier(input_filepath):
  """Recognize letters from black-and-white images using Naive Bayes
  
  Args:
    input_filepath (str): full file path to a CSV file containing a matrix representation of a black-and-white image

  Returns:
    most_likely_class (str) : String indicating the most likely class, either "A", "B", "C", "D", or "E"
    class_probabilities (:double: `list) : membership in each class in the order 
      [A value, B value, C value, D value, E value]
 """
  classArray = ['A', 'B', 'C', 'D', 'E']
  class_memberships = []
  input = Letter(input_filepath)

  #Calculating the fuzzy values
  propBlack_low = fuzzyStuff(input.propBlack, 0, 0, 0.3, 0.4)
  propBlack_med = fuzzyStuff(input.propBlack, 0.3, 0.4, 0.4, 0.5)
  propBlack_high = fuzzyStuff(input.propBlack, 0.4, 0.5, 1, 1)

  propTop_low = fuzzyStuff(input.topProp, 0, 0, 0.3, 0.4)
  propTop_med = fuzzyStuff(input.topProp, 0.3, 0.4, 0.5, 0.6)
  propTop_high = fuzzyStuff(input.topProp, 0.5, 0.6, 1, 1)

  propLeft_low = fuzzyStuff(input.leftProp, 0, 0, 0.3, 0.4)
  propLeft_med = fuzzyStuff(input.leftProp, 0.3, 0.4, 0.6, 0.7)
  propLeft_high = fuzzyStuff(input.leftProp, 0.6, 0.7, 1, 1)


  #For Each Class, calculate the stregth given rule
  for letter in classArray:
    match letter:
      case 'A':#IF PropBlack is Medium AND (TopProp is Medium OR LeftProp is Medium) THEN class A.
        ruleStrength = t_norm(propBlack_med, s_norm(propTop_med, propLeft_med))
        class_memberships.append(ruleStrength)
      case 'B':#IF PropBlack is High AND TopProp is Medium AND LeftProp is Medium THEN class B.
        ruleStrength = t_norm(propBlack_high, t_norm(propTop_med, propLeft_med))
        class_memberships.append(ruleStrength)
      case 'C':#IF (PropBlack is Low AND TopProp is Medium) OR LeftProp is High THEN class C.
        ruleStrength = s_norm(t_norm(propBlack_low, propTop_med), propLeft_high)
        class_memberships.append(ruleStrength)
      case 'D':#IF PropBlack is Medium AND TopProp is Medium AND LeftProp is High THEN class D.
        ruleStrength = t_norm(propBlack_med, t_norm(propTop_med, propLeft_high))
        class_memberships.append(ruleStrength)
      case 'E':#IF PropBlack is High AND TopProp is Medium AND LeftProp is High THEN class E.
        ruleStrength = t_norm(propBlack_high, t_norm(propTop_med, propLeft_high))
        class_memberships.append(ruleStrength)

  #argmax
  highest_membership_class = classArray[class_memberships.index(max(class_memberships))]

  return highest_membership_class, class_memberships