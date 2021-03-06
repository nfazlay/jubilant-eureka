# jubilant-eureka
## Recognizing letters from black-and-white images using a naΓ―ve Bayes classifier and a fuzzy classifier


### naΓ―ve_bayes_classifier
We calculate the normal distribution for each Class, given each value of Mean and s.d. We then multiply it with the probability of the Class. Let's call the product value. The most_likely_class is the maximum of the values, and the probabilities of each class is found by dividing the value with the sum of all the values.

- PropBlack: The proportion of pixels in the image that are black.
- TopProp: The proportion of the black pixels that are in the top half of the image.
- LeftProp: The proportion of the black pixels that are in the left half of the image.

| P( A ) = 0.28* | P( B ) = 0.05* | P( C ) = 0.10* | P( D ) = 0.15* | P( E ) = 0.42* |
|---------|---------------|-------|--------|-----|
| PropBlack: π = 0.38, π = 0.06 |PropBlack: π = 0.51, π = 0.06| PropBlack: π = 0.31, π = 0.06| PropBlack: π = 0.39, π = 0.06 | PropBlack: π = 0.43, π = 0.12 |
|TopProp: π = 0.46, π = 0.12|TopProp: π = 0.49, π = 0.12| TopProp: π = 0.37, π = 0.09 | TopProp: π = 0.47, π = 0.09 | TopProp: π = 0.45, π = 0.15 | 
|LeftProp: π = 0.50, π = 0.09 |LeftProp: π = 0.57, π = 0.09 | LeftProp: π = 0.64, π = 0.06 | LeftProp: π = 0.57, π = 0.03 | LeftProp: π = 0.65, π = 0.09 

*The prior probability of each letter (following rough frequencies of use in the English language)

### fuzzy_classifier
We have a function FuzzyStuff that claculates the fuzzy membership function for each feature, given each fuzzy set and characteristic. The rule strength is then calculated for each rule using Godel t_norm and Godel s_norm (functions defined) , and the rule with the maximum strength is the highest_membership_class. 
###### The fuzzy membership functions are trapezoidal on the range [0, 1]  
The values for π, π, π, π are given below for each fuzzy set and characteristic.
|PropBlack|TopProp|LeftProp|
|---------|--------|-------|
|Low: π = 0, π = 0, π = 0.3, π = 0.4|Low: π = 0, π = 0, π = 0.3, π = 0.4|Low: π = 0, π = 0, π = 0.3, π = 0.4|
|Medium: π = 0.3, π = 0.4, π = 0.4, π = 0.5|Medium: π = 0.3, π = 0.4, π = 0.5, π = 0.6| Medium: π = 0.3, π = 0.4, π = 0.6, π = 0.7| 
|High: π = 0.4, π = 0.5, π = 1, π = 1|High: π = 0.5, π = 0.6, π = 1, π = 1| High: π = 0.6, π = 0.7, π = 1, π = 1|

##### Rules

- IF PropBlack is Medium AND (TopProp is Medium OR LeftProp is Medium) THEN class A.
- IF PropBlack is High AND TopProp is Medium AND LeftProp is Medium THEN class B.
- IF (PropBlack is Low AND TopProp is Medium) OR LeftProp is High THEN class C.
- IF PropBlack is Medium AND TopProp is Medium AND LeftProp is High THEN class D.
- IF PropBlack is High AND TopProp is Medium AND LeftProp is High THEN class E.

##### Special thanks to our prof Mathew Holden, Fall 2021 CarletonU