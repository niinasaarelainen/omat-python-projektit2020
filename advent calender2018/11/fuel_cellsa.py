
data = 3999
#data = 
leveys = 299
korkeus = 299
cell_leveys = 3
cell_korkeus = 3
luvut = []


"""  cell at 3,5  (X,Y notation)  serial = 8
122,79, grid serial number 57:
217,196, grid serial number 39

The rack ID is 3 + 10 = 13.
The power level starts at 13 * 5 = 65.
Adding the serial number produces 65 + 8 = 73.
Multiplying by the rack ID produces 73 * 13 = 949.
The hundreds digit of 949 is 9.
Subtracting 5 produces 9 - 5 = 4."""
def find_power_level():
    x = 217
    y = 196
    serial = 39

    rack_id = x + 10
    p_level = (rack_id * y + serial ) * rack_id
    p_level = int(str(p_level)[-3:-2]) - 5
   
    return p_level




print(find_power_level())
