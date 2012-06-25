from sys import argv

filename = argv[1]

txt = open(filename)

print "Here's your file %r:" %filename 
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open (file_again)

print txt_again.read() #pydoc isn't opening, why?

