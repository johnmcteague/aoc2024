'''
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

'''
reports = []

num_safe = 0

def is_safe(report_data):
    '''
    Determine if dataset is safe
    '''
    current_direction = 0  # Use to track direction (0 - first check, -1 - decreasing, 1 - increasing)
    num_samples = len(report_data)
    current  = int(report_data[0])  # Gotta convert to int

    for i in range(1, num_samples):
        next_sample = int(report_data[i])  # Grab the next sample

        if current == next_sample:  # If two consequtive samples are the same, fail
            return False
        
        # Check for changing of direction (increase/decrease). Only relevant on second sample and beyond
        if current > next_sample:
            if current_direction == -1:
                return False
            current_direction = 1
        else:
            if current_direction == 1:
                return False
            current_direction = -1
        if abs(current - next_sample) > 3:  # If difference of more than 3, fail
            return False
        current = int(report_data[i])
    return True  # If we pass every check, report is safe

# Load the file 
with open('input','r') as infile:
    for line in infile:
        # Split the data into data points
        data = line.rstrip().split(' ')
        reports.append(data)

for report in reports:
    # Check if safe and increment counter
    if is_safe(report):
        print(f'{report} - Safe')
        num_safe = num_safe + 1
    else:
        print(f'{report} - Unsafe')

print(f'Total Safe Reports: {num_safe}')