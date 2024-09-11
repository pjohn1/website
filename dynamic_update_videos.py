import os

with open('jupiter.html','r') as f:
    lines = f.readlines()
f.close()

video_str = ""
for i in os.listdir('videos'):
    video_str += "\'videos/"+i+"\',"
video_str = video_str[:-1] #remove last comma
# print(video_str)

entered = False
for l in range(len(lines)):
    split = lines[l].split()
    if len(split) > 1 and split[1] == 'videoFiles':
        entered = True
        lines[l] = f'const videoFiles = [{video_str}];\n'
        print(l)
        break
if not entered:
    print('did not find line')
    raise


final_str = "\t\t"
for line in lines:
    final_str += line

jupiter = open('jupiter.html','w')
jupiter.write(final_str)
jupiter.flush()
jupiter.close()
print('Finished!')
