class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sumi=sum(energy)
        hour=0
        if sumi>=initialEnergy:
            hour+=sumi-initialEnergy+1
        start=initialExperience
        for i in experience:
            if i>=start:
                hour+=i-start+1
                start=i+1+i
            else:
                start+=i
        return hour        