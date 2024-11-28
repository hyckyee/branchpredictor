# 분기 예측기 사용법

이 문서는 Python 프로젝트에서 `BranchPredictor` 클래스를 어떻게 사용할 수 있는지 설명합니다.

## 1. 설치

1. 이 저장소를 클론하거나 `branch_predictor.py` 파일을 다운로드합니다.
2. `branch_predictor.py` 파일을 Python 프로젝트 디렉토리에 추가합니다.

## 2. 예시 코드

`BranchPredictor` 클래스를 사용하여 분기 예측을 시뮬레이션할 수 있습니다. 아래는 분기를 등록하고 예측하며, 실제 결과에 따라 상태를 업데이트하는 예시 코드입니다.

### 예시 코드

```python
from branch_predictor import BranchPredictor, branch_decision

# 새로운 분기 예측기 객체 생성
predictor = BranchPredictor()

# 고유 ID로 분기 등록
branch_id = "branch_1"
predictor.register_branch(branch_id)

# 분기 예측 및 상태 업데이트
# 예를 들어, 실제 결과가 'Taken' (True)이라고 가정
branch_decision(predictor, branch_id, actual_taken=True)

# 분기 결과가 'Not Taken' (False)인 경우 예시
branch_decision(predictor, branch_id, actual_taken=False)

# 분기 상태 확인
print(f"[{branch_id}] 최종 상태: {predictor.get_state(branch_id)}")
