from collections import Counter

class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
        freqs = Counter(my_list)
        return freqs.most_common(1)[0][0]

    @classmethod
    def doubles(cls, my_list: list):
        if not my_list:
            return 0
        freqs = Counter(my_list)
        return sum(1 for count in freqs.values() if count >= 2)

# Example usage
numbers = [1,1,2,1,3,3,4,5,5,5,6,5,5,5]
print(ListHelper.greatest_frequency(numbers))  # Output: 5
print(ListHelper.doubles(numbers))  # Output: 3