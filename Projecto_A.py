def Main():
    MainMenu()
    
    
    
    
    
def MainMenu():
    
    print("What problem do you want to solve? ")
    print("1. Floatation ")
    print("2. Springs")
    
    
    if input() == "1":
        Problem1()
    elif input()== "2":
        Problem2()
        

def Problem1(): ## Flutuação 

    print("Insert de Gravity: ")
    G = float(input()) # Gravidade
    print("Insert ")
    DF = float(input()) # Densidade do Fluido
    DO = float(input()) # Densidade do Objeto
    V = float(input() # Volume 
    

    ## Formula Fb = P.G.V

    while (True):
        print("Object Properties: Mass =" + str() + "Density=" + str() +  "Volume ="+ str(V))
        print("Fluid has density of " + str() + "Gravity is" + str())
         
        
        

    
    
    
    
        
def Problem2(): ## Molas
    
    print("Insert the Gravity: ")
    ForçaGravítica = float(input()) # gravidade 
    print("Insert de Mass: ")
    M = float(input()) # Massa do corpo
    print("Insert the Constant: ")
    K = float(input()) # Constante de mola
    print("Insert the base spring length: ")
    R = float(input()) # Comprimento da mola em descanso 
    L = float() # Comprimento da mola esticada  
    Fg = float() # força gravitica 
    Fg = M * ForçaGravítica # Força Gravítica 
    add = float() # Cálculos axilares

    print(Fg)
    
    while (True):
        

        print("Object mass is: " + str(M), "Gravity is: " + str(ForçaGravítica))
        print("Base spring length is: " + str(R), "Constant = " + str(K)) 

        add = (- K * -R) + -Fg ## formula 
        print(add)
        L = add / K
        print("Spring would stretch to: " + str(L))
        
        response = input()

        if(response == "Set Mass ".split()):
            M = float(response) 
            print(M)
        elif(response == "Set Constant ".split()):
            K = response
        elif(response == "Set Gravity" ):
            ForçaGravítica = response
        elif( response == "Set Length "):    
            R = response
        
        

        

        


        
        

    


Main()