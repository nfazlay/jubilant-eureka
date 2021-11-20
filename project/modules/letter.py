import csv
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