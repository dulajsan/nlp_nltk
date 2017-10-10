import csv
import nltk

f = open('exp.csv')
csv_f = csv.reader(f)
csv_f.next()  #skip the header line

dataset = []

for row in csv_f:
    dataset.append(({'name1': row[0], 'name2': row[1]}, row[2]))

print (dataset)

classifier = nltk.NaiveBayesClassifier.train(dataset)

mydata = {'name1':'def', 'name2':'window'}
print (mydata, classifier.classify(mydata))