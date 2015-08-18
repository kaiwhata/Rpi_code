import sys
import matplotlib.image as mpimg

img = mpimg.imread(str(sys.argv[1]))
'''
for i in range(len(img[:,0,0])):
	for j in range(len(img[0,:,0])):
		if (img[i,j,0]+img[i,j,2])==0:
			img[i,j,0] = 0.01
			img[i,j,2] = 0.01
'''
img=img+0.01
mpimg.imsave('output.png',((img[:,:,0]-img[:,:,2])/(img[:,:,0]+img[:,:,2])))
'''

mpimg.imsave('output.png',(img[:,:,0]-img[:,:,2]))
'''