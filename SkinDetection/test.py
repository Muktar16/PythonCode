from PIL import Image

probability=[[[0]*256]*256]*256

f = open("traindatafile.txt", "r")

for i in range (256):
    for j in range (256):
        for k in range (256):            
            probability[i][j][k] = float(f.readline())
f.close()

# data to 3*3 matrix
# i=0
# j=0
# k=0

# for data in f:
#     if(k==256):
#         j=j+1
#         if(j==256):
#             i=i+1
#     probability[i%256][j%256][k%256]=float(data)
#     k=k+1

testingImage = Image.open('0446.jpg')
testImLoader = testingImage.load()
output_Image = testingImage.load()


for i in range (0, testingImage.size[0]):
    for j in range (0,testingImage.size[1]):
        if probability[testImLoader[i,j][0]][testImLoader[i,j][1]][testImLoader[i,j][2]] >= 1.0:
            output_Image[i,j] = testImLoader[i,j]
            #output_Image[i,j] = (255,255,255)
        else:
            output_Image[i,j] = (255,255,255)
#testingImage.save("outputImage.bmp")
testingImage.show()
