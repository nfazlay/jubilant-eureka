
def naive_bayes_classifier(input_filepath):
  # input is the full file path to a CSV file containing a matrix representation of a black-and-white image

  # most_likely_class is a string indicating the most likely class, either "A", "B", "C", "D", or "E"
  # class_probabilities is a five element list indicating the probability of each class in the order [A probability, B probability, C probability, D probability, E probability]
  return most_likely_class, class_probabilities


def fuzzy_classifier(input_filepath):
  # input is the full file path to a CSV file containing a matrix representation of a black-and-white image

  # highest_membership_class is a string indicating the highest membership class, either "A", "B", "C", "D", or "E"
  # class_memberships is a four element list indicating the membership in each class in the order [A value, B value, C value, D value, E value]
  return highest_membership_class, class_memberships