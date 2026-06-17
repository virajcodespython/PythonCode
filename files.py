def print_numbers(limit):
	for number in range(1, limit + 1):
		print(f"Number: {number}")


def sum_numbers(limit):
	total = 0
	current = 1

	while current <= limit:
		total += current
		current += 1

	return total


def main():
	limit = 5

	print("Basic loop demo")
	print_numbers(limit)
	print(f"Sum from 1 to {limit}: {sum_numbers(limit)}")


if __name__ == "__main__":
	main()
