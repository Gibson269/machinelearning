## Read a text file and count the number of lines, words, and characters. 
'''
def count_text_file(file_path):
    with open(file_path,'r') as file:
        lines= file.readlines()
        line_count=len(lines)
        word_count=sum(len(line.split()) for line in lines)
        char_count=sum(len(line) for line in lines)
    return line_count, word_count, char_count

file_path='destination.txt'
lines, words, characters = count_text_file(file_path)
print(f"Lines: {lines}, Words: {words}, Characters:{characters}")

'''

with open ("destination.txt", 'r') as file:
    count=file.read()
    lines=file.readlines()

wordcount=len(count.split())
linescount=len(lines)
Charactercount=len(count.strip())

print (f"Word count is {wordcount}, Character Count is {Charactercount}, Linecount is {linescount} ")

