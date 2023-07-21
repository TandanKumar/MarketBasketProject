import os
import sys


class MARKET_BASKET_PROJECT_Exception(Exception):

    def __init__(self,error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message=MARKET_BASKET_PROJECT_Exception.get_detailed_error_message(error_message=error_message,error_detail=error_detail)

    @staticmethod
    def get_detailed_error_message(error_message : Exception , error_detail:sys)->str:
        """
            error_message :Exception Object
            error_detail : object of sys module
        
        """
        
        _,_,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error has occured in file [{file_name}] at line number [{line_number}] and Error Message :[{error_message}]"
        return error_message    

    def __str__(self):
        return self.error_message
    
    def __repr__(self)->str:
        return MARKET_BASKET_PROJECT_Exception.__name__.str()
