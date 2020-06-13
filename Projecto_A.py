def Main():
    MainMenu()
    
    
    
    
    
def MainMenu(): # Menu principal 
    
    print("What problem do you want to solve? ")
    print("1. Floatation ")
    print("2. Springs")
    
    
    if input() == "1":
        Problem1()
    elif input()== "2":
        Problem2()
       
"""
def Problem1(): ## Flutuação 

    print("Insert de Gravity: ")
    G = float(input()) # Gravidade
    print("Insert fluid density ")
    DF = float(input()) # Densidade do Fluido
    print("Insert object density")
    DO = float(input()) # Densidade do Objeto
    print("Insert de side of cube")
    L = float(input()) # Aresta do cubo
    V = float() # Volume
    V = L * L * L 
     
    
    # Variaveis
    M = float() # Massa
    FG = float() # Força Gravítica 
    FB = float() # força Buoyancy
    A = float() # area 
    C = float() # Calado



    

    ## Formula Fb = P.G.V

    while (True):
        
        print("Object Properties: Mass =" + str(M) + "Density=" + str(DO) +  "Volume ="+ str(V))
        print("Fluid has density of " + str(DF) + "Gravity is" + str(G))
         
        # Formula para o Volume
        V = L * L * L 

        # Calcular a Massa  
        M = DO * V
        # Calcular o Volume 
        V = M/ DO
        
        # Força gravítica
        FG = M * G
        # Força de Buoyancy
        FB = FG / (DF * G)
        # Calado 
        C = FB / (L * L)

        response = input()

        if():

 """
    
    
    
        
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
    add = float() # Cálculos axilares

    print(Fg)
    
    while (True):
        
        X = str()
        

        print("Object mass is: " + str(M), "Gravity is: " + str(ForçaGravítica))
        print("Base spring length is: " + str(R), "Constant = " + str(K)) 
        Fg = M * ForçaGravítica # Força Gravítica 
        add = (- K * -R) + -Fg ## formula 
        L = add / K # Comprimento da mola esticada 
        print("Spring would stretch to: " + str(L))
        
        print("1. Set Mass:")
        print("2. Set Constant:")
        print("3. Set Gravity:")
        print("4. Set Length:")

        response = input() # input da resposta 
 
        if( response == "1"): # Modifica a massa
            print("Insert the new Mass: ")
            M = float(input())
        elif(response == "2"): # Modifica a constante 
            print("Insert the new Constant: ")
            K = float(input())
        elif(response == "3" ): # Modifica a gravidade 
            print("Insert the new Gravity: ")
            ForçaGravítica = float(input())
        elif( response == "4"): # Modifica o comprimento da mola em descanso 
            print("Insert the new Length: ")    
            R = float(input())
            
Main() # Chama a função principal 
        
        

        

        


        
        

    

