import os
import subprocess
import glob
import os.path

file_copy = []
os.makedirs('Result')
os.makedirs('Copy_Source')
os.chdir('Source/')
subprocess.run('cp *.jpg ../Copy_Source', shell = True)
os.chdir('../')
files = glob.glob(os.path.join('Copy_Source/', "*.jpg"))
for file in files:
	print('Source   ', file)
file_copy = files
print(file_copy)
for image in file_copy:
	subprocess.call('sips --resampleWidth 200 %s' % image, shell = True)
os.chdir('Copy_Source/')
subprocess.run('cp *.jpg ../Result', shell = True)
os.chdir('../Result')
subprocess.run('pwd')
subprocess.run('ls')