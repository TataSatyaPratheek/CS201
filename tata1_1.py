import csv

states= ['A', 'B', 'C', 'D', 'E','F']
paths = ['0', '1']
initial_state=['A']
final_states = ['F']
other_states = []

for i in states:
    if i not in final_states:
        other_states.append(i)

print("States:")
print(states)
print("Paths:")
print(paths)
print("Final states")
print(final_states)
print("Other states")
print(other_states)

print("Input:")
with open('function.csv', 'r') as file:
    data = csv.reader(file, delimiter =",")
    dfa_0 = {}
    dfa_1= {}
    next(data)
    for row in data:
        print(row)
        dfa_0[row[0]]=row[1]
        dfa_1[row[0]] = row[2]
    print("Transition state if path is 0:")
    print (dfa_0)
    print("Transition state if path is 1:")
    print (dfa_1)

dfa_ = [dfa_0,dfa_1] #and so on
n=len(dfa_0)

def dfa_state_vec(st):
    return [df[st] for df in dfa_]

def completely_equivalent(st1,st2):
    if dfa_state_vec(st1) == dfa_state_vec(st2):
        return True

def inSame(st1,st2, lst_states):
    if st1 == st2:
        return True
    else:
        for lst_state in lst_states:
            if (st1 in lst_state) and (st2 in lst_state):
                return True

def equivalent(st1,st2, lst_states):
    if completely_equivalent(st1,st2):
        return True
    else:
        if inSame(st1,st2,lst_states):
            for s1,s2 in zip(dfa_state_vec(st1), dfa_state_vec(st2)):
                if not inSame(s1,s2,lst_states):
                    return False
            return True
        else:
            return False

def make_up_artist(listOlist):
    first = [set(x) for x in listOlist]
    lst = []
    for x in first:
        if x not in lst:
            lst.append(x)
    lst_made_up = [list(x) for x in lst]
    return lst_made_up

def next_equi_list(prev_equi_list):        
    lst = []
    for sub_sts in prev_equi_list:
        if len(sub_sts) == 1:
            lst.append(sub_sts)
        else:
            for st1 in sub_sts:
                sub_sub_lst = [st1]
                for st2 in [x for x in sub_sts if x != st1]:
                    if equivalent(st1,st2, prev_equi_list):
                        sub_sub_lst.append(st2)
                lst.append(sub_sub_lst)
    return make_up_artist(lst)

# 0_equivalence
states_list_0 = [other_states, final_states]
print("After 0 Equivalence:")
print(states_list_0)

# 1_equivalence
states_list_n=next_equi_list(states_list_0)


# next equivalences
states_list_n1=[]
for i in range(n-2):
    states_list_n1 = next_equi_list(states_list_n)
    if(states_list_n1==states_list_n):    # same result for consecutive equivalences
        break
    states_list_n = states_list_n1.copy()  # preparing for next equivalence

print("Final result after the minimization of DFA:")
print(states_list_n)
states_copy=states_list_n.copy()

# For writing the equivalent states together (E.g- ['A','C'] as ['AC'])

for i in range(len(states_list_n)):
    st = ''
    if len(states_list_n[i])>1:
        for j in range(len(states_list_n[i])):
            st+=states_list_n[i][j]
        states_list_n[i]=[st]
print("Final result after the minimization of DFA: (writing equivalent states together)")
print(states_list_n)

# Output as CSV format
with open('output.csv', 'w', newline='') as file:  # str: the name of file
    writer = csv.writer(file)
    states.insert(0,"States")
    writer.writerow([states[i] for i in range(len(states))])

    paths.insert(0, "Paths")
    writer.writerow([paths[i] for i in range(len(paths))])

    initial_state.insert(0, "Initial states")
    writer.writerow([initial_state[0],initial_state[1]])

    final_states.insert(0, "Final states")
    writer.writerow([final_states[i] for i in range(len(final_states))])

    form=["States"]
    for i in range(1,len(paths)):
        form.append(f"transition state if path is {paths[i]}")

    writer.writerow([form[i] for i in range(len(form))])  # The first row of the file

    for i in range(0, len(states_list_n)):
        writer.writerow([states_list_n[i], dfa_0[states_copy[i][0]],dfa_1[states_copy[i][0]]])






