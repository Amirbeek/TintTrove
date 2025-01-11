import imageio.v2 as imageio
from flask import Flask, request, jsonify, render_template
from color_clustering import get_colors

app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/color', methods=['GET', 'POST'])
def color():
    if request.method == 'POST':
        if 'images[]' not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        image_file = request.files['images[]']

        try:
            # Read image using imageio
            image = imageio.imread(image_file)
        except Exception as e:
            app.logger.error(f"Image processing failed: {str(e)}")
            return jsonify({"error": f"Failed to process the image. Error: {str(e)}"}), 400

        try:
            # Get dominant colors
            dominant_colors = get_colors(image, number_of_colors=5, show_chart=False)
            app.logger.info(f"Dominant colors: {dominant_colors}")
            return jsonify({"dominant_colors": dominant_colors})
        except Exception as e:
            app.logger.error(f"Color extraction failed: {str(e)}")
            return jsonify({"error": f"Failed to extract colors. Error: {str(e)}"}), 500

    return render_template('color.html')


if __name__ == '__main__':
    app.run(debug=True)
