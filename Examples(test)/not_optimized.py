def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 피보나치 수 계산
n = 50
result = fibonacci(n)
print(f"Fibonacci({n}) = {result}")
