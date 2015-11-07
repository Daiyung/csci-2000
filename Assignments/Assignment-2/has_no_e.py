#Name: Dai Vincent Chan
#Student ID: 100 554 446
def has_no_e(input_string):
    if 'e' in input_string:
        #print('There is ''e'' ')
        return False
    else:
        #print('There is no e in the string')
        return True

reader = open('test.txt', 'r')
contents = reader.readlines()
for line in contents:
    in_string = reader.readline()
    has_no_e(in_string)
reader.close()
