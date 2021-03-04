Kshitij Khaladkar
Readme for the code find_route.py

The code uses UCS for uninformed search and A* for informed search
In uni_search method:
We create a data structure related to UCS and find the expanded nodes and the cost for the search
In Astar_search method:
We create a data structure for A* and find the expanded nodes and cost with the heuristic value.

To run the code:
For UCS:
python find_route.py input1.txt Bremen Kassel
For A*:
python find_route.py input1.txt Bremen Kassel h_kassel.txt
