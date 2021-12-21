# L14: https://reurl.cc/ye2pYl

import random
import statistics

# random
print( random.choice([0, 1, 5, 8]) )
print( random.sample([0, 1, 5, 8], 2) )

print( "##########################" )
print( random.random() )
print( random.uniform(0, 1) )
print( random.uniform(0.0, 1.0) )
print( random.normalvariate(100, 10) )

data = [0, 1, 5, 8]
print( data )
random.shuffle( data )
print( data )


# statistics
print( "##########################" )
print( statistics.mean([1, 4, 6, 9]) )
print( statistics.median([1, 4, 6, 9]) )
print( statistics.stdev([1, 4, 6, 9]) )

