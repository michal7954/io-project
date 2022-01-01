def getUserOperation(operationString: str, userOperationsList):

    if operationString.isnumeric():
        operationIndex = int(operationString) - 1
        if operationIndex >= 0 and operationIndex < len(userOperationsList):
            return userOperationsList[operationIndex]

    else:
        for operation in userOperationsList:
            if operation.value == operationString:
                return operation

    return None
