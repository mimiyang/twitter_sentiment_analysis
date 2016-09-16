import sys
import json

def main():
 total=0
 tweet_amt={}

 with open(sys.argv[1]) as tweet1:
	for line in tweet1:
		data=json.loads(line)
		if "text" in data:
			ter1=data["text"]
			ter2=ter1.encode('ascii','ignore')
			ter3=ter2.split(" ")
			for a in ter3:
				total=total+1
			for b in ter3:
				if b in tweet_amt:
					tweet_amt[b] += 1
				else:
					tweet_amt.update({b:1})
 for keys in tweet_amt:
	n=float(tweet_amt[b])/total
	print (keys,n)

if __name__ == '__main__':
	main()
				
