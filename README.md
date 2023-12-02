# Fake News Prediction

## Overview
This project aims to predict the authenticity of news articles using machine learning techniques. It involves text preprocessing, including lowercase conversion and lemmatization, followed by classification into "FAKE" or "REAL" categories.

## Structure

### 1. `MainScript.py`
This script serves as the entry point of the project. It orchestrates the data processing steps by instantiating objects from other modules and executing the necessary operations.

### 2. `FileManager.py`
Responsible for handling file-related operations, specifically reading the dataset from a CSV file.

### 3. `TextProcessor.py`
Contains methods for text preprocessing using the spaCy library. It performs tasks such as lowercase conversion and lemmatization of text data.

### 4. `DataProcessor.py`
Manages the processing of data features. This class includes methods for label binarization and dropping unnecessary columns from the dataset.

## Usage

1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Update the `file_path` variable in `MainScript.py` to point to your dataset file.
4. Run `MainScript.py` to initiate the data processing pipeline.

## Dependencies
- pandas
- scikit-learn
- spacy

## How to Use
1. Replace the dataset file path in `MainScript.py` with the path to your dataset.
2. Execute `MainScript.py`.
3. The processed dataset with added columns for lowercase text and lemmatized text will be available for further analysis or modeling.

## Notes
- This code assumes the dataset is in CSV format and follows a specific structure (columns: 'Unnamed: 0', 'label', 'title', 'text').
- Additional preprocessing steps or model implementations can be added within the modular structure provided.

## Credits
- This code is based on machine learning techniques taught in various data science courses and adapted for the purpose of fake news prediction, hence the dataset finds on Kaggle at https://www.kaggle.com/datasets/rajatkumar30/fake-news.
