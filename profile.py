"""Create Dating Profile"""

class Profile:
    """Dating Profile generator

    To create a dating profile, pass in a list of prompts
    and the text of the template

    Whatever is filled in is generated in
    dating profile card

    """

    def __init__(self, words):
        """create a profile with the words and template text format"""

        self.prompts = words
        

    def generate(self, answers):
        """substitute answers into html profile page template"""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


myProfile = Profile(["name", "age", "location", "bio"])