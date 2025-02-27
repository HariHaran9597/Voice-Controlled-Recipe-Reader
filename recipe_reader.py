import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import tempfile

class RecipeReader:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.current_step = 0
        self.recipe_steps = []
        self.is_running = True
        self.temp_dir = tempfile.mkdtemp()
        # Adjust microphone energy threshold for better recognition
        with sr.Microphone() as source:
            print("Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Microphone calibrated!")
            # Set dynamic energy threshold
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.energy_threshold = 4000

    def load_recipe(self, file_path):
        """Load recipe steps from a text file."""
        try:
            with open(file_path, 'r') as file:
                self.recipe_steps = [step.strip() for step in file.readlines() if step.strip()]
            return True
        except FileNotFoundError:
            print(f"Could not find recipe file: {file_path}")
            return False

    def speak_text(self, text, is_error=False):
        """Convert text to speech and play it."""
        try:
            import pyttsx3
            engine = pyttsx3.init()
            if is_error:
                engine.say(f"Error: {text}")
            else:
                engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {str(e)}")
            print("Please check if pyttsx3 is properly installed and your audio system is working.")

    def listen_command(self):
        """Listen for voice commands."""
        with sr.Microphone() as source:
            print("Listening for command...")
            try:
                # Add a short pause after text-to-speech
                import time
                time.sleep(0.5)
                
                # Adjust microphone for each listening session
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Increase timeout and phrase_time_limit for better command capture
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")
                return command
            except sr.WaitTimeoutError:
                print("No command heard. Please try again.")
                self.speak_text("I didn't hear anything. Please try again.", is_error=True)
            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
                self.speak_text("I couldn't understand that. Please try again.", is_error=True)
            except sr.RequestError:
                print("Could not request results. Check your internet connection.")
                self.speak_text("I'm having trouble connecting to the speech recognition service. Please check your internet connection.", is_error=True)
            return None

    def process_command(self, command):
        """Process voice commands and take appropriate action."""
        if command is None:
            return

        if "next" in command:
            if self.current_step < len(self.recipe_steps) - 1:
                self.current_step += 1
                self.speak_text(f"Step {self.current_step + 1}: {self.recipe_steps[self.current_step]}")
            else:
                self.speak_text("You have reached the end of the recipe.")

        elif "repeat" in command:
            if self.recipe_steps:
                self.speak_text(f"Repeating step {self.current_step + 1}: {self.recipe_steps[self.current_step]}")

        elif "stop" in command:
            self.is_running = False
            self.speak_text("Stopping recipe reader.")

    def run(self, recipe_file):
        """Main method to run the recipe reader."""
        if not self.load_recipe(recipe_file):
            return

        print("Recipe loaded successfully!")
        self.speak_text("Welcome to Recipe Reader! Starting with the first step.")
        self.speak_text(f"Step 1: {self.recipe_steps[0]}")

        while self.is_running:
            command = self.listen_command()
            self.process_command(command)

if __name__ == "__main__":
    reader = RecipeReader()
    # You can replace this with your recipe file path
    recipe_file = "sample_recipe.txt"
    reader.run(recipe_file)