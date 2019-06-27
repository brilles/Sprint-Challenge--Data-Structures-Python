import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names # stretch is this without set
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names # stretch is this without set
f.close()

# duplicates = names_1 & names_2
duplicates=[]

# stretch 
for i in names_1:
    if i in names_2:
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
