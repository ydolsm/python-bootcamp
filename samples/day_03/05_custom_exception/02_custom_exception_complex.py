class CustomError(Exception):

    count = 0

    def __init__(self, message, id):
        CustomError.count += 1

        custom_message = f"Custom Error {CustomError.count} with ID {id}"
        super().__init__(custom_message)

raise CustomError("yikes", 'a')