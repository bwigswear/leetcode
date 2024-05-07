class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        negativeheap = []
        positive = 0
        first = []
        firstindex = -1
        last = []
        lastindex = -1
        for i, transaction in enumerate(transactions):
            if(transaction[0] > transaction[1]):
                if firstindex == -1:
                    first = transaction
                    firstindex = i
                    last = transaction
                    lastindex = i
                    continue
                if transaction[1] < first[1]:
                    first = transaction
                    firstindex = i
                if transaction[1] > last[1]:
                    last = transaction
                    lastindex = i
                    
            else:
                positive = max(transaction[0], positive)
        
        money = 0

        if firstindex == -1:
            return positive
        
        money+=first[0]
        money-=first[1]

        for i, transaction in enumerate(transactions):
            if(transaction[0] > transaction[1]):
                if i == firstindex or i == lastindex:
                    continue
                money+= transaction[0]
                money-= transaction[1]
        
        if lastindex != firstindex:
            money+=last[0]

            if positive > 0 and positive > last[1]:
                money += positive
                money -= last[1]
        else:
            if positive > 0 and positive > last[1]:
                money += positive
            else:
                money += last[1]
        return money