from PIL import Image
import glob

imageFile = glob.glob("*.jpg")
maskImageFile = glob.glob("*.bmp")

imageFile.sort()
maskImageFile.sort()
skinCount=0
nonSkinCount=0
skin=[[[0]*256]*256]*256
nonSkin=[[[0]*256]*256]*256
skinProbability=[[[0]*256]*256]*256
nonSkinProbability=[[[0]*256]*256]*256
probability=[[[0]*256]*256]*256

for iterator in range(len(imageFile)-1):

    im = Image.open(imageFile[iterator]) # Can be many different formats.
    maskIm  = Image.open(maskImageFile[iterator]) # Can be many different formats.

    imageLoader = im.load()
    maskImageLoader = maskIm.load()
    height = maskIm.size[0] # Get the width and hight of the image for iterating over
    width = maskIm.size[1]  # Get the width and hight of the image for iterating over
    
    #calculate skinCount and nonSkin count for each pixel
    for i in range(height):
        for j in range(width): 
            if(maskImageLoader[i,j][0]<255 or maskImageLoader[i,j][1]<255 or maskImageLoader[i,j][2]<255):
                skin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
                skinCount+=1
            else:
                nonSkin[imageLoader[i,j][0]][imageLoader[i,j][1]][imageLoader[i,j][2]]+=1
                nonSkinCount+=1              

    print("Image: ",iterator,"Skin Count: ",skinCount, "Non Skin Count: ", nonSkinCount)
    pointer=0

f=open("traindatafile.txt","w")
for i in range (0, 256):
    for j in range (0, 256):
        for k in range (0, 256):
            skinProbability[i][j][k] = skin[i][j][k]/skinCount
            nonSkinProbability[i][j][k] = nonSkin[i][j][k]/nonSkinCount
            if nonSkinProbability[i][j][k] == 0 and skinProbability[i][j][k] == 0:
                probability[i][j][k]=0
            elif nonSkinProbability[i][j][k] == 0:
                probability[i][j][k]=100
            else:
                probability[i][j][k] = skinProbability[i][j][k]/nonSkinProbability[i][j][k]
                    
            f.write(str(probability[i][j][k])+"\n")
f.close()
                    
                    
            

                    
    