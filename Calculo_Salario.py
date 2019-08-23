import math

n = input("Digite o número a ser convertido: ").upper()
n_base = 16 # n_base = int(input("Digite a base do número: "))

i = 0

base2 = []
base8 = []
base10 = 0
base16 = []

letra_base16 = {10: "A",
                11: "B",
                12: "C",
                13: "D",
                14: "E",
                15: "F",
                "A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15,}

# +=========================================================================+ #
# |                                  DECIMAL                                | #
# +=========================================================================+ #

if n_base == 10:
    
    # DECIMAL PARA BINÁRIO
    val = int(n)
    while True:
        if val >= 2:
            resto = val % 2
            base2.append(math.trunc(resto))
            
            val = val / 2
        else:
            base2.append(math.trunc(val))
            base2 = base2[::-1]
            break
    
    
    # DECIMAL PARA OCTAL
    val = int(n)
    while True:
        if val >= 8:
            resto = val % 8
            base8.append(math.trunc(resto))
            
            val = val / 8
        else:
            base8.append(math.trunc(val))
            base8 = base8[::-1]
            break
    
    
    # DECIMAL PARA HEXADECIMAL
    val = int(n)
    while True:
        if val >= 16:
            resto = val % 16
            if resto < 10:
                base16.append(math.trunc(resto))
            else:
                base16.append(letra_base16[math.trunc(resto)])
            
            val = val / 16
        else:
            if val < 10:
                base16.append(math.trunc(val))
            else:
                base16.append(letra_base16[math.trunc(val)])
            
            base16 = base16[::-1]
            break
    
    print("\nBASE 2:  ", *base2, sep="")
    print("BASE 8:  ", *base8, sep="")
    print("BASE 16: ", *base16, sep="")
    
# +=========================================================================+ #
# |                                  OCTAL                                  | #
# +=========================================================================+ #
    
elif n_base == 8:
    
    # OCTAL PARA BINÁRIO
    val = n
    
    for num in val:
        i = 2
        while i >= 0:
            num = int(num)
            if (num - 2**i) >= 0:
                num = num - 2**i
                base2.append(1)
            else:
                base2.append(0)
                
            i -= 1
    
    # se houve, remove os números '0' do começo do binário
    while base2[0] == 0:
        base2.remove(0)


    # OCTAL PARA DECIMAL
    val = n
    i = 0
    
    for num in val[::-1]:
        base10 += int(num) * (8**i)
        i += 1
    
    print("\nBASE 2:  ", *base2, sep="")
    print("BASE 10: ", base10)
    
# +=========================================================================+ #
# |                                HEXACIMAL                                | #
# +=========================================================================+ #
    
elif n_base == 16:
    
    # OCTAL PARA BINÁRIO
    val = n
    
    for num in val:
        i = 3
        while i >= 0:
            num = int(num)
            if (num - 2**i) >= 0:
                num = num - 2**i
                base2.append(1)
            else:
                base2.append(0)
                
            i -= 1
    
    # se houve, remove os números '0' do começo do binário
    while base2[0] == 0:
        base2.remove(0)
    
    
    # HEXADECIMAL PARA DECIMAL
    val = list(n)
    i = 0
    
    for num in val[::-1]:
        if num.isnumeric():
            num = int(num)
        else:
            num = letra_base16[num]
        
        base10 += int(num) * (16**i)
        i += 1
        
    print("\nBASE 2:  ", *base2, sep="")
    print("BASE 10: ", base10)
    
# BUILDING AREA - BE CAREFULL
