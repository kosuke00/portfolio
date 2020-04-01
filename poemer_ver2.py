import numpy as np
import re
class Poemer:
    def __init__(self,num,file):
        self.num = num
        self.group_size = self.num + 1
        self.text = open(file).read().lower()
        self.hand = re.sub(r",""?","",self.text)
        self.lihand = self.hand.split()
        self.word_dict = {}
        return

    def open_txt(self):
        word_li = []
        li = self.lihand
        li_2 = []
        for word in li:
            if "(" in word or ")" in word:
                continue
            else :li_2.append(word)
        for i in range(0,len(li_2)-self.group_size):
            key = tuple(li_2[i:i+self.num])
            value = li_2[i+self.num]
            if key in self.word_dict:
                self.word_dict[key].append(value)
            else:
                self.word_dict[key] = [value]

        return word_li




    def generate_txt(self,n):
        dict = self.open_txt()
        index = np.random.randint(0,len(self.lihand)-self.num)
        # return index
        result = self.lihand[index:index + self.num]

        for i in range(n):
            state = tuple(result[len(result)-self.num:])
            next_word = np.random.choice(self.word_dict[state])
            result.append(next_word)
        return " ".join(result[self.num:])

        # # for li in gram:
        #     key = tuple(li[0:n-1])
        #     value = li[n-1]
        #     print(value)
        #     if key in self.word_dict:
        #         self.word_dict[key].append(value)
        #     else:
        #         self.word_dict[key] = value

        # return self.word_dict

soad = Poemer(2,"11realex.txt")

print(soad.generate_txt(50))
