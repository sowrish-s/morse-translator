
#morse dictionary

morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# text to morse

def t2m(text):
    words=text.split()
    encoded=[]
    for word in words:
        enc_chars=[]
        for char in word.upper():
            if char in morse:
                enc_chars.append(morse[char])
            else:
                enc_chars.append("?")
        encoded.append(' '.join(enc_chars))
    return '   '.join(encoded)

# morse to text

def m2t(morcode):
    m2c={v:k for k, v in morse.items()}
    parts=morcode.split()
    decoded=[]
    for code in parts:
        if code in m2c:
            decoded.append(m2c[code])
        else:
            decoded.append("?")
    return ' '.join(decoded)

# main
n=int(input("How many times do you want to translate? : "))
for i in range(n):
    print("Choose an option.")
    print("1. Text to Morse")
    print("2. Morse to Text")
    choice=int(input("Enter your choice : "))
    if choice==1:
        t=input("Enter text you want to convert : ")
        a=t2m(t)
        print(a)
    elif choice==2:
        m=input("Enter morse you want to translate : ")
        a=m2t(m)
        print(a)
    else:
        print("Invalid input, enter either 1 or 2.")
