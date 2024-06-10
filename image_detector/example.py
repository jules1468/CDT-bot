from image_detector.detector import check_image_in_image

# path to images
large_image_path = r'path_to_your_large_image.png'
small_image_path = r'path_to_your_small_image.png'

# verify if referance image is present in data image
result = check_image_in_image(large_image_path, small_image_path)

if result:
    print("La petite image est présente dans la grande image.")
else:
    print("La petite image n'est pas présente dans la grande image.")
