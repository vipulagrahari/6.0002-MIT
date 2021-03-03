    ###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Vipul Agrahari
# Collaborators: None
# Time:

from ps1_partition import get_partitions
import time


#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #Initialize a dictionary
    cow_dict = {}
    
    with open(f"{filename}", "r") as infile:
        
        for line in infile.readlines():
            line = line.strip("\n")
            temp = line.split(",")
            cow_dict[temp[0]] = int(temp[1])
    
    return cow_dict
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    copy_cows = cows.copy()
    {k:v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse = True)}
    cowlist = [k for k in copy_cows.keys()]
    trips = []
    while len(cowlist) > 0:
        totalweight = 0
        new_trip = []
        for cow in cowlist:
            if (totalweight + cows[cow]) < limit:
                totalweight += cows[cow]
                new_trip.append(cow)  
        for travelledcows in new_trip:
            cowlist.remove(travelledcows)
        trips.append(new_trip)
    return trips 

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result = []
    for partition in get_partitions(cows.keys()):
        score = []
        for trip in partition:
            totalWeight = 0
            for name in trip:
                totalWeight += cows[name]
            if totalWeight <= 10:
                score.append(1)
            else:
                score.append(0)
        if len(partition) == sum(score):
            result.append(partition)
    return result
            
    
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    
    #Greedy
    start = time.time()
    print(greedy_cow_transport(cows, limit = 10))
    end = time.time()
    print("time taken: ", end-start)
    print("Number of trips: ", len(greedy_cow_transport(cows)))

    #brute force
    tstart = time.time()
    cows_list = brute_force_cow_transport(cows)
    test = {}
    for i, v in enumerate(cows_list):
        test[len(v)] = i
    minimum = min(test, key=test.get)
    print()
    print(cows_list[test[minimum]])
    tend = time.time()
    print('Brute force cow transport time:', tend-tstart)
    print('Number of trips:', minimum)

compare_cow_transport_algorithms()  