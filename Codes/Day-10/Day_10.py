class Reverse:
    def reverse_sentence(self, s):
        return ' '.join(reversed(s.split()))

    def reverse_char(self, s):
        return ''.join(reversed(list(s)))

    def reverse_all(self, s):
        str = Reverse().reverse_setence(s)
        ans = Reverse().reverse_char(str)
        return ans

str = 'night good'
solution = Reverse()
print(solution.reverse_sentence(str))
print(solution.reverse_all(str))
print(solution.reverse_char(str))