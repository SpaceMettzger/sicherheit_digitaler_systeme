

probs = {"A": 6.51, "N": 9.78, "B": 1.89, "O": 2.51, "C": 3.06, "P": 0.79, "D": 5.08, "Q": 0.02, "E": 17.40, "R": 7.00,
         "F": 1.66, "S": 7.27, "G": 3.01, "T": 6.15, "H": 4.76, "U": 4.35, "I": 7.55, "V": 0.67, "J": 0.27, "W": 1.89,
         "K": 1.21, "X": 0.03, "L": 3.44, "Y": 0.04, "M": 2.53, "Z": 1.13}

sorted_probs = {k: v for k, v in sorted(probs.items(), key=lambda item: item[1], reverse=True)}
print("Relative hauefigkeit der Buchstaben des Alphabets")
print(sorted_probs, "\n")
prob_sorted_letters = [k for k in sorted_probs.keys()]


krypt1 = "GPSBO NLPZB RPJIN LPRZE KNLPR ZFKHJ RPBPZ CHKSY PWYIL ZPCPZ ZYZR BJPBB NLHOP BBPHB TOPZY BNLHO PBBPH Z"
krypt2 = ("PBRBY QKLSQ RSHRP XPZJK BHPXP ZZRNL YQPRH QRSKZ BHPXP ZBIZJ PSZQP RHQRS KZBHR PXPZA PQIPL ZYBRZ JPBRB YRFFP "
          "SPYQK BQKLZ BRZZR ZJPSH RPXPP BRBYK XPSRF FPSKO NLPYQ KBGPS ZOZEY RFQKL ZBRZZ")

# Erstes Wort von krypt 1 ist "versuchen"
krypt1 = krypt1.replace(" ", "")
str_versuchen = "versuchen"

# Erste 7 Zeichen des krypt1 den Buchstaben aus dem Wort "versuchen" zuordnen
cypher_part = {}
for i, char in enumerate(str_versuchen):
    if char not in cypher_part:
        cypher_part[char] = krypt1[i]

cypher = {}

# Sortierung umkehren, um später einfacher damit arbeiten zu können
for key, value in cypher_part.items():
    cypher[value] = key

print("Teilchiffe durch das Wort 'Versuchen' erkannt:")
print(cypher, "\n")

# Häufigkeit der Buchstaben in krypt1 zählen
krypt1_dict = {}
for char in krypt1:
    if char not in krypt1_dict:
        krypt1_dict[char] = 1
    else:
        krypt1_dict[char] += 1

# Dictionary der Anzalh der Buchstaben nach Häufigkeit sortieren
sorted_krypt_1 = {k: v for k, v in sorted(krypt1_dict.items(), key=lambda item: item[1], reverse=True)}
print("Häufigkeit der Buchstaben von krypt1:")
print(sorted_krypt_1, "\n")
sorted_krypt_1_letters = [k for k in sorted_krypt_1.keys()]

# Restliche Buchstben werden anhand ihrer häufigkeit in krypt1 verglichen mit der generellen häufigkeit der Buchstaben
# im Alphabet der chiffre hinzugefügt
for i, letter in enumerate(sorted_krypt_1_letters):
    if letter not in cypher.keys():
        cypher[letter] = prob_sorted_letters[i]

# krypt1 wird mit der chiffre weitestgehend entschlüsselt (kleine Buchstaben sind sicher bekannt, große sind unklar)
decoded_krypt = []
for letter in krypt1:
    decoded_krypt.append(cypher[letter])

print("Teilweise entschlüsselte Botschaft aus krypt1:")
print("".join(decoded_krypt), "\n")

# Der rest des Klartexts wird manuell entschlüsselt:

print("Manuell vollständig entschlüsstelte Botschaft aus krypt1")
krypt1_entschluesselt = ("versuchen sie doch einfach einmal diesen klartext ohne kenntnis des schluessels zu "
                         "entschluesseln\n")
print(krypt1_entschluesselt)

krypt1_entschluesselt = krypt1_entschluesselt.replace(" ", "")

# Mit dem entschlüsselten krypt1 kann eine genauere chiffre erstellt werden:

cypher_new = {}
for i, char in enumerate(krypt1):
    if char not in cypher_new:
        cypher_new[char] = [*krypt1_entschluesselt][i]

print("Neue chiffre aufgrund der entschlüsselten Botschaft krypt1:")
print(cypher_new, "\n")

krypt2 = krypt2.replace(" ", "")

krypt2_dict = {}
for char in krypt2:
    if char not in krypt2_dict:
        krypt2_dict[char] = 1
    else:
        krypt2_dict[char] += 1
sorted_krypt_2 = {k: v for k, v in sorted(krypt2_dict.items(), key=lambda item: item[1], reverse=True)}
print("Häufigkeit der Buchstaben von krypt2:")
print(sorted_krypt_2, "\n")
sorted_krypt_2_letters = [k for k in sorted_krypt_2.keys()]

cypher_krypt_2 = cypher_new
for i, letter in enumerate(sorted_krypt_2_letters):
    if letter not in cypher_krypt_2.keys():
        cypher_krypt_2[letter] = prob_sorted_letters[i]

decoded_krypt_2 = []
for letter in krypt2:
    decoded_krypt_2.append(cypher_krypt_2[letter])

decrypted_2 = []
for char in krypt2:
    try:
        decrypted_2.append(cypher_krypt_2[char])
    except KeyError:
        decrypted_2.append(char)

print("krypt2 entschlüsselt mit dem Schlüssel aus krypt1:")
print("".join(decrypted_2))

krypt_2_decoded = ("es ist wahr wir lieben das leben nicht weil wir ans leben sondern weil wir ans lieben gewoehnt sind "
                   "es ist immer etwas wahnsinn inder liebe es ist aber immer auch etwas vernunft im wahnsinn")
