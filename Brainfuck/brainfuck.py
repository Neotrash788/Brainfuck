with open('brainfuck.brainfuck', 'r') as f:
    code = ''
    for i in list(f.readlines()):
        code = code + i.strip('\n')

codePos = 0
cells = [0]
pos = 0
out = []

while codePos < len(code):
    inst = code[codePos]

    if inst == '+':
        cells[pos] += 1

    if inst == '-':
        cells[pos] -= 1

    if inst == '>':
        if pos == len(cells)-1:
            cells.append(0)
        pos += 1

    if inst == '<':
        if pos == 0:
            cells.insert(0, 0)
        pos -= 1

    if inst == ',':
        cells[pos] = int(input('Input an int ->'))

    if inst == '.':
        out.append(chr(cells[pos]))

    if inst == '[':
        if cells[pos] == 0:
            while code[codePos] != ']':
                codePos += 1

    if inst == ']':
        if not cells[pos] == 0:
            while code[codePos] != '[':
                codePos -= 1

    codePos += 1

print(f'Cells -> {cells}\nOutput -> {out}')
