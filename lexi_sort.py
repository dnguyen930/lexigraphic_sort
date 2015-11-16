class Lexigraphical_Sort:

    def sort(self, word_list, order):
        # Reset the new ord dictionary
        self.new_ord = {}

        # Fill in the new ord dictionary
        for i, char in enumerate(order):
            # If character in order is not alpha, not lower-case, or is a repeat
            # Raise and exception
            if not char.isalpha() or \
               not char.islower() or \
               char in self.new_ord.keys():
                raise Exception("Invalid Order")

            # New character, add to dictionary
            self.new_ord[char] = i

        # Sort the list with against the new ordering
        return self.merge_sort(word_list)

    # Merge Sort
    def merge_sort(self, list):
        if len(list) <= 1:
            return list

        # Split the list
        middle = len(list) / 2
        left = list[:middle]
        right = list[middle:]

        # Recursively split each list
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        # Merge the two halves together
        return self.merge(left, right)

    # Merging function
    def merge(self, left, right):
        result = []

        while left and right:
            # Check if the left word is less
            if self.left_is_less(left[0], right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # Append the rest of the remaining list
        if left:
            result.extend(left)
        if right:
            result.extend(right)
        return result

    # Check if the left word is less than
    def left_is_less(self, word_a, word_b):
        # Check for empty words
        if word_a == "":
            return True
        elif word_b == "":
            return False

        # Create of list of characters for both words
        list_a = [char for char in word_a]
        list_b = [char for char in word_b]

        # While both list are empty
        while(list_a and list_b):
            # Pop off the first char
            char_a = list_a.pop(0)
            char_b = list_b.pop(0)

            # If character doesn't have new ord value, raise Exception
            if char_a not in self.new_ord.keys() or char_b not in self.new_ord.keys():
                raise Exception("Invalid char, cannot compare")

            # Return true is char_a is less than char_b
            if self.new_ord[char_a] < self.new_ord[char_b]:
                return True
            elif self.new_ord[char_a] > self.new_ord[char_b]:
                return False
            # We continue to pop if the chars are the same

        # Check which list is now empty, that case is now shorter
        if not list_a:
            return True
        else:
            return False


lexi = Lexigraphical_Sort()
print lexi.sort(["acb", "abc", "bca"], "abc")
print lexi.sort(["acb", "abc", "bca"], "cba")
print lexi.sort(["aaa","aa",""], "a")
