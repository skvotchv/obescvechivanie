import numpy as np

def nonlin(x, deriv = False):
	if(deriv == True):
           return(x * (1-x))

	return(1 / (1 + np.exp(-x)))
    
X = np.array([[0, 0, 1, 6, 4, 5, 1, 2, 4, 3],
            [0, 1, 1, 4, 2, 7, 4, 8, 8, 7],
            [1, 0, 1, 4, 6, 7, 1, 8, 2, 4],
            [1, 1, 1, 0, 1, 3, 7, 6, 7, 4]])

print(X)
               
y = np.array([[1],
			[3],
			[7],
			[9]])

print(y)

np.random.seed(1)



# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((10, 4)) - 1
syn1 = 2 * np.random.random((4, 4)) - 1
syn2 = 2 * np.random.random((4, 1)) - 1

print(syn0, syn1, syn2)

for j in range(20000):

	# проходим вперёд по слоям 0, 1, 2 и 3
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))

    # как сильно мы ошиблись относительно нужной величины?
    l3_error = y - l3
    
    if (j% 10000) == 0:
        print("Error:" + str(np.mean(np.abs(l3_error))))
        
    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l3_delta = l3_error * nonlin(l3, deriv=True)

    # как сильно значения l3 влияют на ошибки в l2?
    l2_error = l3_delta.dot(syn2.T)
    
    # в каком направлении нужно двигаться, чтобы прийти к l2?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta = l2_error * nonlin(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print(l2)
