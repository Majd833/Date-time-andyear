import random
import time
def getRandomDate(startDate,endDate):
    print("I will choose a random date between", startDate,"and",endDate)
    randomgenerator=random.random()
    dateformat= '%m/%d/%Y'
    start=time.mktime(time.strptime(startDate*dateformat))
    end=time.mktime(time.strptime(endDate*dateformat))
