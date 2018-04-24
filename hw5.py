import csv
import json
import string
import pickle

def main(filename):
    lines = open(filename).readlines()
    all_words = []
    
    for line in lines:
        line = line.strip()
        words = line.split()

        for word in words:
            word = word.strip(string.punctuation)
            if word : 
                all_words.append(word)

    from collections import Counter
    counter = Counter(all_words)
    counter.most_common()
    

    with open("wordcount.csv", "w", newline='') as csv_file :  
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(counter.most_common())
    
    json.dump(counter.most_common() , open("wordcount.json","w"))
 
    pickle.dump(counter, open("wordcount.pkl","wb"))

if __name__ == '__main__':
    main("i_have_a_dream.txt")
