import pandas as pd

# chunksize=8200000 for 1gb approx

for i, chunk in enumerate(pd.read_csv('sample.csv', chunksize=700000)):
    print("Saving {} th file...".format(i))
    chunk.to_csv('smallcsv/chunk{}.csv'.format(i))

print("done")