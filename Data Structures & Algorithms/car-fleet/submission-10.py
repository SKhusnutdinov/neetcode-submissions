class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]

        pairs.sort(reverse=True)
        print(pairs)
        st = []

        for pair in pairs:
            p, s = pair
            t = (target - p) / s

            if not st:
                st.append(t)
            if st and st[-1] >= t:
                continue
            else:
                st.append(t)

        return len(st)