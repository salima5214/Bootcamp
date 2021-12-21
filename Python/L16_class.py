# L16: https://reurl.cc/Gb796A

class IO:
    SupportedSrcs = [ "console", "file"]
    def read( src ):
        if src not in IO.SupportedSrcs:
            print("Not supported")
        else:
            print( "Read from", src)

print(IO.SupportedSrcs)
IO.read("file")
IO.read("internet")