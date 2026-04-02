import sys
args = sys.argv
if len(args) == 1:
    print('Please input filename')
else:
    filename = args[1]
    with open(filename) as f:
        print(f.read())

# print(sys.argv) # На выходе список из одного элемента, который содержит название нашего файла(с адресом)
# args = sys.argv
# filename = args[1]
# with open(filename) as f:
#     print(f.read())