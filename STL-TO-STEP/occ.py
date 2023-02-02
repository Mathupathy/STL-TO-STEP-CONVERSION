from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_stl_file, write_step_file

shp = read_stl_file(r"C:\Users\19174\Documents\mine.stl")

# Write the file as STEP
write_step_file(shp, "mine.step")
