class Phone:
    def __init__(self, input):
        self.atmost_size = 100000
        lines = input.split("\n")
        self.structure = [{"/": []}]
        wd = self.structure
        pwd = ""
        for line in lines:
            instruction = line.split(" ")
            is_command = instruction[0] == "$"

            if is_command:
                is_cd = instruction[1] == "cd"
                if is_cd:
                    if instruction[2] == "..":
                        parent_dir = (
                            pwd.split(",")[:-1]
                            if pwd[-1] != ","
                            else pwd[:-1].split(",")[:-1]
                        )
                        # print("self.structure: ", self.structure, type(self.structure) == list)
                        # print("Line: ", line)
                        # print("parent_dir", parent_dir)
                        # print("before WD: ", wd)
                        # print("before PWD: ", pwd)
                        for i, dir in enumerate(parent_dir):
                            # print("dir: ", dir)
                            if i == 0:
                                wd = self.structure[0]["/"]
                                pwd = "/"
                                continue

                            pwd += "," + dir
                            wd = wd[0][dir] if type(wd) == list else wd[dir]
                        # print("wd: ", wd)
                        # print("after PWD: ", pwd)

                        continue

                    for object in wd:
                        if instruction[2] in object.keys():
                            pwd += instruction[2] + ","
                            wd = object[instruction[2]]
                            break
                continue

            is_dir = instruction[0] == "dir"
            if is_dir:
                wd.append({str(instruction[1]): []})
                continue

            wd.append({str(instruction[1]): int(instruction[0])})
        self.structure = self.structure[0]
        print("RESULT: ", self.structure)

    def free_space(self):
        size = 0
        for key in self.structure.keys():
            if not size < self.atmost_size:
                return size
            object_size = self.get_total_size(self.structure[key])
            if object_size < self.atmost_size:
                size += object_size
        return size

    def get_total_size(self, object):
        size = 0
        if self.check_is_dir(object):
            for child in object:
                if self.check_is_dir(child):
                    size += self.get_total_size(child)
        size += self.get_total_size(object)

    @staticmethod
    def check_is_dir(object):
        return type(object) == list
