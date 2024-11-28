# branch_predictor.py
class BranchPredictor:
    def __init__(self, table_size=128):
        """
        분기 예측기를 초기화합니다.
        :param table_size: 분기 테이블의 크기 (기본값: 128)
        """
        self.table_size = table_size
        self.history_table = [2] * table_size  # 초기 상태: 약간 Taken
        self.branch_map = {}  # 분기 ID -> 테이블 인덱스 매핑

    def register_branch(self, branch_id):
        """
        새로운 분기를 등록합니다.
        :param branch_id: 분기의 고유 ID (예: 함수 이름, 코드 위치)
        """
        if branch_id not in self.branch_map:
            self.branch_map[branch_id] = len(self.branch_map) % self.table_size

    def predict(self, branch_id):
        """
        특정 분기의 예측 결과를 반환합니다.
        :param branch_id: 분기의 고유 ID
        :return: True (Taken) 또는 False (Not Taken)
        """
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        return self.history_table[index] >= 2  # 2 이상이면 Taken 예측

    def update(self, branch_id, actual_taken):
        """
        분기의 실제 결과를 업데이트합니다.
        :param branch_id: 분기의 고유 ID
        :param actual_taken: 실제 결과 (True: Taken, False: Not Taken)
        """
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        if actual_taken:
            self.history_table[index] = min(3, self.history_table[index] + 1)  # 최대값 3
        else:
            self.history_table[index] = max(0, self.history_table[index] - 1)  # 최소값 0

    def get_state(self, branch_id):
        """
        특정 분기의 상태를 반환합니다.
        :param branch_id: 분기의 고유 ID
        :return: 분기의 현재 상태 (0~3 사이의 값)
        """
        if branch_id not in self.branch_map:
            raise ValueError(f"Branch ID '{branch_id}' is not registered.")
        index = self.branch_map[branch_id]
        return self.history_table[index]

# 분기 예측기를 코드 흐름에 삽입할 수 있는 함수
def branch_decision(predictor, branch_id, actual_taken):
    """
    분기 예측 및 결과 업데이트를 처리합니다.
    :param predictor: BranchPredictor 객체
    :param branch_id: 분기의 고유 ID
    :param actual_taken: 실제 결과 (True: Taken, False: Not Taken)
    :return: 예측 결과
    """
    prediction = predictor.predict(branch_id)
    print(f"[{branch_id}] 예측 결과: {'Taken' if prediction else 'Not Taken'}")
    
    # 실제 결과 업데이트
    predictor.update(branch_id, actual_taken)
    print(f"[{branch_id}] 업데이트된 상태: {predictor.get_state(branch_id)}")
    return prediction
