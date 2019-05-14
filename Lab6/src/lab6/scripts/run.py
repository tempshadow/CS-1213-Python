stack = {}
heap = {i: None for i in range(1000,1050)}
SIZE = 50
def find_space(struct):
  min_addr = min(struct.keys())
  for i in range(min_addr, min_addr + SIZE):
    if struct[i] is None:
      return i
def get_input(input_str):
  input_str = input_str.strip()
  input_parts = input_str.split(' ')
  if len(input_parts) == 1:
    if 'quit' not in input_parts:
      return input_parts + ['print', None]
    else:
      return [None, None, None]
  if len(input_parts) > 3:
    return [input_parts[0], input_parts[1], input_parts[2] + input_parts[3] + input_parts[4]]
  return input_parts
def evaluate(r_value):
  is_var = False
  try:
    r_value = int(r_value)
  except:
    is_var = True
  if not is_var:
    if r_value not in heap.values():
      space = find_space(heap)
      if space is None:
        raise MemoryError("Not enough memory.")
      addr = space
      heap[addr] = r_value
    else:
      addr = [key for key, value in heap.items() if value == r_value].pop()
  else:
    addr = stack[r_value]
  return addr
def evaluate2(r_value):
  is_var = False
  try:
    r_value = float(r_value)
  except:
    is_var = True
  if not is_var:
    if r_value not in heap.values():
      space = find_space(heap)
      if space is None:
        raise MemoryError("Not enough memory.")
      addr = space
      heap[addr] = r_value
    else:
      addr = [key for key, value in heap.items() if value == r_value].pop()
  else:
    addr = stack[r_value]
  return addr
def assignment(l_value, r_value):
  if '.' not in r_value:
    addr = evaluate(r_value)
    stack[l_value] = addr
  else:
    addr = evaluate2(r_value)
    stack[l_value] = addr
def assignment2(l_value, r_value):
  if '.' not in str(heap[stack[r_value[0]]]):
    if r_value[1] == '+':
      addr = evaluate(heap[stack[r_value[0]]] + heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '-':
      addr = evaluate(heap[stack[r_value[0]]] - heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '/':
      addr = evaluate(heap[stack[r_value[0]]] / heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '*':
      addr = evaluate(heap[stack[r_value[0]]] * heap[stack[r_value[2]]])
      stack[l_value] = addr
  else:
    if r_value[1] == '+':
      addr = evaluate2(heap[stack[r_value[0]]] + heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '-':
      addr = evaluate2(heap[stack[r_value[0]]] - heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '/':
      addr = evaluate2(heap[stack[r_value[0]]] / heap[stack[r_value[2]]])
      stack[l_value] = addr
    elif r_value[1] == '*':
      addr = evaluate2(heap[stack[r_value[0]]] * heap[stack[r_value[2]]])
      stack[l_value] = addr
def print_var(var):
  if var not in stack.keys():
    print("NotFoundError")
  else:
    print(heap[stack[var]])
def print_var3(var, op, var2):
  if var not in stack.keys():
    print("NotFoundError")
  else:
    if op == '+':
      print(heap[stack[var]] + heap[stack[var2]])
    elif op == '-':
      print(heap[stack[var]] - heap[stack[var2]])
    elif op == '/':
      print(heap[stack[var]] / heap[stack[var2]])
    elif op == '*':
      print(heap[stack[var]] * heap[stack[var2]])
def main():
  while True:
    _str = input(">>> ")
    lvalue, op, rvalue = get_input(_str)
    if rvalue == None:
      if op == 'print':
        print_var(lvalue)
    elif rvalue[0] == 'x':
      if op == '=':
        assignment2(lvalue, rvalue)
        print_var(lvalue)
    else:
      if op == '=':
        assignment(lvalue, rvalue)
      elif op == '+':
        print_var3(lvalue, op, rvalue)
      elif op == '-':
        print_var3(lvalue, op, rvalue)
      elif op == '/':
        print_var3(lvalue, op, rvalue)
      elif op == '*':
        print_var3(lvalue, op, rvalue)
      elif op == 'print':
        print_var(lvalue)
      elif op is None:
        break
if __name__ == '__main__':
  main()