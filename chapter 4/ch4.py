#Problem 1: Validate Email Addresses
1. import re

pattern = r'^[\w\.]+@[\w\.]+\.(com|org|edu)$'
emails = ["user@example.com", "bad-email", "test@domain.org"]

for email in emails:
if re.match(pattern, email):
print(f" Valid: {email}")
else:
print(f" Invalid: {email}")


#Problem 2: Extract Hashtags
import re

text = "I love #Python and #AI"
hashtags = re.findall(r'#\w+', text)
print(hashtags)




#Problem 3: Validate Phone Numbers
import re

pattern = r'^(\+\d-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'
phones = ["+1-555-1234", "123-456-7890", "5551234"]

for phone in phones:
    if re.match(pattern, phone):
        print(f" Valid: {phone}")
    else:
        print(f" Invalid: {phone}")



#Problem 4: Word Frequency
import re
from collections import Counter

text = "Python, Python! AI is great; Python AI."
words = re.findall(r'\b\w+\b', text.lower())
frequency = Counter(words)
print(dict(frequency))






#Problem 5: Find Duplicate Words
import re  
text = "This is is a test test"
duplicates = re.findall(r'\b(\w+)\s+\1\b', text)
print(duplicates)







#Problem 6: Extract Dates

import re

text = "The events are on 2023-05-12 and 2024-01-01."
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print(dates)


#Problem 7: Mask Sensitive Data
import re

text = "Card: 1234-5678-9012-3456"
masked = re.sub(r'\d(?=\d{4})', '*', text)
print(masked)




#Problem 8: Extract Programming Languages
import re
  
text = "I know Python, Java, and C++ but not Ruby."
languages = re.findall(r'\b[A-Za-z\+]+\b', text)
print(languages)
