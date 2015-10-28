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

#Euclidean Distance Score
def euc_distance(prefs,person1,person2):
	si={}
	s=0
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	#if person1 and person2 do not share any item, then return 0
	if len(si)==0:
		return 0
	#computing the difference between the sum of the squares	
	for item in si:
		s+=pow(prefs[person1][item]-prefs[person2][item],2)
	#1+sqrt(s) in order to avoid sqrt(s)==0
	return 1/(1+sqrt(s))

#print(euc_distance(critics,'Lisa Rose','Gene Seymour'))

#Pearson Correlation Score
def pearson_score(prefs,person1,person2):
	si={}
	sum1_s=0
	sum2_s=0
	sum1_sq=0
	sum2_sq=0
	sum1_mul=0

	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1
	n=len(si)
	if n == 0:
		return 1
	for item in si:
		#computing the sum of all preferences
		sum1_s+=prefs[person1][item]
		sum2_s+=prefs[person2][item]
		#ccomputing the sum of squares
		sum1_sq+=pow(prefs[person1][item],2)
		sum2_sq+=pow(prefs[person2][item],2)
		#computing the sum of multiply
		sum1_mul+=prefs[person1][item]*prefs[person2][item]
	#computing pearson value
	num=sum1_mul-(sum1_s*sum2_s/n)
	den=sqrt((sum1_sq-pow(sum1_s,2)/n)*(sum2_sq-pow(sum2_s,2)/n))
	if den==0:
		return 0
	return num/den

#print(pearson_score(critics,'Toby','Lisa Rose'))

#return the top matches
def Topmatches(prefs,person,n=5,similarity=pearson_score):
	scores=[]
	'''
	for other in prefs:
		if other != person:
			scores.append([(similarity(prefs,person,other),other)])
	'''
	scores = [(similarity(prefs,person,other), other) for other in prefs if other!=person]

	scores.sort()
	scores.reverse()
	return scores
#for person in critics:
#print(Topmatches(critics,'Toby'))

#make recommendations for someone based on others' ratings
def getRecommendations(prefs,person,similarity=pearson_score):
	totals={}
	simsum={}
	result={}
	for other in prefs:
		#not compare with self
		if other == person:
			continue
		sim=similarity(prefs,person,other)
		#ignore the rating is 0 or less than 0
		if sim <= 0:
			continue
		for item in prefs[other]:
			#only comment the moveis which someone has not watched
			if item in prefs[person]:
				continue
			#the sum of similarity	
			simsum.setdefault(item,0)
			simsum[item]+=sim
			#computing the score
			totals.setdefault(item,0)
			totals[item]+=prefs[other][item]*sim
	for item in totals:
		result.setdefault(item,0)
		result[item]=totals[item]/simsum[item]
	return result
#print(getRecommendations(critics,'Toby'))

#swap the item and person
def transform(prefs):
	si={}
	for person in prefs:
		for item in prefs[person]:
			si.setdefault(item,{})
			#swap the item and person
			si[item][person]=prefs[person][item]
	return si

#result1=transform(critics)
#print(getRecommendations(result1,'Just My Luck'))

#construct item comparsion data set
def calsimitems(prefs,n=10):
	result={}
	count=0
	#convert the preferences matrix around item
	itemprefs=transform(prefs)
	for item in itemprefs:
		count+=1
		if count % 100 ==0:
			print("%d / %d" %(count,len(itemprefs)))
		#search the most similar item
		scores=Topmatches(itemprefs,item,similarity=euc_distance)
		result[item]=scores
	return result
#print(calsimitems(critics))

#receive the recommendation items
def getrecomitems(prefs,person):
	scores={}
	simsum={}
	calsim={}
	result_scores={}
	#get the similarity
	calsim=calsimitems(prefs)
	for item in prefs[person]:
		for (sim,movie) in calsim[item]:
			#ignore to get the rating of item the person has
			if movie in prefs[person]:
				continue
			#computing the sum of similarity of movie
			simsum.setdefault(movie,0)
			simsum[movie]+=sim
			#computing the scores
			scores.setdefault(movie,0)
			scores[movie]+=sim*prefs[person][item]
	#get the final scores
	for movie in simsum:
		result_scores[movie]=scores[movie]/simsum[movie]
	return result_scores
#print(getrecomitems(critics,'Toby') )


