import time

class BranchPredictor:
    def __init__(self, table_size=128):
        self.table_size = table_size
        self.history_table = [2] * table_size  # 초기 상태: 약간 Taken
        self.branch_map = {}  # 분기 ID -> 테이블 인덱스 매핑

    def register_branch(self, branch_id):
        if branch_id not in self.branch_map:
            self.branch_map[branch_id] = len(self.branch_map) % self.table_size

    def predict(self, branch_id):
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        return self.history_table[index] >= 2  # 2 이상이면 Taken 예측

    def update(self, branch_id, actual_taken):
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        if actual_taken:
            self.history_table[index] = min(3, self.history_table[index] + 1)  # 최대값 3
        else:
            self.history_table[index] = max(0, self.history_table[index] - 1)  # 최소값 0

    def get_state(self, branch_id):
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        return self.history_table[index]

# 행렬 곱셈 함수
def matrix_mult(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]

# 행렬 거듭제곱 함수 (분기 예측 적용)
def matrix_power_optimized(M, n, predictor, branch_id):
    """
    행렬 거듭제곱을 최적화하여 계산합니다. 분기 예측기를 사용하여 효율적인 계산을 합니다.
    :param M: 기본 행렬
    :param n: 거듭제곱할 지수
    :param predictor: 분기 예측기
    :param branch_id: 분기 ID
    :return: M^n
    """
    predictor.register_branch(branch_id)  # 분기 ID 등록
    
    # 분기 예측: n이 홀수인지 짝수인지에 대한 예측
    if n == 1:
        return M

    if predictor.predict(branch_id):  # 예측: 분기가 짝수일 것으로 예측
        half = matrix_power_optimized(M, n // 2, predictor, branch_id)
        result = matrix_mult(half, half)
    else:  # 예측: 분기가 홀수일 것으로 예측
        half = matrix_power_optimized(M, (n - 1) // 2, predictor, branch_id)
        result = matrix_mult(matrix_mult(half, half), M)
    
    # 실제 결과 업데이트
    predictor.update(branch_id, actual_taken=(n % 2 == 0))

    return result

# 시간 측정을 위한 함수
def fibonacci_matrix_with_predictor(n, predictor, branch_id):
    start_time = time.time()
    
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_power_optimized(base_matrix, n - 1, predictor, branch_id)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    return result_matrix[0][0], elapsed_time

# 피보나치 수 계산 및 시간 측정
n = 900
branch_id = "matrix_power_branch"
predictor = BranchPredictor()

result, elapsed_time = fibonacci_matrix_with_predictor(n, predictor, branch_id)

# 결과 출력
print(f"Fibonacci({n}) = {result}")
print(f"계산 시간: {elapsed_time:.10f} 초")
