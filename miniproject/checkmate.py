def checkmate(board) :
    board_lst = []

    for row in board.splitlines() :
        board_lst.append(list(row.strip()))

    for row in board_lst :
        if len(row) != len(board_lst) :
            print("Invalid Board")
            return

    board_size = len(board_lst)

    # find King
    k_pos = None
    for i in range(board_size) :
        for j in range(board_size) :
            if board_lst[i][j] == "K" :
                k_pos = (i, j)
                break
        
        if k_pos :
            break

    if not k_pos :
        print("No King in the board")
        return

    k_pos_x, k_pos_y = k_pos

    # in board or not
    def in_bounds(x, y):
        return 0 <= x < board_size and 0 <= y < board_size
    
    # Rook and Queen for up down left right
    rook_dir = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in rook_dir:
        x, y = k_pos_x + dx, k_pos_y + dy
        while in_bounds(x, y):
            if board_lst[x][y] != '.':
                if board_lst[x][y] in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Bishop and Queen for diagonal
    bi_dir = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    for dx, dy in bi_dir:
        x, y = k_pos_x + dx, k_pos_y + dy
        while in_bounds(x, y):
            if board_lst[x][y] != '.':
                if board_lst[x][y] in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Pawn for up diagonal
    pawn_dir = [(1, 1), (1, -1)]
    for dx, dy in pawn_dir:
        x, y = k_pos_x + dx, k_pos_y + dy
        if in_bounds(x, y) and board_lst[x][y] == 'P':
            print("Success")
            return

    print("Fail")