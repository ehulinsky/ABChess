# ABChess
A chess AI written in python using alpha-beta search that is super slow and can only search about 4 moves ahead

### Alpha-Beta 
At first this was implemented with a normal minimax algorithm, but it was super slow, so slow that it took about 4-5 minutes to make a move when searching to a depth of four. With the alpha-beta algorithm, it takes about 10 seconds.

### Evaluation Function
The evaluation function I didn't even try on, I just looked up the relative values for chess pieces on Wikipedia. The evaluation function scores positions by running over all the pieces adding those values to the total if they are the computers and subtracts them if they are the players. The king is valued at 1000000 because that is greater than everything else combined.

### Problems
1.) When the computer can't find any way to capture something in 4 moves, it just picks the first move from the list, which is usally to move the rightmost rook back and forth. It doesn't understand the strategy at all, just the tactics. One way to fix this to is feed it knowlege of strategy through the evaluation function. But then this isn't even artificial intellegence, its a artificial instruction-follower (granted, they are not *as* specific instructions as normal computer programs)

2.) The interface is not user friendly, must type moves in in UCI and the ASCII is hard to look at.

3.) Its written in Python completely so its slooooowwww.
