def create_writer(file):
    def writer(value):
        with open(file, 'a') as f:
            f.write(str(value) + '\n')
    return writer


write_to_file = create_writer('output.txt')
write_to_file(1)
write_to_file("nothing's wrong with me")
write_to_file(2)
write_to_file("nothing's wrong with me")

f = open('output.txt','r')
print(f.read())