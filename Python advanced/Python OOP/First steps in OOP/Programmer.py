class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, lang, skills):
        if lang == self.language:
            self.skills += skills
            return f'{self.name} watched {course_name}'
        return f"{self.name} does not know {lang}"

    def change_language(self, new_lang, skills_needed):
        if self.skills >= skills_needed and new_lang != self.language:
            previous = self.language
            self.language = new_lang
            return f"{self.name} switched from {previous} to {new_lang}"
        if self.skills >= skills_needed and new_lang == self.language:
            return f"{self.name} already knows {self.language}"
        return f"{self.name} needs {skills_needed - self.skills} more skills"
