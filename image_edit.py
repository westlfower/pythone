from PIL import Image

#이미지 경로 저장
image_path="characters.jpg"

#이미지 열어 객체를 저장
image=Image.open(image_path)
image=image.crop((410,300,5590,2700))
width,height=image.size

# (2행 5열 이미지)
frame_width=width//5
frame_height=height//2

#이미지 분할

frames=[]
for row in range(2):
    for col in range(5):
        left= col*frame_width
        upper=row*frame_height
        right=left+frame_width
        lower=upper+frame_height
        frame=image.crop((left,upper,right,lower))
        frames.append(frame)

for i, frame in enumerate(frames):
    frame.save(f'frame_{i+1}.png')
    
print(f'{len(frames)}개의 프레임이 저장되었습니다.')
