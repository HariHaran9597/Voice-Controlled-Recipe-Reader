# Voice-Controlled Recipe Reader

A hands-free recipe reading application that allows you to navigate through recipe steps using voice commands while cooking. Perfect for when your hands are messy or occupied with cooking tasks!

## Features

- **Voice-Controlled Navigation**: Navigate through recipe steps using simple voice commands:
  - "Next" - Move to the next recipe step
  - "Repeat" - Repeat the current step
  - "Stop" - End the recipe reading session

- **Text-to-Speech**: Clear audio readout of recipe steps using pyttsx3 engine

- **Smart Speech Recognition**: 
  - Automatic microphone calibration for optimal voice recognition
  - Dynamic energy threshold adjustment
  - Ambient noise reduction
  - Timeout and phrase time limits for better command capture

- **Recipe File Support**: Load recipes from simple text files

## Dependencies

The project requires the following Python packages:

- SpeechRecognition - For voice command recognition
- gTTS - Google Text-to-Speech engine
- pyttsx3 - Text-to-speech conversion
- playsound - Audio playback
- streamlit - Web interface (for future development)
- langchain - AI framework for smart command interpretation (optional)

## Setup

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have a working microphone connected to your system

## Usage

1. Create a recipe file (e.g., sample_recipe.txt) with steps on separate lines
2. Run the recipe reader:
   ```
   python recipe_reader.py
   ```
3. The program will:
   - Calibrate your microphone
   - Load the recipe
   - Read the first step
   - Wait for your voice commands

## Sample Recipe

The project includes a sample cookie recipe that demonstrates the format:

```
Preheat the oven to 350 degrees Fahrenheit.
In a large bowl, mix 2 cups of flour with 1 teaspoon of salt and 1 teaspoon of baking powder.
In a separate bowl, cream together 1 cup of butter and 1 cup of sugar until light and fluffy.
Add 2 eggs one at a time, mixing well after each addition.
Gradually stir the dry ingredients into the wet mixture.
Drop rounded tablespoons of dough onto ungreased baking sheets.
Bake for 12-15 minutes or until edges are lightly golden.
Let cool on baking sheets for 5 minutes before transferring to wire racks.
```

## Technical Details

- **Microphone Calibration**: The system performs initial calibration and continuous adjustment for ambient noise
- **Command Recognition**: Uses Google's Speech Recognition service for accurate voice command interpretation
- **Error Handling**: Robust error handling for various scenarios:
  - No command heard
  - Unclear audio
  - Connection issues
  - File not found errors

## Future Enhancements

- Web interface using Streamlit
- Smart command interpretation using AI
- Support for multiple recipe formats
- Timer functionality for cooking steps
- Ingredient list management

## Note

Ensure you have a stable internet connection as the speech recognition service requires internet connectivity.