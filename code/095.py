# write to a text file

f = open("code/Data/t.txt","w")
# or:
# f = open("Data/t.txt",mode = "w")
# w = create and write
# r = read(default)
# a = append
# x = create if not existed

f.write("Hello, World!")
f.close()
