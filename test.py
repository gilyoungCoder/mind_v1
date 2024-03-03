import torch
import torch.nn.functional as F
import math
# 확률 텐서 예시
prob_tensor = torch.tensor([0, 1/30, 0.5, 0.8])

# Sigmoid 함수 적용
higher_probs = torch.sigmoid(prob_tensor * 10-0.4)  # 스케일 조정을 통해 변화를 강화

print(higher_probs)

print(math.log(1/5))