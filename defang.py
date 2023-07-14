import sys

INPUT_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]

with open(INPUT_PATH, encoding = "utf-8") as input_file:
    with open(OUTPUT_PATH, "w", encoding = "utf-8") as output_file:
        contents = input_file.readlines()
        for line in contents:
            line = line.replace("http", "hxxp")
            line = line.replace("ftp", "fxp")
            line = line.replace(".", "[.]")
            line = line.replace("@", "[AT]")
            output_file.write(line)
    output_file.close()
input_file.close()
