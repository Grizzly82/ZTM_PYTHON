#Using the Pillow library to open and manipulate images


from PIL import Image
import os

def process_and_save_image(input_path, output_folder, output_filename):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Open the image
        img = Image.open(input_path)

        # Example processing: resize and convert to grayscale
        img_resized = img.resize((300, 300))  # Resize to 300x300
        img_gray = img_resized.convert("L")   # Convert to grayscale

        # Build full output path
        output_path = os.path.join(output_folder, output_filename)

        # Save the processed image
        img_gray.save(output_path)

        print(f"Image processed and saved to: {output_path}")

    except FileNotFoundError:
        print("Error: The input image file was not found.")
    except OSError as e:
        print(f"Error processing image: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = "Exercise_21/dc_images/Pop! Batman with Bomb.png"  # Path to your input image
    save_folder = "Exercise_21/dc_images/new_dc_images"  # Folder where you want to save
    save_filename = "output_dc_image.png"  # Output file name

    process_and_save_image(input_image_path, save_folder, save_filename)
