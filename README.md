# The Gourmet AI - Recipe Generation System


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Ingredient Detection**: Uses YOLOv8 to identify 12 common fruits from images
- **Recipe Generation**: Generates recipes based on detected fruits using Mistral-7B
- **User-Friendly Interface**: Simple Streamlit web interface
- **Specialized Accuracy**: 92% detection accuracy for trained fruits
- **Quick Processing**: Average response time of 4.2 seconds

## Installation

1. Clone the repository:
   ```bash
   git c lone https://github.com/yourusername/gourmet-ai.git
   cd gourmet-ai
   ```
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Run the Streamlit application:
  ```bash
  streamlit run app.py
  ```
4. Upload an image containing fruits through the web interface

5. View detected fruits and generated recipes\

## Project Structure

**gourmet-ai/
├── models/               # Pretrained model weights
├── data/                 # Sample test images
├── src/
│   ├── detection.py      # Fruit detection module
│   ├── generation.py     # Recipe generation module
│   └── utils.py          # Helper functions
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md             # This file**

## Roadmap
1. Basic fruit detection (12 categories)

2. Recipe generation integration

3. Expand to 50+ ingredients

4. Add dietary preference filters

5. Implement portion size estimation

## Contributing
1. We welcome contributions! Please follow these steps:
2. Fork the project
3. Create your feature branch (git checkout -b feature/AmazingFeature)
4. Commit your changes (git commit -m 'Add some AmazingFeature')
5. Push to the branch (git push origin feature/AmazingFeature)
6. Open a Pull Request
## Acknowledgements
1. YOLOv8 by Ultralytics
2. Mistral-7B by Mistral AI
3. Streamlit for the web interface
4. All contributors and testers
   
