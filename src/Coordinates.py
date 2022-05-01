import argparse

parser = argparse.ArgumentParser(description="Output Analysis")
parser.add_argument("-p", "--path", type=str, required=True)
parser.add_argument("-o", "--output", type=str, required=True)
args = parser.parse_args()


def analyze(path, output):
    with open(path, "r") as file:
        lines = file.readlines()

        dof = 0
        step = 0

        with open(output, "w") as file2:

            for i, line in enumerate(lines):
                if "Deg. of freedom" in line:
                    dof = int(line.split()[-1])

                if line[-1] == "\n" and "Standard orientation:" in line:
                    step += 1

                    file2.write("step: {}\n".format(step))
                    file2.write("----------------------------------------------\n")
                    for k in range(i + 5, i + 5 + dof):
                        file2.write(lines[k])
                        print(lines[k])
                    file2.write("\n")


if __name__ == '__main__':
    analyze(args.path, args.output)
