#Create a program to implement a stack using a list
class stack():
    def __init__(self):
        self.stack=[]

    def empty(self):
        return len(self.stack)==0
            
    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def push(self,item):
        return self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()

#Testing implementation
if __name__ == "__main__":
    st=stack()
    print(st.empty()) #Returns True
    st.push(1)
    st.push(2)
    st.push(3)
    st.push('a')
    st.push('b')
    st.push('c')
    print(st.empty()) #Returns False
    print(f'\nThe stack has {st.size()} elements.')
    print(f'\nStack elements: {st.stack}')
    st.pop()
    print(f'\nStack elements: {st.stack}')
    print(f'\nLast element of stack is: {st.top()}')
    print(f'\nLast element of stack is: {st.peek()}')