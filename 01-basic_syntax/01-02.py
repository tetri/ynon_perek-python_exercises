# Write a program that takes a file name as command line argument,
# count how many times each word appears in the file and prints the word that appears the most
# (and its relevant count)

import sys
import operator 
#import pprint
import time

def wordhistogram(path):
    file = open(path, mode='r', encoding='utf-8')
    text = file.read()

    list = []
    for line in text.split('\n'):
        for commas in line.split(','):
            for dots in commas.split('.'):
                for word in dots.split(' '):
                    if (len(word) > 0):
                        list.append(word)
    list.sort()

    dict = {}
    for word in list:
        dict[word] = dict.get(word, 0) + 1
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

def main(argv):
    h = wordhistogram(argv[0])
    #pprint.pprint(h)

    top = h[0]
    print(top)

if __name__ == "__main__":
    start_time = time.clock()
    main(sys.argv[1:])
    print("time: %ss" % (time.clock() - start_time))