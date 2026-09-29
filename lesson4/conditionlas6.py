for x in range(2, 101):
    Tub_son=True

    for i in range(2,x):
        if x%i==0:
            Tub_son=False
            break


    if Tub_son:
        print(x)      
        