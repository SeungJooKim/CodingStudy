# 10 자물쇠와 열쇠
def attach(keyi, keyj, M, key, board):
    for i in range(M):
        for j in range(M):
            board[keyi + i][keyj + j] += key[i][j]


def detach(keyi, keyj, M, key, board):
    for i in range(M):
        for j in range(M):
            board[keyi + i][keyj + j] -= key[i][j]


def issolved(N, M, board):
    for i in range(N):
        for j in range(N):
            if board[i + M - 1][j + M - 1] == 0 or board[i + M - 1][j + M - 1] == 2:
                return False
    return True


def rotate_90(key):
    rkey = [[0] * len(key) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            rkey[j][len(key) - 1 - i] = key[i][j]
    return rkey


def solution(key, lock):  # M <= N
    M = len(key)  # 키
    N = len(lock)  # 자물쇠
    # big board
    board = [[0] * (M * 2 + N - 2) for _ in range(M * 2 + N - 2)]

    for i in range(N):
        for j in range(N):
            board[i + M - 1][j + M - 1] = lock[i][j]
    # print(board)

    for _ in range(4):
        for keyi in range(M + N - 2 + 1):
            for keyj in range(M + N - 2 + 1):
                attach(keyi, keyj, M, key, board)
                if issolved(N, M, board):
                    return True
                detach(keyi, keyj, M, key, board)
                # rotate_90
        key = rotate_90(key)

    return False