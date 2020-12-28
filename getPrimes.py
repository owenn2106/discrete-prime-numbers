def getprimes(x):
	primes = []

	# Loop through 9999 possible prime numbers
	for a in range(2, 10000000):

		# Loop through every number it could divide by
		for b in range(2, a):

			# Does b divide evenly into a ?
			if a % b == 0:
				break

		# Loop exited without breaking ? (It is prime)
		else:
			# Add the prime number to our list
			primes.append(a)

		# We have enough to stop ?
		if len(primes) == x:
			return primes

print(getprimes(1000000))
