
def print_number_text(number):

    dict_yekane =   {   "0": "sefre" ,
                        "1" : "yek",
                        "2" : "do",
                        "3" : "se" ,
                        "4" : "chahar",
                        "5" : "pange",
                        "6" :"shesh",
                        "7" : "hafte",
                        "8" : "hasht",
                        "9" : "noh",
                        "10": "dah"}

    dict_dahgne =   {   "1" : "dah",
                        "2" : "bist",
                        "3" : "si" ,
                        "4" : "chehel",
                        "5" : "pangah",
                        "6" :"shast",
                        "7": "haftad",
                        "8": "hashtad",
                        "9" : "navad"}

    dict_sadgane =  {   "1" : "sad",
                        "2" : "devist",
                        "3" : "sesad" ,
                        "4" : "chaharsad",
                        "5" : "pansad",
                        "6" :"sheshsad",
                        "7": "haftesad",
                        "8": "hashtsad",
                        "9" : "nohsad"}

    dict_dahgane_taki = {"11" : "yazdah",
                         "12" : "davazdah",
                         "13" : "sisdah",
                         "14" : "chahardah",
                         "15" : "panzdah",
                         "16" : "shanzdah",
                         "17" : "hevdah",
                         "18" : "hegdah",
                         "19" : "nozdah",
                         "20" : "biste"}

    
    if int(number) <= 10:
        return dict_yekane[number]
    
    
    elif int(number) < 20:
        return dict_dahgane_taki[number]
    
    
    elif int(number) < 100:
        return f"{dict_dahgne[number[0]]}o {print_number_text(number[1])}" if number[1] != "0" else dict_dahgne[number[0]] 
    

    elif int(number) < 1_000:

        return f"{dict_sadgane[number[0]]}o {print_number_text(number[1:])}" if number[1:] != "00" else dict_sadgane[number[0]]
    
    
    elif int(number) < 1_000_000:
        return f"{print_number_text(number[:-3])} hezaro {print_number_text(number[-3:])}" if number[-3:] != '000' else f"{print_number_text(number[:-3])} hezar"
    
    
    elif int(number) < 1_000_000_000:
        return f"{print_number_text(number[:-6])} meliyono {print_number_text(number[-6:])}" if number[-6:] != '000_000' else f"{print_number_text(number[:-6])} meliyone"
    

    elif int(number) < 1_000_000_000_000:
        return f"{print_number_text(number[:-9])} meliyardo {print_number_text(number[-9:])}" if number[-9:] != '000_000_000' else f"{print_number_text(number[:-9])} meliyard"
    

    elif int(number) < 1_000_000_000_000_000:
        return f"{print_number_text(number[:-12])} biliyono {print_number_text(number[-12:])}" if number[-12:] != '000_000_000_000' else f"{print_number_text(number[:-12])} biliyon"


    elif int(number) < 1_000_000_000_000_000_000:
        return f"{print_number_text(number[:-15])} tiriliyono {print_number_text(number[-15:])}" if number[-15:] != '000_000_000_000_000' else f"{print_number_text(number[:-15])} tiriliyon"



while 1 :

    number = input("enter a number: ")
    text = print_number_text(number)
    print(text)
