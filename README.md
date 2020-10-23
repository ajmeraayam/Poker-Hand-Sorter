# Poker-Hand-Sorter
 
To execute the code, you need python v3.6 or above. 
After installing python on the workstation, go to the directory where the python files are stored.
On Windows/Linux: 
<pre><code>cd ADDRESS_TO_THE_PYTHON_FILES
</code></pre>

The file ***PokerHands.py*** is the main file that will sort all the hands and return with the number of wins for each player for the given input file. To run the code, you must specify two parameters - input file and output file. You can point to the input file using *-i*. You can point where to store the file and the name of the file by using *-o*.

__Example:__
* If the input file is in different folder than the source code, then - 
<pre><code> -i ADDRESS-TO-THAT-FOLDER/NAME-OF-INPUT-FILE.txt 
</code></pre>

* If the input file is in same folder as the source code, then - 
<pre><code> -i NAME-OF-INPUT-FILE.txt 
</code></pre>

* If the output file should be stored in different folder than the source code, then - 
<pre><code> -o ADDRESS-TO-THAT-FOLDER/NAME-OF-OUTPUT-FILE.txt 
</code></pre>

* If the output file should be stored in same folder as the source code, then - 
<pre><code> -o NAME-OF-OUTPUT-FILE.txt 
</code></pre>

***Finally,***
<pre><code>python PokerHands.py -i poker-hands.txt -o output.txt
</code></pre>

The output of the program in the file will be the number of wins for each player for given input of poker hands:
<pre><code>Player1: xxx
Player2: xxx
</code></pre>

***NOTE*** - It is assumed that the input file will be formatted as
<pre><code>AH 9S 4D TD 8S 4H JS 3C TC 8D</code></pre>
where first 5 strings (excluding whitespaces) will be Player 1's hand and next 5 strings will be Player 2's hand for a given game. If the input is not formatted as mentioned then the program will not work according to the requirements. 