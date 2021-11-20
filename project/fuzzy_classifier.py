import math
import sys
sys.path.append(".")
from .modules.letter import Letter

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