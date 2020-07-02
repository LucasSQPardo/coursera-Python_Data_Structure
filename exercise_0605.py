#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
search = text.find(':')
number = text[search+1:] #no number after the : because i want to check until the end of the string 
number = number.strip()
number = float(number)

print(f'{number}')


