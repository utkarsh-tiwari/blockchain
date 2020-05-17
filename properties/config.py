import os

process_folder_name = 'blockchain'
properties_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)))
processing_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), process_folder_name, 'processing')
log_config = os.path.join(properties_folder, 'logging_config.yml')
