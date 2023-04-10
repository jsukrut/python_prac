def test():
   try:
       f = open("demofile.txt")
       f.write("Lorum Ipsum")
       print('File has been written')
   except:
       print("Unable to write the file")
   finally:
       print("Something went wrong")
   
test()