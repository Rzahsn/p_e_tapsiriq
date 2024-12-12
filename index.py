
while True:
    
    try:
        ad,soyad,ata,university,login,parol = input().split()
    
    except ValueError:
        print("Verilənləri düzgün daxil edin")
        break
    
    a = open("db.txt" , "r")
    b=a.read()
    a.close()

    f = open("db.txt","a")
    if b.count(login) == 0:
        
        if len(ad) < 25 and len(soyad) < 25 and len(ata) < 25 and len(login) < 25 and len(parol) < 25:
            f.write(ad+" "+soyad+" "+ ata+" "+university+" "+login+" "+parol+"\n")
            print("Əlavə olundur!")

        else:
            print("Uzunluq 25-den kicik olmalidir")
    else:
        print("Istifadeci movcuddur")

    f.close()

    
    

