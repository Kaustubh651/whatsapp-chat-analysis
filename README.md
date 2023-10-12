## WhatsApp Chat Analyzer

### Project Overview

The WhatsApp Chat Analyzer is a Python application built with Streamlit that allows users to analyze and visualize their WhatsApp chat data. Users can upload their chat data, and the application provides insights into the chat, such as statistics, timelines, activity maps, word clouds, and more. This README file provides a detailed overview of the project structure, requirements, and functionalities.

### Project Structure

The project consists of three main files:

1. `app.py`: This is the main Streamlit application script. It contains the user interface and the logic for uploading chat data, selecting analysis parameters, and displaying various visualizations and statistics.

2. `helper.py`: This module contains the core functions and utilities used by the main application. It includes functions for data preprocessing, calculating statistics, generating word clouds, and creating visualizations like bar charts and heatmaps.

3. `preprocessor.py`: This module handles the preprocessing of the WhatsApp chat data. It extracts messages, dates, and user information from the raw chat data and converts it into a structured DataFrame.

### Requirements

To run this project, you'll need the following:

- Python 3.7 or higher
- Streamlit (for the web interface)
- Pandas (for data manipulation)
- Matplotlib (for plotting)
- Seaborn (for generating heatmaps)
- WordCloud (for creating word clouds)
- Emoji (for emoji analysis)
- urlextract (for extracting URLs from messages)

### How to Use

1. **Clone the Repository:**
   Clone the project repository to your local machine using `git clone`.

2. **Install Dependencies:**
   Install the necessary Python dependencies using the following command:
   ```
   pip install streamlit pandas matplotlib seaborn wordcloud emoji urlextract
   ```

3. **Prepare WhatsApp Chat Data:**
   Export your WhatsApp chat data as a text file (with .txt extension). This chat data should be exported from WhatsApp, including the messages, timestamps, and user names. Ensure that the chat data is in the standard WhatsApp export format.

4. **Run the Application:**
   Run the Streamlit application using the following command:
   ```
   streamlit run app.py
   ```

5. **Upload Chat Data:**
   In the Streamlit web application, upload your WhatsApp chat data file using the file uploader.

6. **Analyze and Visualize:**
   - Choose the user or "Overall" for an analysis.
   - Click the "Show Analysis" button to generate statistics and visualizations for the selected user.
   - Explore features like message statistics, timelines, activity maps, word clouds, and common words.

### Functionalities

- **Message statistics:** Provides the total number of messages, words, media messages, and links shared for the selected user.
- **Monthly and daily timelines:** Displays line charts showing message trends over time.
- **Activity maps:** Shows the busiest day, monthly activity, and a heatmap of weekly activity.
- **Most active user:** If "Overall" is selected, it identifies the most active user in the chat.
- **Word cloud:** Generates a word cloud for the selected user's messages.
- **Most common words:** Displays a bar chart of the most common words used in messages.
- **Emoji analysis (currently commented out):** Provides an analysis of emojis used in the chat.

### Contributions

Contributions to this project are welcome. You can enhance and extend the functionality, improve the UI, and fix any issues. Please make sure to create a pull request with a detailed description of your changes.

### License

This project is available under the MIT License.

### Disclaimer

This project is not affiliated with WhatsApp and is intended for personal use and analysis of chat data. Please respect privacy and data sharing policies when using the application.

---
