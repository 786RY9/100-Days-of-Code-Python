import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# def encrypt(original_text, shift_amount):
#     encrypted_text = ''
#     for s in original_text:
#         if s ==' ':
#             encrypted_text+=' '
#         else:
#             original_index = alphabet.index(s)
#             shift_to_index = original_index + shift_amount
#             encrypted_text+=alphabet[shift_to_index%len(alphabet)]
    
#     print(encrypted_text)

# def decrypt(encrypted_text, shift_amount):
#     original_text = ''
#     for s in encrypted_text:
#         if s ==' ':
#             original_text+=' '
#         else:
#             original_index = alphabet.index(s)
#             shift_to_index = original_index - shift_amount
#             original_text+=alphabet[shift_to_index%len(alphabet)]
    
#     print(original_text)


def caesar(original_text,shift_amount,encode_or_decode):
    ot = original_text
    original_text = ''
    for s in ot:
        if s ==' ':
            original_text+=' '
        elif not s.isalpha():
            original_text+=s
        else:
            original_index = alphabet.index(s)
            if encode_or_decode == 'encode':
                shift_to_index = original_index + shift_amount
                original_text+=alphabet[shift_to_index%len(alphabet)]
            elif encode_or_decode == 'decode':
                shift_to_index = original_index - shift_amount
                original_text+=alphabet[shift_to_index%len(alphabet)]
            else:
                print('Please enter either "encode" or "decode". ')
    
    print(original_text)

print(art.logo)
direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n').lower()
text = input('Type your message: \n').lower()

shift = int(input('Type the shift number: \n'))

caesar(text,shift_amount=shift,encode_or_decode=direction)

keep_encrypting = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
while keep_encrypting == 'yes':
    
    direction = input('Type "encode" to encryp, type "decode" to decrypt: \n').lower()
    text = input('Type your message: \n').lower()

    shift = int(input('Type the shift number: \n'))

    caesar(text,shift_amount=shift,encode_or_decode=direction)
    keep_encrypting = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
if keep_encrypting == 'no':
    print('Bye!')

else:
    print('Entered something else, other than: {yes or no} ')
    









