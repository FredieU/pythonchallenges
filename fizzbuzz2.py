def fizzbuzz(n, m1, m2):
	for i in range(1, n+1):
		if i % m1 == 0 and i % m2 == 0:
			print("FizzBuzz!")
		elif i % m1 == 0:
			print("Fizz!")
		elif i % m2 == 0:
			print("Buzz!")
		else:
			print(i)
			
if __name__ == "__main__":
	fizzbuzz(100, 3, 5)
