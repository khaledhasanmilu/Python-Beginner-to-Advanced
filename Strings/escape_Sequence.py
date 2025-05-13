str ="Khlaid is\n a good\n \"boy\""
print(str)

user = input("Enter your name:")
print(f"Good Afternoon, {user}")

letter = '''  Dear <|Name|>,
             You are selected! 
            <|Date|> ''' 
#name = input("Your name ")
print(letter.replace("<|Name|>","khaled").replace("<|Date|>","14 May,2030"))