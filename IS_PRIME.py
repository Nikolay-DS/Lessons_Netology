def is_prime(x):
	n = 2
	while True:
		if x > 3 and n < x:            
			if x % n == 0:
				return False
				break
			else:
				n += 1
				continue
		elif x < 2:
			return False        
		elif x == 2 or x == 3:
			return True
			break
		else:
			return True
for x in range(21):			
    print(is_prime(x), x)