import time

# Verificar se o valor lido é 10 % maior que a média
# equação valor > media = media + (media x 0.10)


valor=0
media=0
cont = 1
while True:
    
    valor = int(input("valor :>"))
    media = media + valor / cont
    nova_media = media + (media * 10 / 100)
    if valor > nova_media:
        print("cont", cont, "Media = ", media, "Valor",valor, " excede limite de 10% ", nova_media)
    
    else:
        print("cont", cont,"Media = ", media, "Valor",valor, "nova", nova_media)
    cont += 1
    time.sleep(3)
