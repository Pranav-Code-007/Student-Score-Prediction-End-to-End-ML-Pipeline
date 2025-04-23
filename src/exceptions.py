import sys

def error_message_details(error, error_details:sys):
    _, _, exc_tb =  error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_back.co_filename
    error_message= f"Error occred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __int__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self):
        self.error_message      
