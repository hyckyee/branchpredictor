# 분기 예측기

이 레포는 분기 예측기를 구현한 코드이다. 이 분기 예측기는 분기 예측 결과를 예측하고, 실제 결과를 바탕으로 예측 상태를 업데이트한다. 2비트 포화 카운터를 사용하여 분기의 결과(Taken 또는 Not Taken)를 예측한다.

## 기능

- 여러 분기 등록 및 관리
- 분기 예측 (Taken 또는 Not Taken)
- 실제 결과에 따른 예측 상태 업데이트
- 각 분기의 예측 상태 추적 및 출력

## 클래스: `BranchPredictor`

`BranchPredictor` 클래스는 분기 예측을 수행하고 실제 결과에 따라 예측 상태를 업데이트하는 기능을 제공한다. 2비트 포화 카운터를 사용하여 분기 예측을 진행한다.

### 메소드

- **`__init__(self, table_size=128)`**: 분기 예측기를 초기화한다. 기본값은 128이다.
- **`register_branch(self, branch_id)`**: 새로운 분기를 등록한다. `branch_id`는 고유한 분기 ID이다.
- **`predict(self, branch_id)`**: 특정 분기의 예측 결과를 반환한다. 예측 결과는 `True` (Taken) 또는 `False` (Not Taken)이다.
- **`update(self, branch_id, actual_taken)`**: 실제 분기 결과에 따라 예측 상태를 업데이트한다.
- **`get_state(self, branch_id)`**: 지정된 분기의 현재 상태를 반환한다. 상태는 0에서 3 사이의 값이다.

## 사용법

자세한 사용법은 [USAGE.md](USAGE.md) 파일에서 확인할 수 있다.
## 테스트
조건: 900까지의 피보나치 수열 연산   
(환경: Pentium Gold 7505, 8GB LPDDR4)   
일반 코드: 측정불가/(30까지 1초 이상 소요)   
단순 분기예측:0.0017576218초   
분기예측+행렬곱: 0.0000846386초   

## 라이선스

이 프로젝트는 MIT 라이선스 하에 제공됩니다. 자세한 사항은 [LICENSE](LICENSE) 파일을 참조하십시오.
