import aoc
import re

puzzle_input = aoc.fetch_input(2022, 11)

# Not solved independently

monkeys = {}


def refine():
    monkeys.clear()
    for monkey, data in enumerate(puzzle_input.split("\n\n")):
        starting_items, operation, test, test_if_true, test_if_false = \
            re.findall(": (.+)", data)
        monkeys[monkey] = (
            [int(item) for item in starting_items.split(", ")],
            operation
        ) + tuple(
            int(v.split()[-1]) for v in (test, test_if_true, test_if_false)
        )


# Part one

refine()

stats = {monkey: 0 for monkey in monkeys}

for i in range(20):
    for monkey, (
        items, operation, divisible_by, true_monkey, false_monkey
    ) in monkeys.items():
        stats[monkey] += len(items)
        for old in items:
            new = eval(operation.partition(" = ")[2])
            new = int(new / 3)
            target = true_monkey if (new % divisible_by) == 0 else false_monkey
            monkeys[
                true_monkey if (new % divisible_by) == 0 else false_monkey
            ][0].append(new)
        items.clear()
result = 1

for count in list(sorted(stats.values()))[-2:]:
    result *= count
print(result)

# Part Two

refine()

monkey_product = 1
for values in monkeys.values():
    monkey_product *= values[2]
stats = {monkey: 0 for monkey in monkeys}
for i in range(10000):
    for monkey, (
        items, operation, divisible_by, true_monkey, false_monkey
    ) in monkeys.items():
        stats[monkey] += len(items)
        for old in items:
            new = eval(operation.partition(" = ")[2])
            new = new % monkey_product
            target = true_monkey if (new % divisible_by) == 0 else false_monkey
            monkeys[
                true_monkey if (new % divisible_by) == 0 else false_monkey
            ][0].append(new)

        items.clear()
result = 1
for count in list(sorted(stats.values()))[-2:]:
    result *= count
print(result)
