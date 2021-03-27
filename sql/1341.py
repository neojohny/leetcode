from functools import cmp_to_key

class Solution:
    """
    @param a: the array in problem.
    @return: represent the new number.
    """
    def combine(self,a):
        result = []
        self.pre_combine(a,result)
        r = []
        for c in result:
            if len(c) > len(r):
                r = [str(i) for i in c]
        #r = [str(c) for c in result[0]]
        r.sort(reverse=True, key=cmp_to_key(lambda x, y: -1 if x + y < y + x else 1))
#        a = [str(a[i]) for i in range(len(a)) if i not in RmIdx]

        return ''.join(r)#str(max([int(r) for r in result]))
    
    def pre_combine(self, a,result):
        # write your code here
        total,new_list = self.calc_digits(a)
        #print(new_list)
        if total%3==0 and total>=3:
            #print('inhere',result)
            #result.append(''.join([str(n) for n in new_list]))
            result.append(new_list)
            return result
        else:
            for i in range(len(new_list)-1,-1,-1):
                nextinput = new_list[:i] + new_list[i+1:]         
                output = self.pre_combine(nextinput,result)
                if output:
                    break

    def calc_digits(self,s):
        total = 0
        new_list = []
        for item in s:
            if len(str(item)) == 1:
                total += item
                new_list.append(item)
            else:
                digits = [int(i) for i in str(item)]
                #digits.sort(reverse=True)
                total += sum(digits)
                new_list.append(int(''.join([str(d) for d in digits])))
        
        new_list.sort(reverse=True)
        return total,new_list