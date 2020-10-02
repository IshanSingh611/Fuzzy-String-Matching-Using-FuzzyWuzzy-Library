#import package
from fuzzywuzzy import process

'''
fetch data of indian cities
from the file
'''
with open("d:\\indian_cities_data.txt") as f:
    cities = f.read().split("\n")

'''
store the result by using 
extractbests method with
cutoff = 90 and limit = 5
'''
results = process.extractBests("abad",
                               cities,
                               score_cutoff=90,
                               limit=5)
#show results
print(results)