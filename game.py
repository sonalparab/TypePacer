import json, requests

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Get the quote from the api
def getQuote():
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    r = requests.get(url)
    d = r.json()
    return d["quoteText"]

#Split the quote into words by whitespace
def splitWords(quote):
    list = quote.split(' ')
    return list

print splitWords(getQuote())

'''
s = splitWords("Hi there")
print s[0]
print s[0] == "Hi"
'''
