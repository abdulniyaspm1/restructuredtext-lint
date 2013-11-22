import docutils
from docutils.parsers.rst import Parser

def run(content, filepath=None, **kwargs):
    # Generate a new parser
    parser = Parser()
    settings = docutils.frontend.OptionParser(
                    components=(docutils.parsers.rst.Parser,)
                    ).get_default_values()
    document = docutils.utils.new_document(filepath, settings=settings)

    # Disable stdout
    document.reporter.stream = None

    # Collect errors via an observer
    errors = []
    def error_collector(data):
        errors.append(data)
    document.reporter.attach_observer(error_collector)

    # Parse the content and return our collected errors
    parser.parse(content, document)
    return errors
