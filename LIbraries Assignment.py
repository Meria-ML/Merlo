import numpy as np
import matplotlib.pyplot as plt
import requests

# numpy array and mean
numbers = np.arange(1, 11)
print(numbers)
print("mean =", numbers.mean())

# pandas dataframe
data = {
    "name": ["anna", "brian", "cathy", "david"],
    "age": [23, 30, 25, 28],
    "score": [85, 90, 88, 92]
}

df = pd.DataFrame(data)
print(df)
print(df.describe())

# requests api
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
if r.status_code == 200:
    js = r.json()
    print("bitcoin price =", js["bpi"]["USD"]["rate"])

# matplotlib graph
y = [1, 3, 2, 5, 7, 6]
plt.plot(y)
plt.title("line graph")
plt.show()