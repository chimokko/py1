def create_writer(file):
    f = open(file, 'a')
    def writer(value):
        f.write(str(value) + '\n')
        f.flush()
    return writer


write_to_file = create_writer('output.txt')
write_to_file(1)
write_to_file("nothing's wrong with me")
write_to_file(2)
write_to_file("nothing's wrong with me")

f = open('output.txt','r')
print(f.read())