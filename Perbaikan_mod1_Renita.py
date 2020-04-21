# No. 1 
# def find_short(s):
#     text = s.split()
#     jmlh_hrf = 1000
#     for i in text:
#         if len(i) < jmlh_hrf:
#             jmlh_hrf = len(i)
#     return jmlh_hrf

# print(find_short("Many people get up early in the morning"))
# print(find_short("Every office would getting newest monitor"))
# print(find_short("Create new file after this morning"))

# No. 2
def persistence(n) :
    angka = n
    pengulangan = 0
    while (len(str(angka)) > 1):
        hasil_kali = 1
        for i in str(angka) :
            hasil_kali *= int(i)
        angka = hasil_kali
        pengulangan += 1
    return pengulangan

print(persistence(39))
print(persistence(999))
# print(persistence(4))

# No 3
# def multiplication_table(row,col):
#     z = ''
#     for i in range(1, row+1):
#         for j in range(1, col+1):
#             z += str(i*j) + ' '
#         if i != row:
#             z += '\n'
#     return z

# print(multiplication_table(3,3)) 
# print(multiplication_table(5,3))
# print(multiplication_table(3,5))

# No 4
# def alphabet_position(text):
#     posisi = ''
#     a = text.lower()
#     dict_alph = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
#     for alphabet in a:
#         if alphabet in dict_alph.keys():
#             posisi += str(dict_alph[alphabet])
#             posisi += ' '
#     return posisi

# print(alphabet_position("The sunset sets at twelve o'clock"))
# print(alphabet_position("it’s never too late to try"))
# print(alphabet_position("Have you done your homework?"))