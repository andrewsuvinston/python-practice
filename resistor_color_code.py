colour_digit={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
colour_multiplier={"black":1,"brown":10,"red":100,"orange":1000,"yellow":10000,"green":100000,"blue":1000000,"violet":10000000,"grey":100000000,"white":1000000000,"gold":0.1,"silver":0.01}
colour_tolerance={"brown":1,"red":2,"green":0.5,"blue":0.25,"violet":0.1,"grey":0.05,"gold":5,"silver":10}

a=int(input('''
Choose Mode:
1.decode colors to resistance
2.Encode resistance to colors
Type the number : '''))
if a==1:
    res=input("Give the colors(eg:black brown red orange) : ").lower()
    def decoder_resistance(colors_string):
        c=colors_string.split()
        if len(c) != 4:
            print("Please enter Four Colours")
        elif c[0] not in colour_digit or c[1] not in colour_digit or c[2] not in colour_multiplier or c[3] not in colour_tolerance:
            print("Give the valid colour")
        else:
            d = colour_digit[c[0]]
            e = colour_digit[c[1]]
            f = colour_multiplier[c[2]]
            g = colour_tolerance[c[3]]
            print(f"{(d*10+e)*f} ohms ±{g}%")
    decoder_resistance(res)
else:
    print("working")
        
              
