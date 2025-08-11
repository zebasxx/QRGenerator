import os
import sys
import qrcode


def read_text_from_file(file_path: str) -> str:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def main() -> None:
    input_file_path = os.environ.get("INPUT_FILE", "input.txt")
    output_dir = os.environ.get("OUTPUT_DIR", "output")
    output_file_name = os.environ.get("OUTPUT_FILE", "my_qr.png")

    os.makedirs(output_dir, exist_ok=True)

    try:
        text_to_encode = read_text_from_file(input_file_path)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    qr_image = qrcode.make(text_to_encode)
    output_path = os.path.join(output_dir, output_file_name)
    qr_image.save(output_path)
    print(f"QR code generated successfully at {output_path}")


if __name__ == "__main__":
    main()