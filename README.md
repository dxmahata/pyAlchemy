This is a modified Python API for AlchemyAPI (http://alchemyapi.com). I used to use the Python SDK given in their website. But, I thought
of writing a simpler version with an easy to use interface. The changes are all directed towards myy ease of use. I have been using Alchemy API
for information extraction tasks. The modified API has the following changes:

1. Added function for setting the respnse format (JSON/XML/RDF) with the default being the JSON  format. 

2. Requests module is used for making the GET requests. the module could be obtained from (https://github.com/kennethreitz/requests).
The request library makes it simpler and easier to handle the GET requests sent to AlchemyAPI server and to parse its response. This provides more control to the
user. In order to install requests type easy_install requests in the command line or sudo easy_install requests, if setuptools is installed. For more information
please consult https://github.com/kennethreitz/requests

3. The error messages have been made more informative. 

4 A counter is added in order to track the number of requests sent to the AlchemyAPI server. This helps in controlling the limits imposed.

5. When the response format is set to JSON then a python dictionary is returned. This makes it easier to parse and store the response as Python objects.



The API does not have all the features. Currently, it has the following capabilities:

1. Sentiment analysis at document level, named entity specific, and for targeted named entity
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

The documentation for the AlchemyAPI REST api could be found at http://www.alchemyapi.com/api/. Check out for the available options.
