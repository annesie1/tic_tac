import random

def get_empty_board():
    return [['.' for i in range(3)] for i in range(3)]

def get_human_coordinates():

def get_menu_option():
    while True:
        print("Wybierz tryb gry:")
        print("1.Gra dla 2 graczy")
        print("2.Gra przeciwko AI")
        choice = input("Wybierz (1 lub 2): ")
        if choice in ['1', '2']:
            return choice
        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")

def get_winning_player(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!='.':
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i]!='.':
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2]!='.':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!='.':
        return board[0][2]
    return None


winner = get_winning_player(board)
if winner:
    display_board(board)
    print(f"{winner} wygral!")
    break

if is_board_full(board):
    display_board(board)
    print("To remis!")
    break