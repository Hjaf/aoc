adapter_list = list(open("day10input.txt", "r").read().split('\n'))
adapter_count = len(adapter_list)
adapters = []
adapter_jolt_differences = []
incompatible_adapters = []
adapters.append(0) #outlet is 0
for adapter in adapter_list:
    adapters.append(int(adapter))
adapters.append((max(adapters)+3)) #built in adapter.
adapters.sort()
one_jolts = 0
two_jolts = 0
three_jolts = 0
i = 1
while i < len(adapters):
    this_adapter = int(adapters[i-1]) 
    next_adapter = int(adapters[i])
    difference = (next_adapter - this_adapter)
    adapter_jolt_differences.append(difference)
    if difference == 1:
        one_jolts += 1
    elif difference == 2:
        two_jolts += 1
    elif difference == 3:
        three_jolts += 1
    else:
        incompatible_adapters[adapters[i]] = difference
    i += 1
    
print('''
one jolts: %s
two jolts: %s
three jolts: %s
remaining adapters:
%s
one jolt x three jolt = %s
adapter count: %s
adapter_list count: %s
combination: %s
''' %(one_jolts, two_jolts, three_jolts, incompatible_adapters, (one_jolts*three_jolts), one_jolts+two_jolts+three_jolts, len(adapter_list), adapters))

target_jolt = sum(adapter_jolt_differences)

#####################
#
# unable to do the second part myself, had to use a smart persons solution.
#
# smart person: https://www.youtube.com/watch?v=cE88K2kFZn0
#
# explanation as i (likely mis-)understand it:
# recursive or dynamic function that stores the number of possible combinations if each adapter applied as opposed to counting each full combination.
# the full-range 
#
#####################  
#               
combinations = {}                                       #0 initiate the dictionary for number of possibilities
def variations(i):                                      #1
    remaining_range = range(i+1, len(adapters))         #2  create a range for the remaining possible adapters (adapters is created in answer one)
    if i == len(adapters)-1:                            #3  ignore the last 
        return True                                     #4  when at end of possible adapters available, "reversing the submersion"
                                                        #5  this will happen at the deepest variation when all adapters are chained(?)
    if i in combinations:                               #6  if the adapter number in the chain has already been covered, return it to move on.
        return combinations[i]                          #7  returns existing combination if already added (this will be added on top of the count if called by self line #13)
                                                        #8
    count = 0                                           #9  reset the variation count on start of each dive this only happens when none of the first two ifs are triggered.
                                                        #10 
    for adp in remaining_range:                         #11 this dives into the variation for the current adapter.
        if adapters[adp] - adapters[i] <= 3:            #12 only consider adapters of the remaining possible adapters that are within the 3 jolt difference limit (see task)
            count += variations(adp)                    #13 call self to append the adapter -> line #1 -> either:
                                                        #14         #3(at the last adapter), 6(returns existing count for this adapter) or #11(dive deep, rince and repeat))
    combinations[i] = count                             #15 set the next adapter variation count
    return count                                        #16 return to initial caller, most often this will be itself, but will provide the answer at the end.
print(variations(0))                                    #17 calling the function in a print will print the final return count. (answer to part two)
