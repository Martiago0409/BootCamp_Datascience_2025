#Parte 1 / Normalizacion de datos

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

#Normalizamos los datos en users
for i in range(len(users)):
    for j in range(len(users[i])):
        if isinstance(users[i][j], str):
            users[i][j]=users[i][j].lower().strip().replace("_"," ")

        if isinstance(users[i][j], str) and users[i][j].isdigit():
             users[i][j]=int(users[i][j])

        if isinstance(users[i][j], float):
            users[i][j]=int(users[i][j])
        
        if isinstance(users[i][j], list):
            for k in range(len(users[i][j])):
                if isinstance(users[i][j][k], str):
                    users[i][j][k]=users[i][j][k].lower()

print(*users, sep="\n")

#Parte 2 / 
       
    
    

       


