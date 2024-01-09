

# ********format()

# ******** 

strings= "welcome to {}"

print(strings.format("python"))

# output is welcome to python

strings= "welcome to {}, {}"

print(strings.format("Miami", "Florida"))

# output is welcome to Miami, Florida

strings= "welcome to {2}, {1}, {0}"

print(strings.format( "France", "Paris","Tour Effile", ))

# output is welcome to Tour Effile, Paris, France