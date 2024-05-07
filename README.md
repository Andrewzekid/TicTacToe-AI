# TicTacToe-AI
TicTacToe AI made using MiniMax.

## How MiniMax Works
![a-move-tree-from-the-perspective-of-the-other-player-o](https://github.com/Andrewzekid/TicTacToe-AI/assets/79450923/7901eae0-6dc8-4142-8ea1-ebd02f3d3084)

### Minimax works by recursively considering the game's outcome after both you and your opponent plays the optimal moves.
* Minimax assigns one player, say X to be the maximizing player, whose goal is to maximize the score they get. The other player is the minimizing player, say O, who wants to minimize their score.
* For a given game, I define X wins as +10 points, O wins as -10 points, and a draw as 0 points. From O's perspective, it is ideal to choose moves that result in an outcome of a score as low as possible (preferring 0 points over +10 points) given optimal play on both sides.
* See the image above. On the turn of the minimizing player O, all possible moves are first considered by O. X's responses to those moves are also considered, and O's responses to those are considered until we reach a state where the game is over.
* As shown in the image, this process (of considering the opponents response to your response and then your response to that and so on) creates a tree-like structure. The different branches of this tree are parsed and we pick the move for O where, no matter what X does, results in the lowest possible score for O.

## Demonstration
<video width="300" src="https://github.com/Andrewzekid/TicTacToe-AI/assets/79450923/de404446-0c72-4a3a-8bbb-6598755c8369">






