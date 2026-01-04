import copy

objs = ["人", "狼", "羊", "菜"]
state = [0, 0, 0, 0]  
path = []
visited_map = set() 

def is_dead(s):
    if s[1] == s[2] and s[1] != s[0]:
        return True

    if s[2] == s[3] and s[2] != s[0]:
        return True
    return False

def check_add(next_list, s):
    if not is_dead(s):
        next_list.append(s)


def move(s, obj_idx):
    new_s = s[:]  
    side = s[0]
    another_side = 1 if side == 0 else 0
    
    new_s[0] = another_side       
    new_s[obj_idx] = another_side 
    return new_s

def neighbors(s):
    side = s[0]
    next_list = []
    
    check_add(next_list, move(s, 0))

    for i in range(1, len(s)):
        if s[i] == side:
            check_add(next_list, move(s, i))
            
    return next_list

def get_state_key(s):
    return "".join(map(str, s))

def visited(s):
    return get_state_key(s) in visited_map

def is_success(s):
    return all(x == 1 for x in s)

def state2str(s):
    res = ""
    for i in range(len(s)):
        res += f"{objs[i]}{s[i]} "
    return res

def print_path(p):
    for step in p:
        print(state2str(step))

def dfs(s):
    if visited(s):
        return
    
    path.append(s)

    if is_success(s):
        print("success!")
        print_path(path)
        return

    visited_map.add(get_state_key(s))
    
    neighbors_list = neighbors(s)
    for next_state in neighbors_list:
        dfs(next_state)

    path.pop()

if __name__ == "__main__":
    dfs(state)
