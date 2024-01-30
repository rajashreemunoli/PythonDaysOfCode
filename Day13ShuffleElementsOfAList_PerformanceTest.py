
import timeit

def random_shuffle(test_list):
	import random
	
	#print("The original list is : " + str(test_list))
 	# using random.shuffle() to shuffle a list
	return random.shuffle(test_list)
	print("The shuffled list is : " + str(test_list))

def random_sample(test_list):
	import random
	
	#print("The original list is : " + str(test_list))
 	# using random.sample()to shuffle a list
	return random.sample(test_list, len(test_list))
	print("The shuffled list is : " + str(res))

def permutations_shuffle(input_list):
	import random
	import itertools
 
	permutations = list(itertools.permutations(input_list))
	#shuffled_list = list(random.choice(permutations))
	return list(random.choice(permutations))
	#print("Input List:",input_list)
	print("Shuffled List:", shuffled_list)


# compute random shuffle time
def random_shuffle_time():
    SETUP_CODE = '''
from __main__ import random_shuffle
from random import randint'''
 
    TEST_CODE = '''
mylist = [x for x in range(10)]
find = randint(0, len(mylist))
random_shuffle(mylist)'''
 
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=1000)
 
    # printing minimum exec. time
    print('Random shuffle time: {}'.format(min(times)))


# compute random sample time
def random_sample_time():
    SETUP_CODE = '''
from __main__ import random_sample
from random import randint'''
 
    TEST_CODE = '''
mylist = [x for x in range(10)]
find = randint(0, len(mylist))
random_sample(mylist)'''
 
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=1000)
 
    # printing minimum exec. time
    print('Random sample time: {}'.format(min(times)))


def permutations_shuffle_time():
    SETUP_CODE = '''
from __main__ import permutations_shuffle
from random import randint'''
 
    TEST_CODE = '''
mylist = [x for x in range(10)]
find = randint(0, len(mylist))
permutations_shuffle(mylist)'''
 
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=1000)
 
    # printing minimum exec. time
    print('Permutations shuffle time: {}'.format(min(times)))


if __name__ == "__main__":
	test_list = [1, 4, 5, 6, 3]
	random_shuffle(test_list)
	random_sample(test_list)
	permutations_shuffle(test_list)
	random_shuffle_time()
	random_sample_time()
	permutations_shuffle_time()
