from SelectionSort import *

def main():
    #lists of names and scores from assignment
    names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felicia', 'Carl']
    scores = [99, 85, 64, 78, 95, 50, 88]

    #print out original names and scores
    print('Original Lists')
    print('Names\t Scores')
    for i in range(len(scores)):
        print(f'{names[i]}\t {scores[i]}')
    
    #call sort function
    sort(names, scores, 0) 
    
    
    print()
    #print out sorted names and lists
    print('Sorted Lists')
    print('Names\t Scores')
    
    for i in range(len(scores)):
        print(f"{names[i]}\t {scores[i]}")
if __name__ == "__main__":
    main()