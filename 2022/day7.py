input_data = open("./2022/input/day7input.txt").readlines()

input_data = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''.splitlines()

#folder_content = []
#folder_data_size = 0

# current_path = []

cwd = root = {}
path = []

for row in input_data:
    row = row.strip()
    if row[0] == "$":
        if row[2] == "c":
            directory = row[5:]
            if directory == "/":
                # returning to root
                cwd = root
                path = []
            elif directory == "..":
                # returning to parent directory
                cwd = path.pop()
            else: 
                if directory not in cwd:
                    cwd[directory] = {}  # add to the dict
                path.append(cwd)
                cwd = cwd[directory]
    else:
        output, name = row.split()
        if output == "dir":
            if output not in cwd:
                cwd[name] = {}
        else:
            cwd[name] = int(output)


def part_one(dir = root, min_folder_size = 100_000):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = part_one(child)
        size += s
        ans += a
    if size <= min_folder_size:
        ans += size
    return (size, ans)


print(f'''
# part one: {part_one(root, 100_000)[1]}
''')


def calc_size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(calc_size, dir.values()))

t = calc_size() - 40_000_000
def part_two(dir = root):
    ans = float("inf")
    if calc_size(dir) >= t:
        ans = calc_size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = part_two(child)
        ans = min(ans, q)
    return ans

print(f'''
# part two: {part_two()}
''')
