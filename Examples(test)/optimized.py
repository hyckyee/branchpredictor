import time
import branch_predictor
# 최적화된 피보나치 수 계산 (분기 예측기 사용) + 시간 측정
def fibonacci_optimized_timed(n, predictor, branch_id, cache={0: 0, 1: 1}):
    """
    분기 예측기를 사용하여 최적화된 피보나치 수를 계산하고, 소요 시간을 측정합니다.
    :param n: 피보나치 수의 인덱스
    :param predictor: BranchPredictor 객체
    :param branch_id: 분기 ID
    :param cache: 피보나치 수 캐시 (기본값은 0과 1)
    :return: n번째 피보나치 수, 소요 시간
    """
    predictor.register_branch(branch_id)  # 분기 ID 등록

    # 시간 시작
    start_time = time.time()

    # 분기 예측: n <= 1일 경우 예측된 값을 반환
    if n in cache:
        end_time = time.time()
        return cache[n], end_time - start_time

    # 분기 예측: n > 1일 경우 예측된 값 계산
    if predictor.predict(branch_id):  # 예측: 분기가 Taken(재귀 호출)일 것으로 예측
        cache[n] = fibonacci_optimized_timed(n - 1, predictor, branch_id, cache)[0] + fibonacci_optimized_timed(n - 2, predictor, branch_id, cache)[0]
    else:
        cache[n] = fibonacci_optimized_timed(n - 1, predictor, branch_id, cache)[0] + fibonacci_optimized_timed(n - 2, predictor, branch_id, cache)[0]
    
    # 실제 결과: 분기 실행 후 업데이트
    predictor.update(branch_id, actual_taken=(n > 1))

    # 시간 종료
    end_time = time.time()
    return cache[n], end_time - start_time


# 피보나치 수 계산 및 시간 측정
n = 900
branch_id = "fibonacci_branch"
predictor = branch_predictor.BranchPredictor()

result, elapsed_time = fibonacci_optimized_timed(n, predictor, branch_id)

# 결과 출력
print(f"Fibonacci({n}) = {result}")
print(f"계산 시간: {elapsed_time:.10f} 초")
