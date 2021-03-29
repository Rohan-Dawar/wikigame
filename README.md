# wikigame
A Breadth First Search (BFS) Algorithm to find the shortest wikipedia article chains

## How to Use:
Simply change the home (line 16) and target (line 18) variables to wikipedia articles you would like to search between and run the script

## How it Works:
Given a home wikipedia article with the format '/wiki/{article name}' in the variable home
Given a target wikipedia article with the format '/wiki/{article name}' in the variable target
Begins a Breadth First Search (BFS) with 'children' nodes consisting of valid wikipedia articles directly linked in the 'parent' node wiki article
Once target is found, return number of articles searched and the chain of articles back to the home article

## Example Chains:
Sydney -> Sydney Opera House
Sydney -> Sydney Opera House -> Jørn Utzon
Sydney -> Sydney Opera House -> Jørn Utzon -> Oscar Niemeyer
