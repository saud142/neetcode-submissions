from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in '+-*/':
                b,a = st.pop(),st.pop()
                if t == '+' :
                    st.append(a + b)
                elif t == '-' :
                    st.append(a - b)  
                elif t == '*' :
                    st.append(a * b)
                else:
                    division = a/b
                    if division < 0:
                        st.append(ceil(division))
                    else:
                        st.append(floor(division))
            else:
                st.append(int(t))
        return st[0]               


                


        