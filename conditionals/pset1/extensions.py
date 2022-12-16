fileType = input("File Name: ")
if '.' in fileType:
    fileTypeExtension = fileType.split('.')[1]
else:
    fileTypeExtension = fileType

match fileTypeExtension:
    case 'gif' | 'jpeg' | 'jpg' | 'png' | 'pdf' | 'txt' | 'zip':
        print(f'image/{fileTypeExtension}')
    case _:
        print('application/octet-stream')