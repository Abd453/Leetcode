class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        s = skill[0] + skill[-1]
        chemistry = skill[0] * skill[-1]
        for i in range(1, n // 2):
            if skill[i] + skill[n-i-1] != s:
                return -1
            chemistry += skill[i] * skill[n-i-1]

        return chemistry


        