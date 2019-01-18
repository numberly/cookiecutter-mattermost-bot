from jinja2.ext import Extension


def title_to_directory(title):
    words = title.split(" ")
    return "-".join(word.lower() for word in words)


def file_to_class(filename):
    name = filename.replace(".py", "")
    words = name.split("_")
    return "".join(word.capitalize() for word in words)


class HelpersExtension(Extension):

    def __init__(self, environment):
        super(Extension, self).__init__()
        environment.filters["title_to_directory"] = title_to_directory
        environment.filters["file_to_class"] = file_to_class


__all__ = ["HelpersExtension"]
