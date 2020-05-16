import numpy as np
import random
import matplotlib.pyplot as plt
def conver_data(plants, pole_pocva_frontend, pole , pole_pocva ,kol_pocv, vid):
    real_plants = []
    for i in plants:
        m = obrabotka(i)
        m.append(plants[i])
        m.append(1)
        m.append(vid[plants[i]][0])
        real_plants.append(m)
        
    for i in pole_pocva_frontend:
        m = obrabotka(i)
        pole_pocva[m[0],m[1]] = pole_pocva_frontend[i]
    for i in pole_pocva_frontend:
        m = obrabotka(i)
        pole[m[0],m[1]] = kol_pocv[pole_pocva_frontend[i]]
        
    return real_plants,pole_pocva,pole


def obrabotka(x_y):
    num_out_of_line = []
    num =[]
    real_x_y = ""
    for i in range(len(x_y)):
        if x_y[i] in "0123456789":
            real_x_y += x_y[i]
            try:
                if x_y[i+1] not in "0123456789":
                   num_out_of_line.append(real_x_y)
                   real_x_y = ""
            except:
                   num_out_of_line.append(real_x_y)
    real_x_y = list(map(int, num_out_of_line))
    return real_x_y

def convert_just(plants):
    plants_0 = []
    plants_1 = []
    for i in plants:
        
        if i[2] == 0:
            plants_0.append(i)
        else:
            plants_1.append(i)
            
    return len(plants_0),len(plants_1)

#работает корректно 
def convert_children(new_new_children,plants,vid,pole,pole_pocva):
    bol = True

    
    for i in new_new_children:
        for j in plants:
            
            
            if i[0] == j[0] and i[1] == j[1]:
              
                if pole_pocva[i[0],i[1]] == vid[i[2]][5]:
                    pole[i[0],i[1]]+= i[4]
                bol = False
                break

            
        if  bol :
            plants.append(i)
        bol = True
 
    return plants, pole
        
            
#создаём список координат, в которые будут падать дети
def rand_children(element,semena,pole,vid,plants):
    bol = True
    slovar_detei = {}
    child = []
    p = len(pole)-1
    q = len(pole[0])-1
    rand = []
    prom_child2 =''
    if element[4] - semena * vid[element[2]][0] > 0:
        semena = vid[element[2]][4]
    else:
        semena = int(element[4] / vid[element[2]][0])-1
    if element[0] == 0 and element[1]== 0:
        rand =[[element[0]+1, element[1]+1],[element[0]+1,element[1]],[element[0],element[1]+1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False


    elif bol and element[0] == q and element[1] == 0:
        rand =[[element[0]-1, element[1]], [element[0]-1,element[1]+1],[element[0],element[1]+1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False

    elif bol and element[0] == 0 and element[1]== q :
        rand =[[element[0]+1, element[1]], [element[0],element[1]-1],[element[0]+1,element[1]-1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False

    elif bol and element[0] == p and element[1]== q:
        rand =[[element[0]-1, element[1]], [element[0]-1,element[1]-1],[element[0],element[1]-1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False
        
    elif bol and element[0]== 0 and (0 < element[1] < q):
        rand =[[element[0], element[1]-1], [element[0],element[1]+1],[element[0]+1,element[1]-1],
               [element[0]+1,element[1]],[element[0]+1,element[1]+1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False
        
    elif bol and  element[1]== q and ( 0 < element[0] < p):
        rand =[[element[0]-1, element[1]-1], [element[0]-1,element[1]],[element[0],element[1]-1],
               [element[0]+1,element[1]-1],[element[0]-1,element[1]]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False
        
    elif bol and  element[1]== 0 and ( 0 < element[0] < p):
        rand =[[element[0]-1, element[1]], [element[0]-1,element[1]+1],[element[0],element[1]+1],
               [element[0]+1,element[1]+1],[element[0]-1,element[1]+1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False
        
    elif bol and  element[0]== p and ( 0 < element[1] < q):
        rand =[[element[0]-1, element[1]-1], [element[0]-1,element[1]],[element[0]-1,element[1]+1],
               [element[0],element[1]+1],[element[0],element[1]-1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
        bol = False
    else:
        rand = [[element[0]-1,element[1]-1],[element[0]-1,element[1]],[element[0],element[1]-1],[element[0]-1,element[1]+1],[element[0]+1,element[1]-1],[element[0]+1,element[1]],[element[0],element[1]+1],[element[0]+1,element[1]+1]]
        for i in range(semena):
             prom_child2 = str(random.choice(rand))
             if prom_child2 in slovar_detei:
                 slovar_detei[prom_child2] +=1
             else:
                 slovar_detei[prom_child2] = 1
                
    if slovar_detei != {}:
        for i in slovar_detei:
            x_y = obrabotka(i)
            child.append([x_y[0], x_y[1],element[2],1,int(slovar_detei[i]*vid[element[2]][0])])
    return child, semena

#определяем, умерло ли растение от голода (нехватки еды в поле)
def food_and_dead_after(element,pole,vid,dead_index,pole_pocva):
    dead_plants = -1
    if (pole[element[0],element[1]] - vid[element[2]][1]) <= 0 or (pole_pocva[element[0],element[1]] != vid[element[2]][5]) :
        dead_plants = dead_index
            
    if dead_plants == dead_index:
        
        return dead_plants
    
    else:
        
        return -1
    
def next_step(plants,vid,pole,dead_plants):
    new_plants = []
    
    for i in dead_plants:
        plants[i] = "0"
    
    for i in range(len(plants)):
        
        
        
        if plants[i] != "0":
            plants[i][3] += 1
            new_plants.append(plants[i])
            
    for i in new_plants:
        i[4]+= vid[i[2]][1]
        pole[i[0],i[1]] -= vid[i[2]][1]

    
    return  pole,new_plants


#главная функция
def dly(plants, pole,vid,pole_pocva):
    
    dead_plants = []
    dead_index = 0
    new_children  = []
    new_new_children = []
    new_pole_pocva = pole_pocva
    fact_dead = False
    proverka_vida = (vid[0][5]==vid[1][5]) 
    for i in plants:
        #рождение детей и отнимание массы определенного растения        
        if i[3] == vid[i[2]][3]:
            prom_peremen = rand_children(i,vid[i[2]][4],pole,vid,plants)
            new_children=prom_peremen[0]
            i[4]-=vid[i[2]][0]*prom_peremen[1]
        
        if food_and_dead_after(i,pole,vid,dead_index,pole_pocva) != -1:
            fact_dead = True
            
        if i[3] == vid[i[2]][2] or fact_dead:
            
            if  vid[i[2]][5] == 1 and   not proverka_vida : 
                    new_pole_pocva[i[0],i[1]] = 0
          
            
            if vid[i[2]][5] == 0 and   not proverka_vida :
                    new_pole_pocva[i[0],i[1]] = 1
                    
            pole[i[0],i[1]] +=  i[4]
            dead_plants.append(dead_index)
            
        dead_index += 1
        fact_dead = False
        for i in new_children:
            new_new_children.append(i)

    new_children = convert_children(new_new_children,plants,vid,pole,pole_pocva)
    
    
    pole = new_children[1]
    plants = new_children[0]
    prom = next_step(plants,vid,pole,dead_plants)
    pole = prom[0]
    plants = prom[1]
    pole_pocva = new_pole_pocva
    
    return pole,plants,pole_pocva

def new_generation(plants,pole,vid,pole_pocva):
    
    prom = []
    
    prom = dly(plants,pole,vid,pole_pocva)
    pole = prom[0]
    plants = prom[1]
    pole_pocva = prom[2]

    plants_for_vision = []
    for i in plants:
        plants_for_vision.append(i[0:3])

    return plants,pole,pole_pocva,plants_for_vision