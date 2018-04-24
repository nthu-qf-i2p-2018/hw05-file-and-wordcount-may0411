import csv
import json
import pickle
import string

def main(filename):
    lines = open("i_have_a_dream.txt").readlines()
    all_words =[]
    
    for line in lines:
        line = line.strip()
        words = line.split()    
        
        for word in words:
            word = word.strip(string.punctuation)
            all_words.append(word)        
            
            from collections import Counter
            word_counter = Counter(all_words)
            word_counter.most_common()
                
            with open('word_count.csv','w') as csv_file:
            # create a csv writer from a file object (or descriptor)
              writer = csv.writer(csv_file,delimiter=',')
            # write table head #only one line
              writer.writerow(['word', 'count'])
            # write all (word, count) pair into the csv writer
              writer.writerows(word_counter.most_common())

            json.dump(word_counter.most_common(), open('word_count.json','w'))

            pickle.dump(word_counter, open('word_count.pkl','wb'))


if __name__ == '__main__':
    main("i_have_a_dream.txt")
