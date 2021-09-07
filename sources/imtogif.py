from PIL import Image
import imageio
import glob
import os

os.system("echo *.eps | xargs -n1 pstopdf")
os.system("sips -s format png *.pdf --out .")

for i in range(4):
	for j in range(10):
		temp = Image.open('{i}-{j}.png'.format(i=i, j=j)).convert("RGBA")
		image = Image.new("RGBA", temp.size, "WHITE")
		x, y = image.size
		image.paste(temp, (0, 0, x, y), temp)
		image.convert('RGB').save('{i}-{j}.png'.format(i=i, j=j), 'PNG')

u = []

for k in range(4):
	for l in range(5):
		u.append(imageio.imread('{i}-{j}.png'.format(i=k, j=l)))
	imageio.mimsave("%d.gif" % k, u, duration=1)
	u = []
	for l in range(5, 10):
		u.append(imageio.imread('{i}-{j}.png'.format(i=k, j=l)))
	imageio.mimsave("%d-j.gif" % k, u, duration=1)
	u = []

os.system("mkdir IMAGES")
os.system("mv *.pdf *.png *.eps IMAGES")

print("Job complete.")