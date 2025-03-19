import csv

def read_coordinates(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Başlık satırını atla
        for row in reader:
            x, y = map(int, row)
            print(f"X: {x}, Y: {y}")

if __name__ == "__main__":
    read_coordinates("coordinates.csv")
    