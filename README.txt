This is a modified Python API for AlchemyAPI (http://alchemyapi.com). I used to use the Python SDK given in their website. But, I thought
of writing a simpler version with an easy to use interface. The modified API has the following changes: 

1. Function for setting the format in which the response is obtained (JSON/XML/RDF) with the default being the JSON  format. 
2. The API is dependent on an external python module called requests (https://github.com/kennethreitz/requests).
The request library makes it simpler and easier to handle the GET requests sent to AlchemyAPI server and to parse its response. 
This provides more control to the user. Note: you can install the requests module by simply using the command
easy_install requests if you have setuptools set. For more information and instructions refer to https://github.com/kennethreitz/requests
3. The error messages has been made more informative. 
4. The API also adds a counter in order to track the number of requests sent to the AlchemyAPI server.
This helps in controlling the limits imposed.
5. The responses are obtained as a Python dictionary if one chooses to use json as the output format.

The API does not have all the features. Currently, it has the following capabilities:

1. Sentiment analysis at document level, entity specific, and for targeted named entity
2. Detect named entities from text, url and html.
3. Detect keywords from text, url and html.
4. Author of a url or a html document.
5. Concepts from text, url and html.
6. Category of a text, url and html.
7. Language of the text, url and html.
8. Cleaned text from a url and html.
9. Raw text from a url and html.
10. Feeds from url, html.
11. Microformats from url, html.

For more information please refer to http://alchemyapi.com

The documentation for the AlchemyAPI REST api could be found at http://www.alchemyapi.com/api/
Check out for the available options or parameters that needs to be passed to the fucntions.