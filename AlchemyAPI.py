'''
Created on Jun 12, 2014

@author: Debanjan Mahata
'''

__author__ = "Debanjan Mahata"

import requests
import sys

API_REQUEST_COUNT = 0

#Base URL for calling alchemyapi
BASE_URL = "http://access.alchemyapi.com/calls"
#Setup the endpoints
ENDPOINTS = {}

#setting up sntiment endpoint
ENDPOINTS['sentiment'] = {}
#endpoint for getting text sentiment from given url
ENDPOINTS['sentiment']['url'] = '/url/URLGetTextSentiment'
#endpoint for getting text sentiment from given text
ENDPOINTS['sentiment']['text'] = '/text/TextGetTextSentiment'
#endpoint for getting text sentiment from given html
ENDPOINTS['sentiment']['html'] = '/html/HTMLGetTextSentiment'


#setting up targeted sentiment endpoint
ENDPOINTS['sentiment_targeted'] = {}
#endpoint for getting targeted text sentiment from given url
ENDPOINTS['sentiment_targeted']['url'] = '/url/URLGetTargetedSentiment'
#endpoint for getting targeted text sentiment from given text
ENDPOINTS['sentiment_targeted']['text'] = '/text/TextGetTargetedSentiment'
#endpoint for getting targeted text sentiment from given html
ENDPOINTS['sentiment_targeted']['html'] = '/html/HTMLGetTargetedSentiment'


#setting up endpoint for author
ENDPOINTS['author'] = {}
#endpoint for extracting author from given url
ENDPOINTS['author']['url'] = '/url/URLGetAuthor'
#endpoint for extracting author from given html
ENDPOINTS['author']['html'] = '/html/HTMLGetAuthor'


#setting up keyword endpoint
ENDPOINTS['keywords'] = {}
#endpoint for getting ranked keywords from text of given url
ENDPOINTS['keywords']['url'] = '/url/URLGetRankedKeywords'
#endpoint for getting ranked keywords from text of given text
ENDPOINTS['keywords']['text'] = '/text/TextGetRankedKeywords'
#endpoint for getting ranked keywords from text of given html
ENDPOINTS['keywords']['html'] = '/html/HTMLGetRankedKeywords'


#setting up concept endpoints
ENDPOINTS['concepts'] = {}
#endpoint for getting ranked concepts from text of given url
ENDPOINTS['concepts']['url'] = '/url/URLGetRankedConcepts'
#endpoint for getting ranked concepts from text of given text
ENDPOINTS['concepts']['text'] = '/text/TextGetRankedConcepts'
#endpoint for getting ranked concepts from text of given html
ENDPOINTS['concepts']['html'] = '/html/HTMLGetRankedConcepts'


#setting up entity endpoints
ENDPOINTS['entities'] = {}
#endpoint for getting ranked entities from text of given url
ENDPOINTS['entities']['url'] = '/url/URLGetRankedNamedEntities'
#endpoint for getting ranked entities from text of given text
ENDPOINTS['entities']['text'] = '/text/TextGetRankedNamedEntities'
#endpoint for getting ranked entities from text of given html
ENDPOINTS['entities']['html'] = '/html/HTMLGetRankedNamedEntities'


#setting up category endpoints
ENDPOINTS['category'] = {}
#endpoint for getting categories from text of given url
ENDPOINTS['category']['url']  = '/url/URLGetCategory'
#endpoint for getting categories from text of given text
ENDPOINTS['category']['text'] = '/text/TextGetCategory'
#endpoint for getting categories from text of given html
ENDPOINTS['category']['html'] = '/html/HTMLGetCategory'


#setting up relation endpoints
ENDPOINTS['relations'] = {}
#endpoint for extracting relationship between entities from text of given url
ENDPOINTS['relations']['url']  = '/url/URLGetRelations'
#endpoint for extracting relationship between entities from text of given text
ENDPOINTS['relations']['text'] = '/text/TextGetRelations'
#endpoint for extracting relationship between entities from text of given html
ENDPOINTS['relations']['html'] = '/html/HTMLGetRelations'


#setting up language endpoints
ENDPOINTS['language'] = {}
#endpoint for detecting the language of the text in the given url
ENDPOINTS['language']['url']  = '/url/URLGetLanguage'
#endpoint for detecting the language of the text in the given text
ENDPOINTS['language']['text'] = '/text/TextGetLanguage'
#endpoint for detecting the language of the text in the given html
ENDPOINTS['language']['html'] = '/html/HTMLGetLanguage'


#setting up text endpoints
ENDPOINTS['text_clean'] = {}
#endpoint for extracting text from given url
ENDPOINTS['text_clean']['url']  = '/url/URLGetText'
#endpoint for extracting text from html
ENDPOINTS['text_clean']['html'] = '/html/HTMLGetText'


#setting up raw text endpoints
ENDPOINTS['text_raw'] = {}
#endpoint for extracting raw text from a given url
ENDPOINTS['text_raw']['url']  = '/url/URLGetRawText'
#endpoint for extracting raw text from a given html
ENDPOINTS['text_raw']['html'] = '/html/HTMLGetRawText'


#setting up text title endpoints
ENDPOINTS['text_title'] = {}
#endpoint for extracting the title of text present in a given url
ENDPOINTS['text_title']['url']  = '/url/URLGetTitle'
#endpoint for extracting text title of text present in a html doc
ENDPOINTS['text_title']['html'] = '/html/HTMLGetTitle'


#setting up feeds endpoint
ENDPOINTS['feeds'] = {}
#endpoint for extracting feed links from a given url
ENDPOINTS['feeds']['url']  = '/url/URLGetFeedLinks'
#endpoint for extracting feed links from a given html doc
ENDPOINTS['feeds']['html'] = '/html/HTMLGetFeedLinks'


#setting up microformat endpoints
ENDPOINTS['microformats'] = {}
#endpoint for extracting microformats from a given url
ENDPOINTS['microformats']['url']  = '/url/URLGetMicroformatData'
#endpoint for extracting microformats from given html doc
ENDPOINTS['microformats']['html'] = '/html/HTMLGetMicroformatData'

API_KEY = ""
OUTPUT_MODE = 'json'

def setApiKey():
    """It loads the API key from api_key.txt"""
    global API_KEY
    try:
        fp = open("api_key.txt")
        API_KEY = fp.readline()
        if API_KEY == "":
            print("The api_key.txt file appears to be blank, please run: python alchemyapi.py YOUR_KEY_HERE")
            print("If you do not have an API Key from AlchemyAPI, please register for one at: http://www.alchemyapi.com/api/register.html")
            sys.exit(0)
        else:
            if len(API_KEY) != 40:
                print('It appears that the key in api_key.txt is invalid. Please make sure the file only includes the API key, and it is the correct one.')
                sys.exit(0)
                
        fp.close()
    except IOError:
        print('API Key not found! Please create and fill up api_key.txt file in the same directory which contains the AlchemyAPI module')
        print('If you do not have an API Key from AlchemyAPI, please register for one at: http://www.alchemyapi.com/api/register.html')
        sys.exit(0)
    except Exception as e:
        print(e)


def setOutputMode(outputMode):
    """sets the output mode to one of xml/json/rdf. The default is json"""
    global OUTPUT_MODE
    OUTPUT_MODE = outputMode
    
def sentiment(flavor, data, options={}):
    """
    Calculates the sentiment for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/sentiment-analysis/
    For the docs, please refer to: http://www.alchemyapi.com/api/sentiment-analysis/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    showSourceText -> 0: disabled (default), 1: enabled

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """
    global API_REQUEST_COUNT
    setApiKey()
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['sentiment']:
        return { 'status':'ERROR', 'statusInfo':'sentiment analysis for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["sentiment"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
#        print r.url
        API_REQUEST_COUNT +=1
        
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text
        
    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }
    


def sentiment_targeted(self, flavor, data, target, options={}):
    """
    Calculates the targeted sentiment for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/sentiment-analysis/
    For the docs, please refer to: http://www.alchemyapi.com/api/sentiment-analysis/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    target -> the word or phrase to run sentiment analysis on.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    showSourceText    -> 0: disabled, 1: enabled

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()

    #Make sure the target is valid
    if target is None or target == '':
        return { 'status':'ERROR', 'statusInfo':'targeted sentiment requires a non-null target' }

    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['sentiment_targeted']:
        return { 'status':'ERROR', 'statusInfo':'targeted sentiment analysis for ' + flavor + ' not available' }
        
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["sentiment"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
#        print r.url
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }




def author(self, flavor, data, options={}):
    """
    Extracts the author from a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/author-extraction/
    For the docs, please refer to: http://www.alchemyapi.com/api/author-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.

    Availble Options:
    none

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """
    
    global API_REQUEST_COUNT
    setApiKey()
    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['author']:
        return { 'status':'ERROR', 'statusInfo':'author extraction for ' + flavor + ' not available' }

    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["author"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
#        print r.url
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }





def keywords(self, flavor, data, options={}):
    """
    Extracts the keywords from text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/keyword-extraction/
    For the docs, please refer to: http://www.alchemyapi.com/api/keyword-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
            
    Available Options:
    keywordExtractMode -> normal (default), strict
    sentiment -> analyze sentiment for each keyword. 0: disabled (default), 1: enabled. Requires 1 additional API transaction if enabled.
    showSourceText -> 0: disabled (default), 1: enabled.
    maxRetrieve -> the max number of keywords returned (default: 50)

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """
    global API_REQUEST_COUNT
    setApiKey()
    
    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['keywords']:
        return { 'status':'ERROR', 'statusInfo':'keyword extraction for ' + flavor + ' not available' }

    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["keywords"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }
    



        
def concepts(self, flavor, data, options={}):
    """
    Tags the concepts for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/concept-tagging/
    For the docs, please refer to: http://www.alchemyapi.com/api/concept-tagging/ 
    
    Available Options:
    maxRetrieve -> the maximum number of concepts to retrieve (default: 8)
    linkedData -> include linked data, 0: disabled, 1: enabled (default)
    showSourceText -> 0:disabled (default), 1: enabled

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """
    global API_REQUEST_COUNT
    setApiKey()    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['concepts']:
        return { 'status':'ERROR', 'statusInfo':'concept tagging for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["concepts"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }


        

def entities(self, flavor, data, options={}):
    """
    Extracts the entities for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/entity-extraction/ 
    For the docs, please refer to: http://www.alchemyapi.com/api/entity-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    disambiguate -> disambiguate entities (i.e. Apple the company vs. apple the fruit). 0: disabled, 1: enabled (default)
    linkedData -> include linked data on disambiguated entities. 0: disabled, 1: enabled (default) 
    coreference -> resolve coreferences (i.e. the pronouns that correspond to named entities). 0: disabled, 1: enabled (default)
    quotations -> extract quotations by entities. 0: disabled (default), 1: enabled.
    sentiment -> analyze sentiment for each entity. 0: disabled (default), 1: enabled. Requires 1 additional API transction if enabled.
    showSourceText -> 0: disabled (default), 1: enabled 
    maxRetrieve -> the maximum number of entities to retrieve (default: 50)

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey() 
    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['entities']:
        return { 'status':'ERROR', 'statusInfo':'entity extraction for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["entities"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }



def category(self, flavor, data, options={}):
    """
    Categorizes the text for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/text-categorization/
    For the docs, please refer to: http://www.alchemyapi.com/api/text-categorization/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    showSourceText -> 0: disabled (default), 1: enabled

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey() 
    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['category']:
        return { 'status':'ERROR', 'statusInfo':'text categorization for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["category"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }



def relations(self, flavor, data, options={}):
    """
    Extracts the relations for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/relation-extraction/ 
    For the docs, please refer to: http://www.alchemyapi.com/api/relation-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    sentiment -> 0: disabled (default), 1: enabled. Requires one additional API transaction if enabled.
    keywords -> extract keywords from the subject and object. 0: disabled (default), 1: enabled. Requires one additional API transaction if enabled.
    entities -> extract entities from the subject and object. 0: disabled (default), 1: enabled. Requires one additional API transaction if enabled.
    requireEntities -> only extract relations that have entities. 0: disabled (default), 1: enabled.
    sentimentExcludeEntities -> exclude full entity name in sentiment analysis. 0: disabled, 1: enabled (default)
    disambiguate -> disambiguate entities (i.e. Apple the company vs. apple the fruit). 0: disabled, 1: enabled (default)
    linkedData -> include linked data with disambiguated entities. 0: disabled, 1: enabled (default).
    coreference -> resolve entity coreferences. 0: disabled, 1: enabled (default)  
    showSourceText -> 0: disabled (default), 1: enabled.
    maxRetrieve -> the maximum number of relations to extract (default: 50, max: 100)

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()
    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['relations']:
        return { 'status':'ERROR', 'statusInfo':'relation extraction for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["relations"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }



def language(self, flavor, data, options={}):
    """
    Detects the language for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/api/language-detection/ 
    For the docs, please refer to: http://www.alchemyapi.com/products/features/language-detection/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.

    Available Options:
    none

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """


    global API_REQUEST_COUNT
    setApiKey()

    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['language']:
        return { 'status':'ERROR', 'statusInfo':'language detection for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["language"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }



def text_clean(self, flavor, data, options={}):
    """
    Extracts the cleaned text (removes ads, navigation, etc.) for text, a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/text-extraction/
    For the docs, please refer to: http://www.alchemyapi.com/api/text-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    useMetadata -> utilize meta description data, 0: disabled, 1: enabled (default)
    extractLinks -> include links, 0: disabled (default), 1: enabled.

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()

    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['text_clean']:
        return { 'status':'ERROR', 'statusInfo':'clean text extraction for ' + flavor + ' not available' }

    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["text_clean"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }
    



def text_raw(self, flavor, data, options={}):
    """
    Extracts the raw text (includes ads, navigation, etc.) for a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/text-extraction/ 
    For the docs, please refer to: http://www.alchemyapi.com/api/text-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    none

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()

    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['text_raw']:
        return { 'status':'ERROR', 'statusInfo':'raw text extraction for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["text_raw"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text

    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }




def text_title(self, flavor, data, options={}):
    """
    Extracts the title for a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/text-extraction/ 
    For the docs, please refer to: http://www.alchemyapi.com/api/text-extraction/
    
    INPUT:
    flavor -> which version of the call, i.e. text, url or html.
    data -> the data to analyze, either the text, the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    useMetadata -> utilize title info embedded in meta data, 0: disabled, 1: enabled (default) 

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """


    global API_REQUEST_COUNT
    setApiKey()

    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['text_title']:
        return { 'status':'ERROR', 'statusInfo':'title extraction for ' + flavor + ' not available' }
    

    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["text_title"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text
    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }



def microformats(self, flavor, data, options={}):
    """
    Parses the microformats for a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/microformats-parsing/
    For the docs, please refer to: http://www.alchemyapi.com/api/microformats-parsing/
    
    INPUT:
    flavor -> which version of the call, i.e.  url or html.
    data -> the data to analyze, either the the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.
    
    Available Options:
    none

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()

    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['microformats']:
        return { 'status':'ERROR', 'statusInfo':'microformat extraction for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["microformats"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text
    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }




def feeds(self, flavor, data, options={}):
    """
    Detects the RSS/ATOM feeds for a URL or HTML.
    For an overview, please refer to: http://www.alchemyapi.com/products/features/feed-detection/ 
    For the docs, please refer to: http://www.alchemyapi.com/api/feed-detection/
    
    INPUT:
    flavor -> which version of the call, i.e.  url or html.
    data -> the data to analyze, either the the url or html code.
    options -> various parameters that can be used to adjust how the API works, see below for more info on the available options.

    Available Options:
    none

    OUTPUT:
    The response, already converted from JSON to a Python object. 
    """

    global API_REQUEST_COUNT
    setApiKey()


    
    #Make sure this request supports this flavor
    if flavor not in ENDPOINTS['feeds']:
        return { 'status':'ERROR', 'statusInfo':'feed detection for ' + flavor + ' not available' }
    
    payload = {}
    payload[flavor] = data
    payload["outputMode"] = OUTPUT_MODE
    payload["apikey"] = API_KEY
    
    for option in options:
        payload[option] = options[option]
        

    getUrl = BASE_URL+ENDPOINTS["feeds"][flavor]
    
    try:
        r = requests.get(getUrl,params=payload)
        API_REQUEST_COUNT +=1
        if OUTPUT_MODE == "json":
            return eval(r.text)
        else:
            return r.text
    except Exception as e:
        print("Error for URL: ", r.url)
        print(e)
        return { 'status':'ERROR', 'statusInfo':r.status_code }


    
    


    