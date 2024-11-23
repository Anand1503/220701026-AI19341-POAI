def minimax(depth, nodeIndex, isMaximizingPlayer, scores, targetDepth):

    if depth == targetDepth:
        return scores[nodeIndex]

    if isMaximizingPlayer:
        return max(minimax(depth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:

        return min(minimax(depth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(depth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


if __name__ == "__main__":
    scores = [3, 5, 2, 9, 12, 5, 23, 23]

    targetDepth = 3

    optimalValue = minimax(0, 0, True, scores, targetDepth)
    print("The optimal value for the game is:", optimalValue)
