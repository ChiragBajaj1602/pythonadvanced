# write a python problem for the cube of teh giuven range using generators
def cubegenerator():
    count=1
    for i in range(10):
        yield count**3
        count+=1
for cube in cubegenerator():
    print("The cubes are %d",cube)
# write a python pr
