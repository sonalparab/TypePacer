import json, requests, sys
reload(sys)
sys.setdefaultencoding('utf-8')


#Get the quote from the api
def getQuote():
    prompt = ""
    for x in range(0,3):
        url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en&?sig=" + str(x)
        r = requests.get(url)
        #r2 fixes errors about invalid escape characters
        r2 = r.text.replace('\\', '');
        d = json.loads(r2)
        #print d;
        prompt += d["quoteText"] + " "
    return prompt.replace("  ", " ")

#Split the quote into words by whitespace
def splitWords(quote):
    list = quote.split(' ')
    return list

print getQuote()

'''
s = splitWords("Hi there")
print s[0]
print s[0] == "Hi"
'''
