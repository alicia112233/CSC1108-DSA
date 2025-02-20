def reverse():
    ch = input()
    if ch != 'end':
        reverse()
    print (ch)

reverse()

# recursive calls? with input 'a', 'b', 'c', 'end' 
# total recursive calls = 4