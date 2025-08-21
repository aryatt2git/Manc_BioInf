from git_repos.Manc_BioInf.PythonProgramming.logger import logger

logger.info("This is a test")
logger.debug("This is also a test")

def plusOne(number):

    try:
        return number + 1

    except Exception as e:
        logger.error(e)
        raise

plusOne('hello')