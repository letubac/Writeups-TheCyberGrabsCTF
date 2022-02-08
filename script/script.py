# uncompyle6 version 3.5.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.8 (default, Nov 16 2020, 16:55:22) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: script.py
# Compiled at: 2022-01-28 17:05:32
# encoded_flag = '*@),9.9():B@tz&k6<5i&\\mX&xmn-y&*Vu/,wD'
# alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

# def encode_secret(secret):
#     rotate_const = 37
#     encoded = ''
#     for c in secret:
#         index = alphabet.find(c)
#         original_index = (index + rotate_const) % len(alphabet)
#         encoded = encoded + alphabet[original_index]

#     return encoded


# text = raw_input('Enter any text to encrypt: ')
# if encoded_flag == encode_secret(text):
#     print 'Congratulations!!!. You found the flag.'
# else:
#     print 'Sorry!!!'

#-----------------------------------------------------------------------------------

encoded_flag = '*@),9.9():B@tz&k6<5i&\\mX&xmn-y&*Vu/,wD'
alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def encode_secret(secret):
    rotate_const = 37
    encoded = ''
    for c in secret:
        index = alphabet.find(c)
        original_index = (index - rotate_const) % len(alphabet)
        encoded = encoded + alphabet[original_index]

    return encoded
print(encode_secret(encoded_flag))