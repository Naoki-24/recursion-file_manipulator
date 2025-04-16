import random

def main():
	while True:
		n = int(input("Min: "))
		m = int(input("Max: "))
		if n < m:
			break
	ans = random.randint(n, m)
	
	while True:
		user_input = int(input("Guess the number: "))
		if ans == user_input:
			print("You are Correct!")
			break
		print("You are wrong. Retry!")

if __name__=="__main__":
	main()
