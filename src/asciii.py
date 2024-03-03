#Initialize letters & space variables

m = "M"
d = "D"
space = " "
double_space = "    "

#Initialize letter design
d_top_bottom = (d * 4) + space
d_middle = d + (space * 3) + d
m_top_bottom = m + (space * 3) + m
m_m = (m * 2) + space + (m * 2)
m_middle = m + space + m + space + m

# Initialize each line
line1 = d_top_bottom + double_space + m_top_bottom
line2 = d_middle + double_space + m_m
line3 = line2
line4 = d_middle + double_space + m_middle
line5 = d_middle + double_space + m_top_bottom
line6 = line5
line7 = d_top_bottom + double_space + m_top_bottom

#Store each line in list comprehension
lines = [line1, line2, line3, line4, line5, line6, line7]

# For loop
for line in lines: 
    print(line)
