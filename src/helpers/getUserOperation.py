def getUserOperation(operationName, userOperationsList):
    for operation in userOperationsList:
        if operation.value == operationName:
            return operation
    
    return None