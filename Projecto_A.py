import math

def Main(): # função principal 
    MainMenu()
    
    
    
    
    
def MainMenu(): # Menu principal 
    
    print("What problem do you want to solve? ")
    print("1. Floatation ")
    print("2. Springs")
    
     
    while(True):
        
        # Verifica a resposta
        a = input() # resposta
    
        if (a == "1"):
            Problem1()
            break
        elif (a == "2"):
            Problem2()
            break
        else:
            print("choose between 1 or 2, to solve a problem: ")
       

def Problem1(): ## Flutuação 

    print("Insert the Gravity: ")
    G = float(input()) # Gravidade
    print("Insert fluid density ")
    DF = float(input()) # Densidade do Fluido
    print("Insert object density")
    DO = float(input()) # Densidade do Objeto (P)
    print("Insert the Volume")
    V = float(input()) # Volume
    
     
    
    # Variaveis
    M = float() # Massa
    FG = float() # Força Gravítica 
    FB = float() # Volume de baixo de agua 
    A = float() # area 
    C = float() # Calado
    F = float() # auxiliar (arestas)

    while (True):
        
    
        # Calcular a Massa  
        M = DO * V

        print("Object Properties: Mass = " + str(M),  "Density = ", str(DO),   "Volume = " + str(V))
        print("Fluid has density of " + str(DF),  "Gravity is " + str(G))
         

        
        # Força gravítica
        FG = M * G 
        # Volume do objeto de baixo de agua 
        FB = FG / (DF * G)  # volume do objeto de baixo de agua 
        # Calado
        F =  V**(1/3)
        C = FB / (F * F) 
        
        print("The Object would float at: " +  str(C) + " meters")

        print("1. Set Gravity: ")
        print("2. Set Fluid Density: ")
        print("3. Set Object Density: ")
        print("4. Set Volume: ")
        print("5. Set Mass: ")

        response = input()
                
        if(response == "1"):
            G = float(input("Inset the new Gravity: \n"))
        elif(response == "2"):
            DF = float(input("Insert the new Fluid Density: \n")) 
        elif(response == "3"):
            DO = float(input("Insert the new Object Density: \n "))
        elif(response == "4"):
            V = float(input("Insert the new Volume: \n"))
            M = DO * V 
        elif(response == "5"):
            M = float(input("Insert the new Mass: \n"))
            V = M / DO
        else:
            print("Type 1-4 to set a new parameter.")
    
        
def Problem2(): ## Molas
    
    print("Insert the Gravity: ")
    ForçaGravítica = float(input()) # gravidade 
    print("Insert the Mass: ")
    M = float(input()) # Massa do corpo
    print("Insert the Constant: ")
    K = float(input()) # Constante de mola
    print("Insert the base spring length: ")
    R = float(input()) # Comprimento da mola em descanso 


    #Variaveis 
    L = float() # Comprimento da mola esticada  
    Fg = float() # força gravítica 
    add = float() # Cálculos axilares

    
    
    while (True): 

        print("Object mass is: " + str(M), "Gravity is: ", str(ForçaGravítica))
        print("Base spring length is: " + str(R), "Constant = " + str(K)) 
        Fg = M * ForçaGravítica # Força Gravítica 
        add = (- K * -R) + -Fg ## formula
        L = add / K # Comprimento da mola esticada 
        print("Spring would stretch to: " + str(L) + " meters")
        
        print("1. Set Mass:")
        print("2. Set Constant:")
        print("3. Set Gravity:")
        print("4. Set Length:")

        response = input() # input da resposta 
 
        if( response == "1"): # Modifica a massa
            M = float(input("Insert the new Mass: \n"))
        elif(response == "2"): # Modifica a constante 
            K = float(input("Insert the new Constant: \n"))
        elif(response == "3" ): # Modifica a gravidade 
            ForçaGravítica = float(input(  print("Insert the new Gravity: \n")))
        elif( response == "4"): # Modifica o comprimento da mola em descanso   
            R = float(input(print("Insert the new Length: \n")))
        else:
            print("Type 1-4 to set a new parameter.")
            
Main() # Chama a função principal 