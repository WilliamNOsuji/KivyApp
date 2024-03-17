# main_screen.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from api.words_api import fetch_word_details


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create text input field
        self.text_input = TextInput(font_size=16, size_hint=(1, 0.9))
        self.text_input.bind(on_selection=self.on_selection_changed)  # Bind on_selection event
        self.add_widget(self.text_input)

        # Add a button for saving the text
        self.save_button = Button(text='Save', size_hint=(1, 0.1))
        self.save_button.bind(on_press=self.save_text)
        self.add_widget(self.save_button)

    def on_selection_changed(self, instance, selection):
        if selection:
            selected_word = self.text_input.selection_text.strip()
            if selected_word:
                self.fetch_and_show_word_details(selected_word)

    def fetch_and_show_word_details(self, word):
        properties = ['definitions', 'synonyms', 'antonyms', 'examples', 'rhymes']
        word_details = {property: fetch_word_details(word, property) for property in properties}
        self.show_options_popup(word, word_details)

    def show_options_popup(self, word, word_details):
        popup_content = BoxLayout(orientation='vertical')
        popup = Popup(title="Options for '{}'".format(word), content=popup_content, size_hint=(None, None),
                      size=(400, 300))

        # Add options buttons
        for option, details in word_details.items():
            button = Button(text=option.capitalize() + ': ' + ', '.join(details), size_hint_y=None, height=40)
            popup_content.add_widget(button)

        popup.open()

    def save_text(self, instance):
        text_content = self.text_input.text
        # Implement logic to save the text content


class TextEditorApp(App):
    def build(self):
        return MainScreen()


if __name__ == '__main__':
    TextEditorApp().run()