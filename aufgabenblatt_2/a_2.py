
def get_dez_for_word(word: str) -> list[int]:
    word_list = list(word)
    word_list_dez = [(ord(element.title()) - 64) for element in word_list]
    return word_list_dez


def print_decrypted_list_by_word(word_list_dez: list[int]):
    word_list = []
    for j, element in enumerate(C1_xor_C2):
        word_sub_list = []
        for i, letter in enumerate(word_list_dez):
            try:
                word_sub_list.append(chr(((C1_xor_C2[j + i]) ^ letter) + 64))
            except IndexError:
                break
        word_list.append(word_sub_list)

    for i, element in enumerate(word_list):
        print(str(i) + ": ", "".join(element))


C1_xor_C2 = [17, 4, 1, 26, 0, 24, 23, 23, 10, 1, 28, 19, 19, 15, 20, 30, 6, 11, 4, 8, 17, 29, 23, 1, 24, 23, 28, 17, 20,
             18, 9, 27, 17, 13, 13, 10, 13, 18, 7, 4, 22, 23, 10, 22, 13, 27, 8, 5, 28, 1, 23, 26, 19, 12, 6, 0, 8, 7,
             2, 15, 0, 3, 7, 0, 9, 7, 29, 19, 19, 3, 2, 29, 27, 8, 11, 7, 0, 6, 17, 26, 10, 26, 31, 26]



m1_kryptographie = list("*"*len(C1_xor_C2))
m2_sicherheit = list("*"*len(C1_xor_C2))

search_string = "CHLUESSELUNGVON"
print_decrypted_list_by_word(get_dez_for_word(search_string))

m2_sicherheit[5:5+len("SENZUSTANDVON")] = "SENZUSTANDVON"  # Ergibt sich aus dem Wort Kryptographie in m1
m1_kryptographie[5:5+len("KRYPTOGRAPHIE")] = "KRYPTOGRAPHIE"  # Ergibt sich aus dem Wort Sicherheit in m2
m1_kryptographie[18:18+len("WARURSPRUENGLICH")] = "WARURSPRUENGLICH"  # Ergibt sich aus dem Wort Sicherheit in m2
m2_sicherheit[18:18+len("SICHERHEITZUERREICHEN")] = "SICHERHEITZUERREICHEN"  # Ergibt sich aus dem Wort Kryptographie in m1
m1_kryptographie[18:18+len("WARURSPRUENGLICHDIEWI")] = "WARURSPRUENGLICHDIEWI"  # Ergibt sich aus dem Wort Sicherheit in m2
m1_kryptographie[45:45+len("HAFTDERVER")] = "HAFTDERVER"  # Ergibt sich aus dem Wort Sicherheit in m2
m1_kryptographie[18:18+len("WARURSPRUENGLICHDIEWISSENSCHAFT")] = "WARURSPRUENGLICHDIEWISSENSCHAFT"  # Ergibt sich aus dem Wort Sicherheit in m2
m2_sicherheit[37:37+len("ENWERDENSICH")] = "ENWERDENSICH"  # Ergibt sich aus dem Wort Kryptographie in m1
m1_kryptographie[0:0+len("DIESEKRY")] = "DIESEKRY"
m2_sicherheit[0:0+len("UMDIESEN")] = "UMDIESEN"  # Ergibt sich aus dem Wort Kryptographie in m1
m2_sicherheit[43:43+len("ENSICHERHEIT")] = "ENSICHERHEIT"  # Ergibt sich aus dem Wort Kryptographie in m1
m2_sicherheit[52:52+len("EITSKONZEPTEERST")] = "EITSKONZEPTEERST"
m1_kryptographie[52:52+len("VERSCHLUESSELUNG")] = "VERSCHLUESSELUNG"  # Ergibt sich aus dem Wort Kryptographie in m1
m1_kryptographie[52:52+len("VERSCHLUESSELUNGVONI")] = "VERSCHLUESSELUNGVONI"  # Ergibt sich aus dem Wort Kryptographie in m1
m2_sicherheit[71:71+len("TUNDUMGESETZT")] = "TUNDUMGESETZT"
m1_kryptographie[71:71+len("INFORMATIONEN")] = "INFORMATIONEN"
m2_sicherheit[56:56+len("KONZEPTEERSTELL")] = "KONZEPTEERSTELL"

print("".join(m1_kryptographie))
print("".join(m2_sicherheit))

ergebnis = ("DIESE KRYPTOGRAPHIE WAR URSPRUENGLICH DIE WISSENSCHAFT DER VERSCHLUESSELUNG VON INFORMATIONEN"
            "UM DIESEN ZUSTAND VON SICHERHEIT ZU ERREICHEN WERDEN SICHERHEITSKONZEPTE ERSTELLT UND UMGESETZT")