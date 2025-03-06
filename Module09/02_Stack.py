# 2. Function to Implement Stack Operations using *args.

def stack_operations(*args):
    stack = []  # Initializing an empty list to act as a stack
    
    for operation in args:  # Iterating over all the operations provided in *args
        if operation.startswith("push"):  # Checking if the operation is 'push'
            _, value = operation.split()  # Splitting the operation to extract the value
            stack.append(value)  # Pushing (adding) the value onto the stack
            print(f"Pushed {value}")

        elif operation == "pop":  # Checking if the operation is 'pop'
            if stack:  # Ensuring the stack is not empty before popping
                popped_value = stack.pop()  # Removing the top element
                print(f"Popped {popped_value}")
            else:
                print("Stack is empty, cannot pop!")  # Handling empty stack case

        elif operation == "peek":  # Checking if the operation is 'peek'
            if stack:  # Ensuring the stack is not empty before peeking
                print(f"Top element: {stack[-1]}")  # Displaying the last element (top of stack)
            else:
                print("Stack is empty!")  # Handling empty stack case

        elif operation == "display":  # Checking if the operation is 'display'
            print("Stack contents:", stack if stack else "Stack is empty.")  # Displaying stack contents

# Example usage of stack operations
stack_operations(
    "push 10",  # Push 10 onto the stack
    "push 20",  # Push 20 onto the stack
    "push 30",  # Push 30 onto the stack
    "peek",     # View the top element
    "pop",      # Remove the top element (30)
    "display",  # Show remaining stack elements
    "pop",      # Remove the next top element (20)
    "pop",      # Remove the next top element (10)
    "pop"       # Attempt to pop from an empty stack
)