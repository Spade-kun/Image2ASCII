from PIL import Image, ImageEnhance

def image_to_ascii(image_path, save_path, width=100):
    # More detailed ASCII characters from darkest to lightest
    ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    try:
        # Open image and convert to grayscale
        image = Image.open(image_path)
        image = image.convert('L')  # Convert to grayscale

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)  # Increase contrast

        # Calculate new dimensions while maintaining aspect ratio
        aspect_ratio = image.height / image.width
        height = int(width * aspect_ratio * 0.6)  # Adjusted aspect ratio correction factor

        # Resize image
        image = image.resize((width, height))

        # Convert pixels to ASCII
        pixels = image.getdata()
        ascii_str = ''
        for i, pixel in enumerate(pixels):
            # Map pixel value (0-255) to ASCII characters
            ascii_str += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
            if (i + 1) % width == 0:
                ascii_str += '\n'

        # Save ASCII art to file
        with open(save_path, 'w') as f:
            f.write(ascii_str)

        print(f"ASCII art saved to {save_path}")

    except Exception as e:
        print(f"Error processing image: {str(e)}")

def main():
    image_path = input("Enter the path of the image to convert into ASCII: ") # Path of the image
    save_path = input("Enter the path of the file to save the text in: ") # Save as .txt file
    width = int(input("Enter the desired width of the ASCII art (default is 100): ") or 100)

    image_to_ascii(image_path, save_path, width)

if __name__ == "__main__":
    main()

