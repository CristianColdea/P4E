"""
Exercise 6.5: Take a string 'X-DSPAM-Confidence:0.8475' and use find and slicing
to extract the portion of the string after the colon character and the use float
function to convert the extracted string into floating point number.
"""

str = 'X-DSPAM-Confidence:0.8475'

print(float(str[str.find(':')+1:]))
