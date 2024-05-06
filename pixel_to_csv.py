from PIL import Image
import csv

def get_average_rgb(image):
    width, height = image.size
    rgb_data = image.convert("RGB").load()
    average_rgb_values = []

    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = rgb_data[x, y]
            average = (r + g + b) // 3  # Calculating the average of RGB values
            row.append(average)
        average_rgb_values.append(row)

    return average_rgb_values

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def main(image_path, csv_path):
    image = Image.open(image_path)
    average_rgb_values = get_average_rgb(image)
    write_to_csv(average_rgb_values, csv_path)
    print("CSV file has been created with average RGB values.")

if __name__ == "__main__":
    image_path = "./output-part2/warped_image.jpg"  # Specify the path to your input image
    csv_path = "output.csv"         # Specify the path to your output CSV file
    main(image_path, csv_path)