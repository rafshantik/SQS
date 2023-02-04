import numpy as np

# Read the original file
with open('sqscell.out') as f1:
    lines = f1.readlines()

# Save the original file
with open('old-sqscell.out', 'w') as f2:
    f2.writelines(lines)

# Replace it with a new file with 3 cells.
# The 3 cells have the smallest and equal vector lengths
with open('sqscell.out', 'w') as f3:
    elements = lines[0].split()
    if len(elements) >= 1:
        tot = int(elements[0])  # total number of cells
        count = 0
        arr1 = np.zeros((tot, 2))
        for i in range(tot):
            arr1[i][0] = i
            a = np.array([float(x) for x in lines[4 * i + 2].split()])
            b = np.array([float(x) for x in lines[4 * i + 3].split()])
            c = np.array([float(x) for x in lines[4 * i + 4].split()])
            l1 = np.linalg.norm(a)
            l2 = np.linalg.norm(b)
            l3 = np.linalg.norm(c)
            if l1 == l2 and l2 == l3:
                arr1[i][1] = l1
                count += 1
        arr1 = arr1[arr1[:, 1].argsort()]
        if count >= 3:
            j = 0
            f3.write('3\n\n')
            for i in range(tot):
                if arr1[i][1] > 0 and j < 3:
                    f3.write(lines[4 * int(arr1[i][0]) + 2])
                    f3.write(lines[4 * int(arr1[i][0]) + 3])
                    f3.write(lines[4 * int(arr1[i][0]) + 4] + '\n')
                    j += 1
        else:
            f3.write(str(count) + '\n\n')
            for i in range(tot):
                if arr1[i][1] > 0:
                    f3.write(lines[4 * int(arr1[i][0]) + 2])
                    f3.write(lines[4 * int(arr1[i][0]) + 3])
                    f3.write(lines[4 * int(arr1[i][0]) + 4] + '\n')
    else:
        print("The first line of the file does not contain enough information.")
