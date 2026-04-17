class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l,r,count=0,len(people)-1,0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            count+=1
        return count

        
        # people.sort()
        # used=[False]*len(people)
        # count=0
        # for i in range(len(people)):
        #     if used[i]:
        #         continue
        #     used[i]=True
        #     more=limit-people[i]
        #     for j in range(i+1,len(people)):
        #         if not used[j] and people[j]<=more:
        #             used[j] = True
        #             break
        #     count+=1
        # return count