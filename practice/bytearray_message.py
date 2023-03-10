'''
Computers store all data as bytes, not text. To interpret bytes as text (characters), we rely on arbitrary mappings. For example, in ASCII (a popular but old mapping) the byte 01000001 means 'A'. One problem with ASCII is that it only support English characters (and a few other European languages). To solve this problem, Unicode was created. Unicode is like ASCII, but larger. It supports 1,114,112 different symbols (more than enough for all human languages, plus some fun stuff like Emoji 😱). However, because Unicode is so much larger than ASCII, it takes more than 1 byte to encode each character. To make common text smaller, UTF-8 was created. It is a way to encode Unicode characters, that uses a variable-width encoding scheme so that common English characters take less memory. When the above byte array is decoded with the UTF-8 encoding, we get three Unicode code points, u'\u0643\u0644\u0628', which is rendered as كلب.
'''

b = bytearray([0xd9, 0x83, 0xd9, 0x84, 0xd8, 0xa8])
message = b.decode('utf-8')

# Answer: It takes a sequence of bytes and interprets them as UTF-8 encoded Unicode to produce a string of characters
