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
        start = 0
        end = len(self.lst) - 1
        dupes = 0
        while start <= end:
            mid = (start + end) // 2

            if self.lst[mid] == num:
                i = mid - 1
                while i >= 0 and self.lst[i] == num:
                    dupes += 1
                    i -= 1

                j = mid + 1
                while j <= len(self.lst) - 1 and self.lst[j] == num:
                    dupes += 1
                    j += 1

                return dupes
            elif self.lst[mid] < num:
                start = mid + 1
            else:
                end = mid - 1

        return 0
