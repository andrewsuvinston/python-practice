colour_digit={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
colour_multiplier={"black":1,"brown":10,"red":100,"orange":1000,"yellow":10000,"green":100000,"blue":1000000,"violet":10000000,"grey":100000000,"white":1000000000,"gold":0.1,"silver":0.01}
colour_tolerance={"brown":1,"red":2,"green":0.5,"blue":0.25,"violet":0.1,"grey":0.05,"gold":5,"silver":10}

colour_digi={0:"black",1:"brown",2:"red",3:"orange",4:"yellow",5:"green",6:"blue",7:"violet",8:"grey",9:"white"}
colour_multiplie={1:"black",10:"brown",100:"red",1000:"orange",10000:"yellow",100000:"green",1000000:"blue",10000000:"violet",100000000:"grey",1000000000:"white",0.1:"gold",0.01:"silver"}
colour_toleranc={1:"brown",2:"red",0.5:"green",0.25:"blue",0.1:"violet",0.05:"grey",5:"gold",10:"silver"}

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
elif a==2:
    original=input("Enter the Resistance(Eg:4700): ")
    tol=int(input("Enter the Tolerance(if there is no tolerance then enter NONE): "))
    def encoder_resistance(colour_string):
        d=colour_digi[int(original[0])]
        orig_len = len(original)
        if orig_len>=1:
            e=colour_digi[int(original[1])]
        else:
            e=10
        if f>=2:
            c=10**(len(original)-2)
        elif orig_len==1:
            original = original + "0"
            c=10
        else:
            c=1
        g=colour_multiplie[c]
        if tol not in colour_toleranc:
            print("Give the Valid Tolerance, If it has no toleranc give NONE")
        elif tol=="NONE":
            return 
        else:
            h=colour_toleranc[tol]
        print(f"{d} {e} {g} {h}")
    encoder_resistance(original)
else:
    print("Give the Valid Mode")
