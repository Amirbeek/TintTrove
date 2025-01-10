# TintTrove

TintTrove is a simple and elegant image color picker tool that extracts dominant colors from uploaded images. Designed to help designers, artists, and developers explore color palettes with ease. The project is powered by a KMeans clustering algorithm and deployed on Heroku.

## Features
- Extracts dominant colors from any uploaded image.
- Provides HEX and RGB values of colors.
- Responsive and user-friendly design.
- Built for seamless performance with minimal load times.

## Algorithm Details
The core functionality relies on the following algorithm:

### Color Clustering Algorithm
```python
def get_colors(image, number_of_colors, show_chart=False):
    if image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    elif image.shape[2] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    reshaped_image = cv2.resize(image, (600, 400))
    reshaped_image = reshaped_image.reshape(reshaped_image.shape[0] * reshaped_image.shape[1], 3)
    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(reshaped_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB_HEX(ordered_colors[i]) for i in counts.keys()]
    return hex_colors
```

### Key Concepts:
- **KMeans Clustering**: Groups pixels in the image into `number_of_colors` clusters.
- **OpenCV**: Used for image preprocessing (e.g., resizing, color conversion).
- **HEX Conversion**: Converts RGB values to HEX codes for easy usage in design tools.

## Deployment
TintTrove is deployed on **Heroku**, making it accessible anywhere.

### Live Demo
[Check out TintTrove live on Heroku](#)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tinttrove.git
   ```

2. Navigate to the project directory:
   ```bash
   cd tinttrove
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:
   ```bash
   python app.py
   ```

5. Open the application in your browser at `http://localhost:5000`.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Algorithm**: KMeans clustering for color extraction
- **Image Processing**: OpenCV
- **Deployment**: Heroku

## Potential Additions
To increase user engagement, consider adding:
- **Save Palettes**: Allow users to save extracted palettes.
- **Palette Suggestions**: Suggest complementary or analogous palettes based on extracted colors.
- **Download Options**: Export palettes as JSON, CSS, or images.
- **User Accounts**: Enable users to store their palettes online.
- **Integration with Design Tools**: Provide links to Adobe or Canva for direct palette import.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, reach out to:
- Email: support@tinttrove.com
- GitHub Issues: [Create an Issue](https://github.com/your-username/tinttrove/issues)
