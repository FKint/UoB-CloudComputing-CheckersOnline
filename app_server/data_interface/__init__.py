"""
game: {
    whitePlayerId:
    blackPlayerId:
    gameStates: [{
        timestamp: <...>
        state: <...>
    }]
    gameName: <...>
}

gamestate: {
    black_regular: [(row, col)]
    black_kings: [(row, col)]
    white_regular: [(row, col)]
    white_kings: [(row, col)]
}
"""
def get_game_status(game_id):
    return {
        "turn": 0,
        "black_regular": [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2),
                          (2, 3)],
        "black_kings": [],
        "white_regular": [(7, 0), (7, 1), (7, 2), (7, 3), (6, 0), (6, 1), (6, 2), (6, 3), (5, 0), (5, 1), (5, 2),
                          (5, 3)],
        "white_kings": []
    }
