# implementasi stack pada python

# creating a stack
def creating_stack():
    stack = []
    return stack

# creating an empty stack
def check_empty(stack):
    return len(stack) == 0

# check full
def check_full(stack):
    return len(stack) == 10

# adding item into the stack
def push(stack, item):
     if check_full(stack):
        print("stack is full")
     else:
        stack.append(item)
        print("pushed item: " + item)

# removing an element from the stack
def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = creating_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))