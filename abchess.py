import chess
import copy

class ChessState:
    def __init__(self):
        self.board=chess.Board()

    def getMoves(self):
        return list(self.board.legal_moves)

    def result(self,move):
        s=ChessState()
        s.board=copy.copy(self.board)
        s.board.push(move)
        return s
    

    def gameResult(self):
        #returns "1-0", "0-1" or "1/2-1/2" (or "*" if the game is not over)
        return self.board.result()


    #this is not the evaluation function: it just returns 1, 0, or -1
    #for who won
    def score(self):
        result=self.board.result()
        if result=="1-0":
            return 1
        elif result=="0-1":
            return -1
        elif result=="1/2-1/2":
            return 0
        elif result=='*':
            return None #?

    def evaluate(self):
        pieces=self.board.piece_map()
        values={
            chess.KING:1000000,
            chess.QUEEN:9,
            chess.ROOK:5,
            chess.BISHOP:3,
            chess.KNIGHT:3,
            chess.PAWN:1
            }
        total=0
        for p in pieces.values():
            multiplier=1
            if p.color==chess.BLACK:
                multiplier=-1
            total+=multiplier*values[p.piece_type]
        return total
                    

    def isWhitesTurn(self):
        return self.board.turn
    
    def print(self):
        print('   a b c d e f g h\n')
        rank=8
        for row in str(self.board).split('\n'):
            print(str(rank)+'  '+row)
            rank-=1

state=ChessState()
state.print()

def minimax(state,depth):
    results=[]
    if depth==0:
       return (state.score() or 0,None)
    
    if len(state.getMoves())==0 or state.score()==1 or state.score()==-1:
        return (state.score(),None)

    elif state.isWhitesTurn():
        bestScore=float('-inf')
        for m in state.getMoves():
            nextScore=minimax(state.result(m),depth-1)[0]
            if nextScore>bestScore:
                bestScore=nextScore
                nextMove=m
        return (bestScore,nextMove)
    elif not state.isWhitesTurn():
        bestScore=bestScore=float('inf')
        for m in state.getMoves():
            nextScore=minimax(state.result(m),depth-1)[0]
            if nextScore<bestScore:
                bestScore=nextScore
                nextMove=m
        return (bestScore,nextMove)

def getPlayerMove(state):
    print('enter move')
    while True:
        uci_move=input()

        try:
            move=chess.Move.from_uci(uci_move)
        except ValueError:
            print("Invalid move. Try again.")
            continue
        
        if move in state.getMoves():
            return move
        else:
            print("Illegal move. Try again.")

total=0

def alphabeta(state, depth, alpha, beta):
    global total
    if depth==0 or len(state.getMoves())==0:
        total+=1
        return (state.evaluate(),None)
    if state.isWhitesTurn():
        value=float("-inf")
        for m in state.getMoves():
            childScore=alphabeta(state.result(m), depth-1, alpha, beta)[0]
            if childScore>value:
                value=childScore
                nextMove=m
            alpha = max(alpha, value)
            if alpha >= beta:
                break #β cut-off
        return (value,nextMove)
    else:
        value=float("inf")
        for m in state.getMoves():
            childScore=alphabeta(state.result(m), depth-1, alpha, beta)[0]
            if childScore<value:
                value=childScore
                nextMove=m
            beta = min(beta, value)
            if alpha >= beta:
                break #α cut-off
        return (value,nextMove)

def winnerOrTie(state):
    score=state.score()
    if state.score()==None:
        return False
    else:
        if score==0:
            print("Tie")
        elif score==1:
            print("You win!")
        elif score==-1:
            print("MWAA-HA-HA!!! YOU LOSE!!!")
        return True

while True:
    state=state.result(getPlayerMove(state))
    state.print()
    if winnerOrTie(state):
        break
    print('Thinking...')
    total=0
    state=state.result(alphabeta(state,4,float("-inf"),float("inf"))[1])
    state.print()
    print(str(total)+" nodes examined")
    if winnerOrTie(state):
        break
