# pip install rembg
from rembg import remove
from PIL import Image

input_path = r'C:\Users\reza\Desktop\MyFile\tim-berners-lee-on-the-next-generation-internet.png'
output_path = r'C:\Users\reza\Desktop\MyFile\nom.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
print('done')