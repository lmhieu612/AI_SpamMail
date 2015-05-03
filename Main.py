__author__ = 'madlife'
import sys


def read_input_and_train(filename,word_to_index,spam_likelihood,ham_likelihood,prior):
    fd = open(filename, 'r')
    line = fd.readline()
    count_ham = [0 for i in range(0, 100000)]
    count_spam = [0 for i in range(0, 100000)]
    last_of_list = 0
    num_of_email = 0
    num_of_spam_email = 0
    num_of_ham_email = 0
    while line != "":
        num_of_email += 1
        info = line.split(" ")
        class_ = info[1]
        if class_ == 'spam':
            num_of_spam_email += 1
        else:
            num_of_ham_email += 1
        for i in xrange(2, len(info), 2):
            if info[i] not in word_to_index:
                word_to_index[info[i]] = last_of_list
                index = last_of_list
                last_of_list += 1
            else:
                index = word_to_index[info[i]]
            if class_ == 'spam':
                count_spam[index] += int(info[i+1])
            else:
                count_ham[index] += int(info[i+1])
        line = fd.readline()



    for i in range(0,len(word_to_index)):
        spam_likelihood[i] = float(count_spam[i]) / float((count_spam[i] + count_ham[i]))
        ham_likelihood[i] = 1 - spam_likelihood[i]

    prior[0] = float(num_of_spam_email) / float((num_of_spam_email + num_of_ham_email))
    prior[1] = float(num_of_ham_email) / float((num_of_spam_email + num_of_ham_email))


    fd.close()

filename = '/home/madlife/PycharmProjects/SpamMail/spam/spam/data/train'

words_limit = 10000
word_to_index = {}
spam_likelihood = [0 for i in range(0,words_limit)]
ham_likelihood = [0 for i in range(0,words_limit)]
prior = [0, 0]
# prior = [ spam prior, ham prior]

read_input_and_train(filename, word_to_index, spam_likelihood, ham_likelihood, prior)
print len(word_to_index)
print word_to_index['need']
print spam_likelihood
print ham_likelihood
print prior

