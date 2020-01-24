import hashlib
import os

def encrypt():
    # type: () -> object                        # -> SoeltanRadjaMaerlendo
    text = input("Masukan Teks : ")             # -> DarkPhp :v
    print()

    result1 = hashlib.md5(text.encode())
    result2 = hashlib.blake2b(text.encode())
    result3 = hashlib.blake2s(text.encode())
    result4 = hashlib.shake_128(text.encode())
    result5 = hashlib.shake_256(text.encode())
    result6 = hashlib.sha1(text.encode())
    result7 = hashlib.sha224(text.encode())
    result8 = hashlib.sha256(text.encode())
    result9 = hashlib.sha384(text.encode())
    result10 = hashlib.sha512(text.encode())
    result11 = hashlib.sha3_224(text.encode())
    result12 = hashlib.sha3_384(text.encode())
    result13 = hashlib.sha3_256(text.encode())
    result14 = hashlib.sha3_512(text.encode())


    print('Tadaaaa ! text is encrypt ')
    print('=========================\n')
    print('MD5 : ', result1.hexdigest())
    print("\n")
    print('BLAKE 2B : ', result2.hexdigest())
    print("\n")
    print('BLAKE 2S :', result3.hexdigest())
    print("\n")
    print('SHAKE 128 :', result4.hexdigest(999))
    print("\n")
    print('SHAKE 256 :', result5.hexdigest(999))
    print("\n")
    print('SHA 1 :', result6.hexdigest())
    print("\n")
    print('SHA 224 :', result7.hexdigest())
    print("\n")
    print('SHA 256 :', result8.hexdigest())
    print("\n")
    print('SHA 384 :', result9.hexdigest())
    print("\n")
    print('SHA 512 :', result10.hexdigest())
    print("\n")
    print('SHA 3 224 :', result11.hexdigest())
    print("\n")
    print('SHA 3 384 :', result12.hexdigest())
    print("\n")
    print('SHA 3 256 :', result13.hexdigest())
    print("\n")
    print('SHA 3 512 :', result14.hexdigest())
    input('>>>')
    os.system('cls')
    return start()


def jenis():
    print("""[ BERIKUT ADALAH JENIS ALGORITMA YANG DIDUKUNG ]""")
    y = 0
    for x in hashlib.algorithms_guaranteed:
        y += 1
        print('Algoritma ke', y, ':', x)
    input('>>>')
    start()


def tentang():
    print("""
    -> Halo ini adalah program yang saya buat (sultan raja marlindo)
    -> ini adalah kode yang saya buat dari website2 belajar python
    -> ok semoga hari anda menyenangkan ^_^ """)
    input('>>>')
    os.system('cls')
    start()

def start():
    print("""
        =======================
        [ AMANKAN TEKS ANDA ]
        =======================
        1. Mengunci Teks    <-
        ->    2. Jenis Alogaritma
        3. Tentang  <-""")
    pilih = input('>>> ')
    if int(pilih) == 1:
        encrypt()
    elif int(pilih) == 2:
        jenis()
    elif (pilih) == 3:
        tentang()
    else:
        print('Pilihan Tidak Ada !')
        start()


if __name__ == start():
    run()
