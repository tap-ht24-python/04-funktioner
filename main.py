# importera hela modulen
import math_functions as mf
from language.strings import lower_case

result = mf.square(4)
print(result)

# importera bara en funktion
from math_functions import square
from math_functions import pythagoras
result = square(3)
print(result)

result = pythagoras(3, 4)
print(result)

# importera från annan mapp
from language.strings import lower_case
lc = lower_case("HeLLo")
print(lc)
