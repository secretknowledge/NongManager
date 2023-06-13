class Configuration:
    """
    Stores, loads, and handles configuration and settings
    for NongManager application
    """
    def __init__(self, load_file):
        pass

    def save(self, out_file):
        pass


class FileManager:
    """
    Manages creating, deleting, and modifying files within
    the NongManager application
    """
    def __init__(self, configuration):
        self.configuration = configuration  # ConfigurationClass


class Setup:
    """
    Handles creating necessary files when NongManager is run
    for the first time
    """
