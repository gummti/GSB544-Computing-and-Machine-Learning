print ("Hello World")

# experimenting
# test1 = True + "True"
test2 = 0.9
# test2 += "hey"

test3 = "hey"
# test3 += str(test2)
print(test3)

import numpy as np
my_nums = np.array([1,2,3,4,5])
np.sum(my_nums)

import pandas as pd
dat = pd.read_csv("https://gist.githubusercontent.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv")
dat
dat.info()