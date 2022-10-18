

#ask for file name
name = input("File name: ")

#clean file name
name_c = name.lower().strip()

if name_c.endswith(".gif"):
    print ("image/gif")
elif name_c.endswith(".jpg") or name_c.endswith(".jpeg"):
    print ("image/jpeg")
elif name_c.endswith(".png"):
    print ("image/png")
elif name_c.endswith(".pdf"):
    print ("application/pdf")
elif name_c.endswith(".txt"):
    print ("text/plain")
elif name_c.endswith(".zip"):
    print ("application/zip")
else:
    print ("application/octet-stream")