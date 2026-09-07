import requests
import qrcode

user = input("Digite o nome do perfil: ").strip()
url = 'https://github.com/'+ user


resposta = requests.get(url)

if resposta.status_code == 200:
    print("Perfil encontrado")

    gerar_qr=input("Deseja gerar seu QRcode?  s/n ").lower().strip()

    if gerar_qr== 's':
        local = 'C:\\Users\\adres\\OneDrive\\Projetos\\QRcode\\'+ user + '.png '

        qr = qrcode.QRCode()
        qr.add_data(url)

        img = qr.make_image()
        img.save(local)
        img.show()
        print(url)
    else:
        print("Encerrando o programa")  
else:
    print("Perfil não encontrado")
      


  



