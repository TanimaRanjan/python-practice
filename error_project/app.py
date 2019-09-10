class MyCustomError(TypeError):
    def __init__(self,message,code):
        super().__init__(f' Error Code {code} : {message}')
        self.code = code


raise MyCustomError('An Error happened !!!', 500)