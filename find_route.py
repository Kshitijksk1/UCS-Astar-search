import sys

def readinput(filename):
    list = []
    file = open(filename,"r")
    for line in file:
        f = line.rstrip('\n').split(" ")
        list.append(f)
    for i in range(5):
        if list[-1] == ['END', 'OF', 'INPUT']  or  list [-1] == ['']:
            del list[-1]
    return list

def uni_search(data, start, end):
    c = set()
    g = 1
    f = [] 
    m = []
    e = []
    f.append([start, None, 0.0, 0])
    m.append([start, None, 0.0, 0])
    state = start
    done = False
    while not done:
        if not f:
            return False
        e.append(state)
        parent_cost = float(f[0][2])
        prev_depth = f[0][3]
        f.pop(0)
        if str(state) not in c:
            for i in data:
                if state in i:
                    g+=1
                    a =[data.index(i),i.index(state)]
                    if a[1] == 1:
                        gen = data[data.index(i)][0]
                        parent = state
                        depth = prev_depth +1
                        cc = parent_cost + float(data[data.index(i)][2])
                        f.append([gen, parent, cc, depth])
                        m.append([gen, parent, cc, depth])
                    elif a[1] == 0:
                        gen = data[data.index(i)][1]
                        parent = state
                        depth = prev_depth +1
                        cc = parent_cost + float(data[data.index(i)][2])  
                        f.append([gen, parent, cc, depth])
                        m.append([gen, parent, cc, depth])
        c.add(state)
        f = sorted(f,key=lambda x: x[2])
        if not f:
            d = "infinity"
            no_of_e = len(e)
        else:
            state = str(f[0][0])
            d = f[0][2]
            no_of_e = len(e) + 1
        if state == end or d == "infinity":
            show_output(no_of_e, g, d, m, start, end)
            done = True

def Astar_search(data, start, end, heuristic):
    c = set()
    g = 1
    f = [] 
    m = []
    e = []
    f.append([start, None, 0.0, 0, 0.0])
    m.append([start, None, 0.0, 0, 0.0])
    state = start
    done = False
    while not done:
        if not f:
            return False
        e.append(state)
        parent_cost = float(f[0][4])
        prev_depth = f[0][3]
        f.pop(0)
        if str(state) not in c:
            for i in data:
                if state in i:
                    g+=1
                    a =[data.index(i),i.index(state)]
                    if a[1] == 1:
                        gen = data[data.index(i)][0]
                        parent = state
                        depth = prev_depth +1
                        for j in heuristic:
                            if str(gen) in j:
                                h_cost = float(heuristic[heuristic.index(j)][1])
                        cost = parent_cost + float(data[data.index(i)][2])
                        cc = h_cost + parent_cost + float(data[data.index(i)][2])
                        f.append([gen, parent, cc, depth, cost])
                        m.append([gen, parent, cc, depth, cost])
                    elif a[1] == 0:
                        gen = data[data.index(i)][1]
                        parent = state
                        depth = prev_depth +1
                        for j in heuristic:
                            if gen in j:
                                h_cost = float(heuristic[heuristic.index(j)][1])
                        cost = parent_cost + float(data[data.index(i)][2])
                        cc = h_cost + parent_cost + float(data[data.index(i)][2])
                        f.append([gen, parent, cc, depth, cost])
                        m.append([gen, parent, cc, depth, cost])
        c.add(state)
        f = sorted(f,key=lambda x: x[2])
        if not f:
            d = "infinity"
            no_of_e = len(e)
        else:
            state = str(f[0][0])
            d = f[0][2]
            no_of_e = len(e) + 1

        if state == end or d == "infinity":
            show_output(no_of_e,g,d, m, start, end)
            done = True

def show_output(e, g, d, m, start, end):
    if d == "infinity":
        print("Nodes Expanded:", e)
        print("Nodes Generated:", g)
        print("Distance:", d)
        print("route:\nnone")
    else:
        print("Nodes Expanded:", e)
        print("Nodes Generated:", g)
        print("Distance:", d, "km")
        show_route(m, start, end, d)

def show_route(m, start ,end, d):
    r = []
    for i in m:
        if end in i and d in i:
            r.append(i)
    for i in range(r[0][3]-1):
        for j in m:
            if r:
                if r[-1][1] in j and r[-1][3] - 1 in j:
                    r.append(j)
    r.reverse()
    print("Route:")
    if no_of_args == 4:
        for i in range(len(r)):
            if i > 0:
                print(r[i][1],"to",r[i][0],",",r[i][2] - r[i-1][2],"km")
            else:
                print(r[i][1],"to",r[i][0],",",r[i][2],"km")    
    elif no_of_args == 5:
        for i in range(len(r)):
            if i > 0:
                print(r[i][1],"to",r[i][0],",",r[i][4] - r[i-1][4],"km")
            else:
                print(r[i][1],"to",r[i][0],",",r[i][4],"km")
    return None

args = sys.argv
data = readinput(str(args[1]))
start = str(args[2])
end = str(args[3])
no_of_args = len(args)
#print(arguments)
if no_of_args == 4:
    uni_search(data, start, end)

elif no_of_args == 5:
    heuristic = readinput(str(args[4]))
    Astar_search(data, start, end, heuristic)

elif no_of_args > 5:
    print("Wrong Number of Inputs")