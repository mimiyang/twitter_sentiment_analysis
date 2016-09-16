import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    scores = {}
    tweet_data = []

    with open(sys.argv[2]) as data_file:
        for line in data_file:

                tweet_data.append(json.loads(line))

    with open(sys.argv[1]) as f:
    	for line in f:
		(term, score) = line.split("\t")
		scores[term] = int(score)
    print scores
    for e in tweet_data:
	sum=0
	if "text" in e:
		tweet=e["text"]
		tweet1=tweet.encode('ascii','ignore')
		ter=tweet1.split(" ")
		for a in ter:
			if a in scores:
				sum = sum + scores.get(a)
		print sum

		
if __name__ == '__main__':
    main()
