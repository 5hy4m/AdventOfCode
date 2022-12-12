import copy


class Solution:
    def part1(self, input):
        stacks_str, steps = input.split("\n\n")
        stacks = self.create_stacks(stacks_str)
        self.part_1_stack = copy.deepcopy(stacks)
        self.part_2_stack = copy.deepcopy(stacks)
        steps = steps.split("\n")
        top_crates_part1 = ""
        top_crates_part2 = ""

        for step in steps:
            step = step.split(" ")
            self.move_crates(step)

        for step in steps:
            step = step.split(" ")
            self.move_multiple_crates(step)

        for stack in self.part_1_stack:
            top_crates_part1 += stack[-1]

        for stack in self.part_2_stack:
            top_crates_part2 += stack[-1]

        return top_crates_part1, top_crates_part2

    def create_stacks(self, stacks):
        p = 0
        stacks_arr = []
        is_first_line = True
        current_stack_number = 0
        while p < len(stacks):
            if stacks[p] == "\n":
                if is_first_line:
                    is_first_line = False
                current_stack_number = 0
                p += 1
                continue

            if stacks[p] == "[":
                if is_first_line:
                    stacks_arr.append([stacks[p + 1]])
                    current_stack_number += 1
                else:
                    crate = [stacks[p + 1]]
                    crate.extend(stacks_arr[current_stack_number])
                    stacks_arr[current_stack_number] = crate
                    current_stack_number += 1
                p += 3
                continue

            if stacks[p] == " ":
                if "    " in stacks[p : p + 4]:
                    if is_first_line:
                        stacks_arr.append([])
                    current_stack_number += 1
                    p += 4
                else:
                    p += 1
                continue
            p += 1
        return stacks_arr

    def move_multiple_crates(self, step):
        crate_count = int(step[1])
        from_stack = int(step[3]) - 1
        to_stack = int(step[5]) - 1

        self.part_2_stack[to_stack].extend(
            self.part_2_stack[from_stack][-abs(crate_count) :]
        )
        self.part_2_stack[from_stack] = self.part_2_stack[from_stack][
            : -abs(crate_count)
        ]

    def move_crates(self, step):
        crate_count = int(step[1])
        from_stack = int(step[3]) - 1
        to_stack = int(step[5]) - 1
        for _ in range(crate_count):
            self.part_1_stack[to_stack].append(self.part_1_stack[from_stack].pop())
