# RNN Movie Review Analysis

## Overview
The "RNN Movie Review Analysis" app leverages a Recurrent Neural Network (RNN) to analyze movie reviews and predict their sentiment. The app provides a user-friendly interface where users can input their movie reviews and receive an analysis of the sentiment along with a star rating.

## Features
- **Sentiment Analysis**: Predicts whether the review is positive or negative.
- **Star Rating**: Provides a star rating based on the sentiment score.
- **Marvel Avatars**: Displays a random Marvel character avatar for a fun user experience.
- **Interactive UI**: Built with Streamlit for a responsive and interactive user interface.

## Installation

### Prerequisites
- Python 3.12.8
- Virtual environment (recommended)

### Steps
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/RNN_Movie_Review_Analysis.git
    cd RNN_Movie_Review_Analysis
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```sh
    streamlit run app.py
    ```

## Usage
1. Open the app in your browser (usually at `http://localhost:8501`).
2. Enter your name and movie review in the provided fields.
3. Click on "Generate Analysis" to see the sentiment analysis and star rating.

## Files
- `app.py`: Main application file for Streamlit.
- `simplernn.ipynb`: Jupyter notebook for training the RNN model.
- `embedding.ipynb`: Jupyter notebook for embedding representation.
- `requirements.txt`: List of required Python packages.
- `simple_rnn_imdb.h5`: Pre-trained RNN model file.

## Model Training
The RNN model is trained on the IMDB dataset using TensorFlow and Keras. The training process is documented in the `simplernn.ipynb` notebook.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [IMDB Dataset](https://www.imdb.com/interfaces/)

## Contact
For any questions or feedback, please contact [Ankit Pokhrel](mailto:pokhrelankit2004@example.com).
