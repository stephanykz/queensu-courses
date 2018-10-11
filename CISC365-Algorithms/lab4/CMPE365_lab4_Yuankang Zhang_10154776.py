# CMPE 365 Lab 4
# Name: Yuankang Zhang
# Student Number: 10154776

import csv
#import numpy as np
from random import *

'''
Part1


# read original arrive/departure csv files and combine them into one list os lists
def read_csv(arrive_file_name, depart_file_name):
    
    rslt = []
    
    with open(depart_file_name) as list1_depart :
        list1_depart_reader = csv.reader(list1_depart,delimiter = ' ', quoting=csv.QUOTE_NONNUMERIC)
        list1_depart_reader = list(list1_depart_reader)

    with open(arrive_file_name) as list1_arrive :
        list1_arrive_reader = csv.reader(list1_arrive, delimiter = ' ', quoting=csv.QUOTE_NONNUMERIC)
        list1_arrive_reader = list(list1_arrive_reader)

    i = 0
    for row in list1_arrive_reader:
        row.append(list1_depart_reader[i][0])
        row.append(i)
        rslt.append(row)
        i = i + 1
            
    return rslt
        
    
# sort the list of lists by departure time, using bubble sort
def sort_by_departure(table):
    rslt = table
    i = len(rslt) -1
    while i > 0:
        j = 0
        while j < i:
            if rslt[j][1] > rslt[j+1][1]:
                swap(rslt, j, j+1)
            j = j+1
        i = i - 1
    return rslt

def swap(rslt, a, b):
    new_a = rslt[a]
    rslt[a] = rslt[b]
    rslt[b] = new_a

# greedy algorithm to create timetable for gates
def greedy_algo (arrive_file, depart_file):
    timetable = read_csv(arrive_file, depart_file)
    sorted_timetable = sort_by_departure(timetable)
    temp_timetable = []
    gates = []

    l = len(sorted_timetable)
    
    print ("Time Table for All Gates:\n(Aircrafts in each gate listed as [arrive time, departure time, #label of the aircraft])\n")
    while len(sorted_timetable)>0:
        #a ssign the first remaining aircraft in the sorted_timetable to new gate
        gates.append([sorted_timetable[0]])
        sorted_timetable.pop(0)                 # remove this first aircraft
        latest_gate = len(gates)-1              # record the # of the new gate
        for i in sorted_timetable:              # check all remaining aircraft 1 by 1, and assign the suitable ones to the new gate
            latest_aircraft = len(gates[latest_gate])-1
            if i[0] > gates[latest_gate][latest_aircraft][1]:
                gates[latest_gate].append(i)
                sorted_timetable.remove(i)      # for aircrafts that have been assigned to a gate, remove them from sorted_timetable
        print ("Gate " + str(len(gates)) + ":")
        print (gates[latest_gate])
        print ("")
                
    print (str(len(gates)) + " Gates are arranged.")

# test different cases
def test_part1(arrive_csv_name, depart_csv_name):
    greedy_algo (arrive_csv_name, depart_csv_name)

test_part1('start1.csv', 'finish1.csv')



End Part1
'''



'''
Start Part2
'''


# read original arrive/departure csv files and combine them into one list os lists
def read_csv(arrive_file_name, depart_file_name):
    
    rslt = []
    
    with open(depart_file_name) as list1_depart :
        list1_depart_reader = csv.reader(list1_depart,delimiter = ' ', quoting=csv.QUOTE_NONNUMERIC)
        list1_depart_reader = list(list1_depart_reader)

    with open(arrive_file_name) as list1_arrive :
        list1_arrive_reader = csv.reader(list1_arrive, delimiter = ' ', quoting=csv.QUOTE_NONNUMERIC)
        list1_arrive_reader = list(list1_arrive_reader)
        i = 0
        for row in list1_arrive_reader:
            row.append(list1_depart_reader[i][0])
            row.append(i)
            rslt.append(row)
            i = i + 1
            
    return rslt

# for part 2 situation 1, introduce some flight delate situation before sorting
def delate(timetable,possible_delate):

    fraction = randint(1, len(timetable))
    temp_fraction = fraction

    for i in range(0, len(timetable), 1):   # check every aircraft to see if to include lateness
        if temp_fraction > 0:
            ifdelate = choice([True, False])         # choose the delate aircraft randomly: 1 means this aircraft will be delated, 0 means this aircraft will not be delated
            if ifdelate:
                delate_amount = sample(possible_delate,1)   # adding a uniformly random delay
                timetable[i][0] = timetable[i][0] + delate_amount[0] 
                delate_amount = sample(possible_delate,1)
                timetable[i][1] = timetable[i][1] + delate_amount[0]

                temp_fraction = temp_fraction - 1

    return timetable, fraction
        
    
# sort the list of lists by departure time, using bubble sort
def sort_by_departure(table):
    rslt = table
    i = len(rslt) -1
    while i > 0:
        j = 0
        while j < i:
            if rslt[j][1] > rslt[j+1][1]:
                swap(rslt, j, j+1)
            j = j+1
        i = i - 1
    return rslt

def swap(rslt, a, b):
    new_a = rslt[a]
    rslt[a] = rslt[b]
    rslt[b] = new_a


# greedy algorithm to create timetable for gates
def greedy_algo_part2_situation1 (arrive_file, depart_file, possible_delate):
    timetable = read_csv(arrive_file, depart_file)
    timetable, fraction = delate(timetable, possible_delate)              #delate known before sorting
    sorted_timetable = sort_by_departure(timetable)
    temp_timetable = []
    gates = []

    l = len(sorted_timetable)
    
    #print ("Time Table for All Gates:\n(Aircrafts in each gate listed as [arrive time, departure time, #label of the aircraft])\n")
    while len(sorted_timetable)>0:
        # assign the first remaining aircraft in the sorted_timetable to new gate
        gates.append([sorted_timetable[0]])
        sorted_timetable.pop(0)                 # remove this first aircraft
        latest_gate = len(gates)-1              # record the # of the new gate
        for i in sorted_timetable:              # check all remaining aircraft 1 by 1, and assign the suitable ones to the new gate
            latest_aircraft = len(gates[latest_gate])-1
            if i[0] > gates[latest_gate][latest_aircraft][1]:
                gates[latest_gate].append(i)
                sorted_timetable.remove(i)      # for aircrafts that have been assigned to a gate, remove them from sorted_timetable
        #print ("Gate " + str(len(gates)) + ":")
        #print (gates[latest_gate])
        #print ("")
                
    #print (str(len(gates)) + " Gates are arranged.")
    return len(gates), fraction

# Part 2 greedy algorithm to create timetable for gates.
# This time, random fraction of the aircrafts are allowed to have random lateness
def greedy_algo_part2_situation2 (arrive_file, depart_file,possible_delate):
    timetable = read_csv(arrive_file, depart_file)
    sorted_timetable = sort_by_departure(timetable)
    temp_timetable = []
    gates = []

    l = len(sorted_timetable)

    fraction = randint(1, len(timetable)) # selecting a random fraction of the aircrafts that will be delated
    temp_fraction = fraction
                       
    #print ("Time Table for All Gates:\n(Aircrafts in each gate listed as [arrive time, departure time, #label of the aircraft])\n")
    while (len(sorted_timetable) > 0):
        # assign the first remaining aircraft in the sorted_timetable to new gate
        gates.append([sorted_timetable[0]])
        sorted_timetable.pop(0)                 # remove this first aircraft
        latest_gate = len(gates)-1              # record the # of the new gate

        for i in sorted_timetable:              # check all remaining aircraft 1 by 1, and assign the suitable ones to the new gate
            if temp_fraction > 0:                    # include lateness
                ifdelate = randint(0,1)          # 1 means this aircraft will be delated, 0 means this aircraft will not be delated
                if ifdelate:
                    arrive_delate = sample(possible_delate,1)
                    i[0] = i[0] + arrive_delate[0]         # adding a uniformly random delay to arrive time
                    depart_delate = sample(possible_delate,1)
                    i1_temp = i[1] + depart_delate[0]
                    '''while (i1_temp - i[0]) < 0.75:      # impose a minimum time of 0.75h between arrival and departure of any aircraft
                        depart_delate = sample(possible_delate,1)
                        i1_temp = i[1] + depart_delate[0]'''
                    i[1] = i1_temp                      # adding a uniformly random delay to depart time
                    temp_fraction = temp_fraction - 1
            latest_aircraft = len(gates[latest_gate])-1
            if i[0] > gates[latest_gate][latest_aircraft][1]:
                gates[latest_gate].append(i)
                sorted_timetable.remove(i)      # for aircrafts that have been assigned to a gate, remove them from sorted_timetable

        # Due to the possible delate, the sorted_timetable needs to be sorted again
        # before we move on to the next gate assignment
        sorted_timetable = sort_by_departure(sorted_timetable)  

        #print ("Gate " + str(len(gates)) + ":")
        #print (gates[latest_gate])
        #print ("")
                
    print (str(len(gates)) + " Gates are arranged.")

    return len(gates), fraction

# test different cases
def test_part2(arrive_csv_name, depart_csv_name):

    y = [] 
    x1 = [1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0] # highest allowed lateness
    possible_delate = [[0.25,0.5,0.75,1.0],
                       [0.25,0.5,0.75,1.0,1.25],
                       [0.25,0.5,0.75,1.0,1.25,1.5],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75],
                       [0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0]]  
    x2 = []

    for i in range(len(possible_delate)):
        num_gates, fraction = greedy_algo_part2_situation1 (arrive_csv_name, depart_csv_name,possible_delate[i])
        y.append(num_gates)
        x2.append(fraction)
    '''        
    for i in range(len(possible_delate)):
        num_gates, fraction = greedy_algo_part2_situation2 (arrive_csv_name, depart_csv_name,possible_delate[i])
        print (fraction)
        y.append(num_gates)
        x2.append(fraction)'''

    print ("Gate increase: "+ str(y), "Allowed lateness: " + str(x1), "Fraction: " +str(x2))

test_part2('start2.csv', 'finish2.csv')



'''
End Part2
'''
