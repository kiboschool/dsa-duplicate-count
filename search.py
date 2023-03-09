class Search:
    def __init__(self, lst):
        self.lst = lst 

    def duplicate_count_linear(self, num):
        total = 0
        for val in self.lst:
            if val == num:
                total += 1

        if total == 0:
            return 0
        else:
            # number of duplicates is number of occurrences - 1
            return total - 1

    def duplicate_count_binary(self, num):
        # implement binary search duplicate count here
        pass
