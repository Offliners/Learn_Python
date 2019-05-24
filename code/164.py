# be careful when using
# "writelines"

data = ["alpha","beta","gamma"] # some strings

with open("code/Data/data2.txt","w") as f:
    f.writelines(data)

# no newlines will be added
