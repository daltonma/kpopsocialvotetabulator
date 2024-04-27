# K-Pop Social Voting Tabulator

This is a script to process ballots for song collection. 

Ballots should be a csv file called `ballots.csv` and should contain the following structure:

```csv
Choice 1, Choice 2, Choice 3
```


`choices.list` should be a file containing a list of valid choices, where each line is a string containing a distinct choice.

example:
```
Bite Me - ENHYPEN
LALALALA - Stray Kids
Halazia - ATEEZ
Bite Me - ENHYPEN
Maniac - Stray Kids
Oh Mymy : 7s - TWS
Given-Taken - ENHYPEN
```

**This repo STANs ENHYPEN**

## Usage
Create the `ballots.csv` and `choices.list` as described above.

Then run `python tabulatevotes.py` and your results should appear.


## Examples
```csv
Choice 1, Choice 2, Choice 3
Halazia - ATEEZ,Maniac - Stray Kids,Seven - Jungkook
Case 143 - Stray Kids,LALALALA - Stray Kids,Bite Me - ENHYPEN
Given-Taken - ENHYPEN,Oh Mymy : 7s - TWS,Bite Me - ENHYPEN
We Don't Sweat - xikers,Case 143 - Stray Kids,Halazia - ATEEZ
Given-Taken - ENHYPEN,plot twist - TWS,_WORLD - SEVENTEEN
Halazia - ATEEZ,Maniac - Stray Kids,Seven - Jungkook
```

Result:

![an example text, decorative](image.png)

