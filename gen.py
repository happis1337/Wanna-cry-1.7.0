def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# Пример использования
for num in float_range(0.5, 5.5, 0.5):
    print(num)

def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Пример использования
data = list(range(100))
for batch in batch_generator(data, 10):
    print(batch)

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib = fibonacci_sequence()
for _ in range(10):
    print(next(fib))

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Пример использования
for line in read_large_file('large_file.txt'):
    print(line)

