import sys

input_files = []
output_file = ''

args_count = len(sys.argv[1:])
if args_count > 0:
    for x in range(1, args_count):
        # print('Analizuję:', sys.argv[x])
        if sys.argv[x] == '>' and x < args_count:
            output_file = sys.argv[x+1]
            print('Output file:', output_file)
            break
        input_files.append(sys.argv[x])

with open(output_file, "w") as opt_fl:
    for filename in input_files:
        with open(filename) as current_file:
            data = current_file.read()
            opt_fl.write(data)
            opt_fl.write('\n')
