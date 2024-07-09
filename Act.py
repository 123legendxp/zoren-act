"""
diri mo sugot ang bubble sort function

"""
def bubble_sort(word):
    for sort in range(0, len(word) - 1):
        """

        OUTERLOOP Outer loop for traverse the entire list  


        """
        for bubble in range(len(word) - 1):
            if word[bubble] > word[bubble + 1]:
                temp = word[bubble]
                word[bubble] = word[bubble + 1]
                word[bubble + 1] = temp
    return word

word = ['D', 'S', 'M', 'R', 'A', 'E']

"""

DIRI MO TAWAG ANG BUBBLE SORT FUNCTION 


"""

print("unsorted: ", word)
print("The sorted: ", bubble_sort(word))