import sys
import json
import operator 


def main():
	
	tweet_data ={}
	count=1
	with open(sys.argv[1]) as f1:
		for line in f1:
			data=json.loads(line)
			total=0
			if "entities" in data:
				ter1=data["entities"]
				ht=ter1["hashtags"]
				for a in ht:
					ht2=a["text"]
					ht3=ht2.encode('ascii','ignore')
					if ht3 in tweet_data:
						tweet_data[ht3]+=1
					else:
						tweet_data.update({ht3:count})
		sorts = sorted(tweet_data.iteritems(),key=operator.itemgetter(1),reverse=True)
		k=0
		for b in sorts:
			k+=1
			if(k<=10):
				print b[0]+"\t"+str(b[1])

if __name__ == '__main__':
	main()
