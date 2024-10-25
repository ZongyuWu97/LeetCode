class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            for order in range(n - 1 - 2 * layer):
                tmp = matrix[layer][layer + order]
                matrix[layer][layer + order] = matrix[n - 1 - layer - order][layer]
                matrix[n - 1 - layer - order][layer] = matrix[n - 1 - layer][
                    n - 1 - layer - order
                ]
                matrix[n - 1 - layer][n - 1 - layer - order] = matrix[layer + order][
                    n - 1 - layer
                ]
                matrix[layer + order][n - 1 - layer] = tmp
