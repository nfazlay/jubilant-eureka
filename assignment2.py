import csv


class Letter:
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

    # print(self.propBlack)
    # print(self.topProp)
    # print(self.leftProp)

  def parseFile(self, input_filepath):
    """Opens the csv file and reads from it.
    
    Args:
      input_filepath (str): Path to csv file.
    """
    with open(input_filepath) as csvDataFile:
      csvReader = csv.reader(csvDataFile)
      return list(csvReader)
  
  def parseInfo(self):
    bCounter = 0
    tbCounter = 0
    lbCounter = 0
    for i in range(len(self.raw)):
      for j in range(len(self.raw[i])):
        if self.raw[i][j] == "1":
          if i > len(self.raw)/2:#assumed upper bound for odd
            tbCounter += 1
          if j > len(self.raw[i])/2:
            lbCounter += 1
          bCounter += 1
    self.bPixels = bCounter
    self.tbPixels = bCounter - tbCounter
    self.lbPixels = bCounter - lbCounter


l = Letter("Examples\Example0\input.csv")
  







# def naive_bayes_classifier(input_filepath):
#   # input is the full file path to a CSV file containing a matrix representation of a black-and-white image

#   # most_likely_class is a string indicating the most likely class, either "A", "B", "C", "D", or "E"
#   # class_probabilities is a five element list indicating the probability of each class in the order [A probability, B probability, C probability, D probability, E probability]
#   return most_likely_class, class_probabilities


# def fuzzy_classifier(input_filepath):
#   # input is the full file path to a CSV file containing a matrix representation of a black-and-white image

#   # highest_membership_class is a string indicating the highest membership class, either "A", "B", "C", "D", or "E"
#   # class_memberships is a four element list indicating the membership in each class in the order [A value, B value, C value, D value, E value]
#   return highest_membership_class, class_memberships