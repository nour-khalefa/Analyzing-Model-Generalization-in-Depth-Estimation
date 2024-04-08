import os

# Define the base directory
base_dir = "/home/nour.khalefa/datasets/DrivingStereo"

# Define the folder names
folders = ["foggy/foggy", "cloudy/cloudy", "sunny/sunny", "rainy/rainy"]

# Iterate over the folders
for folder in folders:
    left_image_dir = os.path.join(base_dir, folder, "left-image-half-size")
    depth_map_dir = os.path.join(base_dir, folder, "depth-map-half-size")
    
    # Get the list of image files in the left image directory
    left_image_files = os.listdir(left_image_dir)
    
    # Create the output file name
    output_file = os.path.join(base_dir, f"filenames_eval_{folder.replace('/', '_')}.txt")
    
    # Open the output file in write mode
    with open(output_file, "w") as file:
        # Iterate over the left image files
        for left_image_file in left_image_files:
            # Get the corresponding depth map file name
            depth_map_file = left_image_file.replace(".jpg", ".png")
            
            # Write the line to the output file
            file.write(f"{left_image_file} {depth_map_file} 2.061940e+03\n")