charizard = 90
feraligatr = 95
modifier = round((1 * 1 * 1 * 2 * 0.85 * 1.5 * 0.25 ),2)
damage = round(((((((2*90)/5)+2)*110*(205/188))/50)+2),2)
tdamage = round ((damage * modifier),2)
print('Damage Dealt: ', tdamage)
