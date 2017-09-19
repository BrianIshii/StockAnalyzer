import numpy as np

def OneD_array():
    print np.array([2,3,4])
def TwoD_array():
	print np.array([(2,3,4),(5,6,7)])
def empty_array():
    #print np.empty(5)
    #print np.empty((4,5))
    print np.empty((5,4,3))
def ones_array():
	print np.ones((5,4,3))
def random_array():
	print np.random.random((5,4))
def randInt_array():
    #print np.random.randint(10)
    #print np.random.randint(0,10)
    #print np.random.randint(0,10,size=5)
    print np.random.randint(0, 10, size=(2,3))

if __name__ == "__main__":
    #OneD_array()
    #TwoD_array()
    #empty_array()
    #ones_array()
    #random_array()
    #randInt_array()