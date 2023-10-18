from collections import deque
class Solution:
    def generateparaenthesis(self,n: int)->List[str]:
        st=collections.deque()
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append()
            else:
                if not st:
                    return False
                elif i==']'and str[-1]=='[':
                    st.pop()
                elif i=='}'and str[-1]=='{':
                    st.pop()
                elif i==')'and str[-1]=='(':
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False


        