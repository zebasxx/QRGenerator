# QR Generator

A simple Python application that generates QR codes from text files using Docker.

## Features

- Generate QR codes from text files
- Configurable input and output paths via environment variables
- Docker containerization for easy deployment
- Volume mapping for persistent output storage

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd QRGenerator
   ```

2. **Create the input folder and add your text file**
   ```bash
   mkdir -p input
   ```

3. **Create `input/input.txt` with your desired text content**
   ```bash
   # Example content for input/input.txt
   cat > input/input.txt << 'EOF'
   Nro Registro SENASA: 37784
   Envase: Botella 1 litro
   Marca: Coadyuvante Rocio
   Empresa: Tres Rocios SRL
   Clase Toxicológica: IV
   Fecha elaboración: 1/8/25
   Fecha vencimiento: 1/8/27
   Nro lote: 469
   EOF
   ```

4. **Create the output directory**
   ```bash
   mkdir -p output
   ```

## Usage

### Using Docker Compose (Recommended)

1. **Build and run the application**
   ```bash
   docker-compose up --build
   ```

2. **Run in detached mode**
   ```bash
   docker-compose up --build -d
   ```

3. **Stop the application**
   ```bash
   docker-compose down
   ```

### Using Docker directly

1. **Build the Docker image**
   ```bash
   docker build -t qr-generator .
   ```

2. **Run the container**
   ```bash
   docker run -v $(pwd)/output:/app/output qr-generator
   ```

## Configuration

The application supports the following environment variables:

- `INPUT_FILE`: Path to the input text file (default: `input.txt`)
- `OUTPUT_DIR`: Directory to save the generated QR code (default: `output`)
- `OUTPUT_FILE`: Name of the output QR code file (default: `my_qr.png`)

### Customizing via Docker Compose

You can override these settings in your `docker-compose.yml`:

```yaml
version: '3.8'

services:
  qr-generator:
    build: .
    volumes:
      - ./output:/app/output
    environment:
      - PYTHONUNBUFFERED=1
      - INPUT_FILE=/app/input/input.txt
      - OUTPUT_FILE=custom_qr.png
      - OUTPUT_DIR=/app/output
```

## File Structure

```
QRGenerator/
├── app.py              # Main application code
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker image configuration
├── docker-compose.yml # Docker Compose configuration
├── README.md          # This file
├── input/             # Input text files directory
│   └── input.txt      # Your text content (create this)
└── output/            # Generated QR codes (created automatically)
    └── my_qr.png      # Generated QR code image
```

## How It Works

1. The application reads text content from the specified input file
2. Generates a QR code containing that text
3. Saves the QR code image to the output directory
4. The output directory is mapped to your local filesystem via Docker volumes

## Troubleshooting

- **Input file not found**: Ensure you've created the `input/input.txt` file
- **Permission errors**: Make sure the `output` directory has write permissions
- **Docker build fails**: Verify Docker and Docker Compose are properly installed

## License

[Add your license information here] 