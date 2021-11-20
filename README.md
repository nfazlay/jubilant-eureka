# jubilant-eureka
## Recognizing letters from black-and-white images using a naïve Bayes classifier and a fuzzy classifier


### naïve_bayes_classifier
We calculate the normal distribution for each Class, given each value of Mean and s.d. We then multiply it with the probability of the Class. Let's call the product value. The most_likely_class is the maximum of the values, and the probabilities of each class is found by dividing the value with the sum of all the values.

- PropBlack: The proportion of pixels in the image that are black.
- TopProp: The proportion of the black pixels that are in the top half of the image.
- LeftProp: The proportion of the black pixels that are in the left half of the image.

| P( A ) = 0.28* | P( B ) = 0.05* | P( C ) = 0.10* | P( D ) = 0.15* | P( E ) = 0.42* |
|---------|---------------|-------|--------|-----|
| PropBlack: 𝜇 = 0.38, 𝜎 = 0.06 |PropBlack: 𝜇 = 0.51, 𝜎 = 0.06| PropBlack: 𝜇 = 0.31, 𝜎 = 0.06| PropBlack: 𝜇 = 0.39, 𝜎 = 0.06 | PropBlack: 𝜇 = 0.43, 𝜎 = 0.12 |
|TopProp: 𝜇 = 0.46, 𝜎 = 0.12|TopProp: 𝜇 = 0.49, 𝜎 = 0.12| TopProp: 𝜇 = 0.37, 𝜎 = 0.09 | TopProp: 𝜇 = 0.47, 𝜎 = 0.09 | TopProp: 𝜇 = 0.45, 𝜎 = 0.15 | 
|LeftProp: 𝜇 = 0.50, 𝜎 = 0.09 |LeftProp: 𝜇 = 0.57, 𝜎 = 0.09 | LeftProp: 𝜇 = 0.64, 𝜎 = 0.06 | LeftProp: 𝜇 = 0.57, 𝜎 = 0.03 | LeftProp: 𝜇 = 0.65, 𝜎 = 0.09 |
*The prior probability of each letter (following rough frequencies of use in the English language)

### fuzzy_classifier
We have a function FuzzyStuff that claculates the fuzzy membership function for each feature, given each fuzzy set and characteristic. The rule strength is then calculated for each rule using Godel t_norm and Godel s_norm (functions defined) , and the rule with the maximum strength is the highest_membership_class. 
###### The fuzzy membership functions are trapezoidal on the range [0, 1]  
The values for 𝑎, 𝑏, 𝑐, 𝑑 are given below for each fuzzy set and characteristic.
|PropBlack|TopProp|LeftProp|
|---------|--------|-------|
|Low: 𝑎 = 0, 𝑏 = 0, 𝑐 = 0.3, 𝑑 = 0.4|Low: 𝑎 = 0, 𝑏 = 0, 𝑐 = 0.3, 𝑑 = 0.4|Low: 𝑎 = 0, 𝑏 = 0, 𝑐 = 0.3, 𝑑 = 0.4|
|Medium: 𝑎 = 0.3, 𝑏 = 0.4, 𝑐 = 0.4, 𝑑 = 0.5|Medium: 𝑎 = 0.3, 𝑏 = 0.4, 𝑐 = 0.5, 𝑑 = 0.6| Medium: 𝑎 = 0.3, 𝑏 = 0.4, 𝑐 = 0.6, 𝑑 = 0.7| 
|High: 𝑎 = 0.4, 𝑏 = 0.5, 𝑐 = 1, 𝑑 = 1|High: 𝑎 = 0.5, 𝑏 = 0.6, 𝑐 = 1, 𝑑 = 1| High: 𝑎 = 0.6, 𝑏 = 0.7, 𝑐 = 1, 𝑑 = 1|

##### Rules

- IF PropBlack is Medium AND (TopProp is Medium OR LeftProp is Medium) THEN class A.
- IF PropBlack is High AND TopProp is Medium AND LeftProp is Medium THEN class B.
- IF (PropBlack is Low AND TopProp is Medium) OR LeftProp is High THEN class C.
- IF PropBlack is Medium AND TopProp is Medium AND LeftProp is High THEN class D.
- IF PropBlack is High AND TopProp is Medium AND LeftProp is High THEN class E.

##### Special thanks to our prof Mathew Holden, Fall 2021 CarletonU