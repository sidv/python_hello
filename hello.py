print("Hi!")
print("This is another line")
with open("data.txt" ,"w") as fd:
	for i in range(1,20):
		fd.write(str(i))
