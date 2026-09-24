def checkmate(board):
    if not isinstance(board, str):
        print("Error")
        return

    rows = board.split('\n')
    if rows and rows[-1] == "":
        rows = rows[:-1]

    N = len(rows)
    if N == 0:
        print("Error")
        return

    for row in rows:
        if len(row) != N:
            print("Error")
            return

    king_pos = None
    for r in range(N):
        for c in range(N):
            if rows[r][c] == 'K':
                if king_pos is not None:
                    print("Error")
                    return
                king_pos = (r, c)

    if king_pos is None:
        print("Error")
        return

    kr, kc = king_pos

    pieces = {'K', 'Q', 'R', 'B', 'P'}

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
        r, c = kr + dr, kc + dc
        step = 1

        while 0 <= r < N and 0 <= c < N:
            char = rows[r][c]
            if char in pieces:
                if dr == 0 or dc == 0:
                    if char in ['R', 'Q']:
                        print("Success")
                        return
                else:
                    if char in ['B', 'Q']:
                        print("Success")
                        return
                    if char == 'P' and step == 1 and dr == 1:
                        print("Success")
                        return
                break

            r += dr
            c += dc
            step += 1

    print("Fail")
