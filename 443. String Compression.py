class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) != 1:
            lst = list(chars[0])
            counter = 1
            lst1 = []

            for i in range(1, len(chars)):
                if chars[i] != chars[i-1]:
                    counter = 1
                    lst.append(chars[i])
                else:
                    counter += 1
                lst.append(counter)
            for i in range(len(lst)-1):
                if type(lst[i]) == str:
                    lst1.append(lst[i])
                elif type(lst[i+1]) == str and lst[i] != 1:
                    print(f'lst[i]-1: {lst[i]}')
                    if int(lst[i]) > 9:
                        for digit in str(lst[i]):
                            lst1.append(digit)
                    else:
                        lst1.append(lst[i])
            lst1.append(lst[-1])

            if int(lst1[-1]) > 9:
                temp = lst1.pop()
                temp = str(temp)
                for i in temp:
                    lst1.append(i)
            elif int(lst1[-1]) == 1:
                lst1.pop()

            lst1 = [str(item) for item in lst1]
            chars[:] = lst1
        return len(chars)