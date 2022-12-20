with open("input.txt", 'r') as input_f:
    with open("output.txt", 'w') as output_f:
        for line in input_f:
            output_f.writelines(line)
