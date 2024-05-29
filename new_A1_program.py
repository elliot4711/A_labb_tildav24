class areafel(Exception):
    """
    Exception for when area is not big enough to form A1 paper, inherits from Exception
    """
    pass

def get_smallest_size_input():
    """
    Function that takes input for the smallest paper size that will be used to try to form an A1 paper, also handles incorrect inputs
    Parameters: none
    Returns: smallest paper size (int)
    """

    smallest_paper = int(input())

    if 2 <= smallest_paper <= 30:
        return smallest_paper
    else:
        print("Wrong input, please input a number from 2 to 30")
        smallest_paper = get_smallest_size_input()
        return smallest_paper

def get_papers_available(smallest_paper):
    """
    Function that takes input for how many of each paper size will be used to try to form an A1 paper, also handles incorrect inputs
    Parameters: smallest paper size that will be used (int)
    Returns: list of integers with each index corresponding to the amount of papers of that size
    """

    papers_available = str(input())
    papers_available = papers_available.split()
    papers_expected = smallest_paper - 1

    if len(papers_available) > papers_expected or len(papers_available) < papers_expected:
        print("Incorrect input, please input only the numbers of paper types you have specified")
        papers_available = get_papers_available(smallest_paper)
    

    for i in range(len(papers_available)):
        papers_available[i] = int(papers_available[i])
        if papers_available[i] > pow(10, 9):
            print("Incorrect input, please input a maximum of 10^9 of any type of paper")
            papers_available = get_papers_available(smallest_paper)
    return papers_available
    
def get_tape_lenght(papers, paper_size):
    """
    Function that recursively calculates the amount of tape needed to form an A1 paper by recursively creating bigger and bigger papers until an A1 is formed, starting from the biggest size
    Parameters: amount of papers of a certain size, the paper size
    Returns: lenght of tape needed to attach the papers to eatchother
    """

    if papers == 0:
        return 0
    
    smaller_papers = 2 * (papers - papers_available[paper_size - 2])
    if smaller_papers < 0:
        smaller_papers =  0

    return (papers // 2) * paper_longside(paper_size) + get_tape_lenght(smaller_papers, paper_size + 1)

def paper_longside(paper_size):
    """
    Function that calculates the lenght of the long side of an AX paper given the size X
    Parameters: paper size to calculate long side lenght of
    Returns: long side lenght of paper (int)
    """

    a2_short= pow(2, -5/4)
    a2_long = pow(2, -3/4)

    if paper_size == 2:
        return a2_long

    else:
        old_long = a2_long
        old_short = a2_short
        for i in range(paper_size - 2):
            long_side = old_short
            short_side = old_long/2
            old_long = long_side
            old_short = short_side
        
        return long_side
    
smallest_paper = get_smallest_size_input()
papers_available = get_papers_available(smallest_paper)
papers_available_copy = papers_available.copy()

for i in range(len(papers_available_copy) - 1, 0, -1):
    #print(i)
    papers_available_copy[i - 1] += papers_available_copy[i] // 2
    #print(papers_available_copy)

#print(papers_available_copy)

try:
    if papers_available_copy[0] >=2:
        #print("possible")
        tape_lenght = get_tape_lenght(2, 2)
        print(tape_lenght)
    else:
        raise areafel
except:
    print("impossible")
