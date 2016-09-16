import oauth2 as oauth
import urllib2 as urllib

# See assignment1.html instructions or README for how to get these credentials

api_key ="aeYb6V9WmHhtsB3bjwmmPWyGg"
api_secret = "x82UiiGV5xF8WcJl7j2v4PqNprEZYN6GD5mzIaem4Ke4GpxL6D"
access_token_key = "757433613218484225-GtDwCJ4O2duT2Rrx2h9PI4L1pPILWt6"
access_token_secret = "tjrIXHzpv7o9T014O1lthzKCemLQGoaGMvCXhyrSfPujf"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1.1/statuses/sample.json"
  parameters = []
  n = 0
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()
if __name__ == '__main__':
 
        fetchsamples()
        print "]"
