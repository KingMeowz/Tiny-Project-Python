from PIL import Image


def convert_jpg_to_png(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, "PNG")
        print("Konversi berhasil!")
    except Exception as e:
        print("Terjadi kesalahan:", str(e))


if __name__ == "__main__":
    # Ganti dengan path gambar JPG yang ingin diubah
    input_file = "path/images.jpg"
    # Nama file untuk gambar PNG hasil konversi
    output_file = "path/images.png"

    convert_jpg_to_png(input_file, output_file)
