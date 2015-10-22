# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

#Euclidean distance score
def sim_distance(prefs,person1,person2):
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	#if person1 and person2 do not have any share item
	if len(si) == 0:
		return 0
	#computing 
	sum_of_squares = 0
	for item in prefs[person1]:
		if item in prefs[person2]:
			sum_of_squares += pow(prefs[person1][item]-prefs[person2][item],2)

	return 1/(1+sqrt(sum_of_squares))

#Pearson Correlation Score
def sim_pearson(prefs,person1,person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
	n = len(si)
	if n == 0:
		#if there is no share item,return 1
		return 1
	sum1 = sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])

	sum1_sq = sum([pow(prefs[person1][item],2) for item in si])
	sum2_sq = sum([pow(prefs[person2][item],2) for item in si])

	sum_multipy = sum([prefs[person1][item] * prefs[person2][item] for item in si])

	#computing pearson score
	num = sum_multipy - (sum1 * sum2/n)
	den = sqrt((sum1_sq - pow(sum1, 2)/n) * (sum2_sq - pow(sum2, 2)/n))
	if den == 0:
		return 0

	r = num/den
	return r

def matches(prefs,person,n=5,similarity=sim_pearson):
	scores = [(similarity(prefs,person,other), other) for other in prefs if other!=person]
	scores.sort()
	scores.reverse()
	return scores[0:n]

def make_recommendations(prefs,person,similarity=sim_pearson):
	totals = {}
	simsum = {}
	for other in prefs:
		if other == person:
			continue
		#get the similarity	
		sim = similarity(prefs,person,other)
		if sim <= 0:
			continue
		#sum score and similarity sum
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item] == 0:
				totals.setdefault(item,0)
				totals[item] += prefs[other][item] * sim 
				simsum.setdefault(item,0)
				simsum[item] += sim
	#sum score/similarity score			
	ranking = [(total/simsum[item],item) for item, total in totals.items()]
	ranking.sort()
	ranking.reverse()
	return ranking
#get all Euclidean Distance Score and Pearson Correlation Score
person = []
for k in critics:
	person.append(k)
print(person)
for i in range(len(person)):
	#k=i+1
	for k in range(i+1,len(person)):
		print(person[i], person[k], sim_distance(critics,person[i],person[k]))
		print(person[i], person[k], sim_pearson(critics,person[i],person[k]))

#get matches
for k in critics:
	print(k,matches(critics,k))

#make recommendations
for k in critics:
	print('recommendations:')
	print(k,make_recommendations(critics,k))

