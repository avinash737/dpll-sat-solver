import sys

def parse_dimacs(filename):
	clauses = []
	with open(sys.argv[1], 'r') as input_file:
		for line in input_file:
			if line[0] in ['c', 'p']:
				continue
			literals = list(map(int, line.split()))
			assert literals[-1] == 0
			literals = literals[:-1]
			clauses.append(literals)
	return clauses

clauses = parse_dimacs(sys.argv[1])

trail=[]

def BCP():
    v=True
    for i in clauses:
        for j in i:
            if(((j,v,False) not in trail) or ((j,v,True) not in trail)):
                if(j>0):
                    trail.append(j,v,False)
                else:
                    trail.append(j,not v, False)
            for k in trail:
                if(k[1] is not True) then sat=False
            if(not sat) then return False
    return True

def decide():
    if() then return False
	choose unassigned var x
	choose val c from {0,1}
	trail.append(clauses[i][j],v,False)
	return True

def backtrack():
	while(True)
	if(trail.empty()) then return False
	trail.pop(clauses[i][j],v,b)
	if(not b):
     then trail.append(clauses[i][j],not v,True) 
     return True

def DPLL(clauses):
    trail.clear()
    if(not BCP()) then exit(20)
    while(True) if(not decide()) then exit(10)
    while(not BCP()) if(not backtrack()) then exit(20)

print(clauses)

