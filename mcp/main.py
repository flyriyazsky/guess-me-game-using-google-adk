from mcp.server.fastmcp import FastMCP
import time
import logging
import os

mcp = FastMCP()

log_path = os.path.join(os.path.dirname(__file__), 'mcp.log')
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    filename=log_path, 
    filemode='a',
    force=True
)
logger = logging.getLogger(__name__)
# Force unbuffered logging
for handler in logger.handlers + logging.root.handlers:
    handler.flush()

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"MCPError {code}: {message}")

@mcp.tool()
def add_integer(a: int, b: int) -> int:
    '''
    Add two integers together and return the result.
    Arguments:
    a (int): The first integer to add.
    b (int): The second integer to add.
    Returns:    int: The sum of the two integers.
    '''
    logger.info(f"Adding integers: {a} + {b}")
    return a + b

@mcp.tool()
def subtract_integer(a: int, b: int) -> int:
    '''
    Subtract the second integer from the first and return the result.
    Arguments:
    a (int): The integer to subtract from.
    b (int): The integer to subtract.
    Returns:    int: The difference of the two integers. 
    '''
    logger.info(f"Subtracting integers: {a} - {b}")
    return a - b
@mcp.tool()
def divide_integer(a: float, b: float) -> float:
    '''
    Divide the first integer by the second and return the result.
    Arguments:
    a (float): The float to be divided.
    b (float): The float to divide by.
    Returns:    float: The quotient of the two integers.
    '''
    logger.info(f"Dividing floats: {a} / {b}")
    if b == 0:
        raise MCPError(code=400, message="Cannot divide by zero.")
    return float(a / b)

@mcp.tool()
def long_running_task(duration: int) -> str:
    '''
    Simulate a long-running task by sleeping for the specified duration.
    Arguments:
    duration (int): The number of seconds to sleep.
    Returns:    str: A message indicating that the task is complete.
    '''
    logger.info(f"Starting long-running task for {duration} seconds.")
    for i in range(duration):
        logger.info(f"Sleeping... {i+1}/{duration} seconds")
        time.sleep(2)
    logger.info("Task completed.")
    return f"Task completed after {duration} seconds."

if __name__ == "__main__":
    mcp.run(transport="stdio")



