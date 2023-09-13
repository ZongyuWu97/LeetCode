from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist
import numpy as np


class Solution:
  def minimumMoves(self, M: List[List[int]]) -> int:
    data_from, data_to = [], []
    for i in range(3):
      for j in range(3):
        if M[i][j] == 0:
          data_to.append((i, j))
        elif M[i][j] > 1:
          data_from.extend([(i, j)] * (M[i][j] - 1))

    cost = cdist(data_from, data_to, metric='cityblock')
    row_ind, col_ind = linear_sum_assignment(cost)
    return int(cost[row_ind, col_ind].sum())