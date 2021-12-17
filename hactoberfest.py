# input
while True:
    try:
        T = int(input("Enter the test case number: "))
        break
    except:
        print("Invalid input please try again")

while True:
    encrypted_msg = input(
        "Enter the encrypted message(Uppercase and Space omitted): ")
    if encrypted_msg.isupper() and ' ' not in encrypted_msg:
        break
    else:
        print("Invalid input please try again")

while True:
    key = input("Enter the key(Uppercase and Space omitted) : ")
    if key.isupper() and ' ' not in key:
        break
    else:
        print("Invalid input please try again")

# varables
key_extended = (key *(len(encrypted_msg)//len(key))) + key[:(len(encrypted_msg) % len(key))]
# ⬆ to make key as long as encrypted message.
decrypted_msg = ""
key_index = 0

# process
for en_chr in encrypted_msg:
    key_chr = key_extended[key_index]
    # ⬆ to change the key chr to coresponding key
    if (ord(en_chr)-65)-(ord(key_chr)-65) > -1:
        decrypted_msg += chr((ord(en_chr)-65)-(ord(key_chr)-65)+65)
    else:
        decrypted_msg += chr((26-((ord(en_chr)-65)-(ord(key_chr)-65))*-1)+65)
    key_index += 1

# output
print(f"Your decrypted message is: {decrypted_msg}.")
