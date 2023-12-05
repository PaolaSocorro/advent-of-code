def readInput(inputFile: str):
  w1 = open(inputFile, 'r')
  lines = w1.readlines()
  return lines

def findFirstnLast(input: list):
  sum = 0
  validDigits = {
    'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7, 'eight':8,'nine':9}

  # loop over every line in input
  for line in input:
    tmpnums = []
    firstnlastnums = []
    for idx, letter in enumerate(line):
      # validDigits have either a length of 3, 4, or 5 letters max
      tmp3 = line[idx:idx+3]
      tmp4 = line[idx:idx+4]
      tmp5 = line[idx:idx+5]
      # print(line)
      if letter.isdigit():
        # append all numbers in the line
        tmpnums.append(letter)
      # check to see if there valid digits as strings in the line
      if tmp3 in validDigits:
        tmpnums.append(str(validDigits[tmp3]))
      if tmp4 in validDigits:
        tmpnums.append(str(validDigits[tmp4]))
      if tmp5 in validDigits:
        tmpnums.append(str(validDigits[tmp5]))
        # print(tmp5,validDigits[tmp5],tmpnums)
    # print(tmpnums, line)
    # separate first and last, concatenated
    firstnlastnums.append(tmpnums[0]+tmpnums[-1])
    # print(firstnlastnums)
    sum += int(firstnlastnums[0])
  # print(unique_nums)
  print(sum)

def main():
  output = readInput('2023/day1/input.txt')
  findFirstnLast(output)

if __name__ == "__main__":
    main()