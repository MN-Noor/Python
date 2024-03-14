# numbers=[5,2,5,2,2]
# for item in numbers:
#     output=" "
#     for number in range(item):
#        output+='*'
#     print(output)
# names=['aymen', 'mosh' ,'sara' ,'eman' ,'faiza' ,'maryam']
# for item in names:
#     for char in item:
#         print(char)
# list=[2,5,7,9,5,4,3,8]
# largest=1
# for item in list:
#     if item>largest:
#         largest=item
# print(largest) 

def emoji_creator(message):
    words=message.split(" ")
    output=" "
    emoji={
    ":(":"😣",
    ":)":"😃",
    }
    for word in words:
        output+=emoji.get(word,word)+" "
    return output

message=input(">>")   
print(emoji_creator(message))


# phone= input(">>")
# output=" "
# phonebook={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
# }
# for char in phone:
#     output+=phonebook.get(char,'!')+" "
# print(output)
