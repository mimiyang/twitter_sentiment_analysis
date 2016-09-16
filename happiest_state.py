import sys
import json
import operator

def main():

        states = {'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	
	scores = {}
	tweet_data = {}
	with open(sys.argv[1]) as f:
          for line in f:
		term, score = line.split("\t")
		scores[term] = int(score)

	with open(sys.argv[2]) as f2:
	   for line2 in f2:
		ter1 = json.loads(line2)
		td=0
		if "place" in ter1:
			if (td==0):
				ter2=ter1["place"]
				if (ter2 != None):
					ter3=ter2["country_code"]
					if (ter3 == "US"):
					   ter4=ter2["full_name"]
					   ter5=ter4.split(", ")
					   if (len(ter5)) > 1:
						    state=ter5[1]
					            if state == u'USA':
							for key, value in states.items():
								if ter5[0] == value:
									state = key
									
								
							
						    td=0
						    if "text" in ter1:
							tweet=ter1["text"]
							tweet2=tweet.encode('ascii','ignore')
							tweet3=tweet2.split(" ")
							for a in tweet3:
								if a in scores:
									td=td+scores.get(a)
						    if state in tweet_data:
							tweet_data[state]=(float(tweet_data[state])+td)/2
						    else:

							tweet_data.update({state:td})
	print max(tweet_data.iteritems(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
	main()
