from randHandles import RandHandles


#Example 
""" 
- country code: ISO 3166-1 alpha-3
- language code: https://developer.twitter.com/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages
"""

countries = ['Turkey']   
langs = ['tr']
fileNames = ['turkeyHandles.txt'] 
for i in range(len(countries)):         
    randHandles = RandHandles(countries[i], 10, 100, 5, langs[i], fileNames[i])
    randHandles.getHandles()