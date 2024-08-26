from PIL import Image, ImageEnhance
import os

def sharpen_image(image_path, sharpness_factor=2.0, output_path=None):
    try:
        # Open the image
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return
    
    # Enhance the sharpness
    enhancer = ImageEnhance.Sharpness(image)
    sharpened_image = enhancer.enhance(sharpness_factor)
    
    # Determine the output path if not provided
    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_sharpened{ext}"
    
    # Save the sharpened image
    sharpened_image.save(output_path)
    print(f"Sharpened image saved as: {output_path}")

if __name__ == "__main__":
    # Prompt the user for the image file path
    image_path = input("Enter the path to the image file: ").strip()
    
    # Prompt the user for the sharpness factor (optional)
    while True:
        try:
            sharpness_factor = float(input("Enter the sharpness factor (range 0.0 to 10.0, default is 2.0): ") or 2.0)
            if 0.0 <= sharpness_factor <= 10.0:
                break
            else:
                print("Please enter a value between 0.0 and 10.0.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Call the function to sharpen the image
    sharpen_image(image_path, sharpness_factor)

