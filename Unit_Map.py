new_units = 13
minor_change = 12
major_change = 11
no_change = 10
new_build = 42
pot_error = 14

public_land = [951, 953, 954]
housing = [102, 103, 111, 998], 511
highrise = [199, 562, 563, 713, 699]
warehouse = [590, 592, 593, 594]
condos = [711, 116, 997, 511, 907]
boyd = [561, 961]
industry=[200, 550, 695]
malls = [581, 582, 914]
office = [506, 509, 566, 760, 916]

same_types = [public_land, housing, warehouse, condos, boyd, industry, malls, office, highrise]

commres = range(504,513)
apartments = [111, 112, 113, 114, 115, 120, 150, 199]

def property_change_sorter(old, new):

    try:
        old = int(old)
    except ValueError:
        old = 0
    
    try:
        new = int(new)
    except ValueError:
        new = 0

    if old == new:
        return no_change
    
    if old == 0 and new !=0:
        return 14

    # Handle non-changing edge cases
    for grp in same_types:
        if old in grp and new in grp:
            return no_change
        
    # PUD -> SFH may or may not entail a change
    # Call it minor to be safe
    if new in apartments:
        if old in [957, 997, 998]:
            return minor_change
        if old in [911, 901]:
            return new_build
    
    if new in [957, 997, 998]:
        if old in apartments:
            return minor_change

    # Cast commercial/residential hybrid to 400 series
    #new = handle_mod(new, commres, -100)
    #old = handle_mod(old, commres, -100)

    new = handle_mod(new, [106], 6)

    pc_new = new//100
    pc_old = old//100

    if pc_old != pc_new:
        return major_change
    
    if new in apartments and old in apartments:
        if new > old:
            return new_units
        
    if pc_old == pc_new:
        return minor_change


def handle_mod(p_t, chk_lst, delta):
    if p_t in chk_lst:
        p_t += delta
    return p_t