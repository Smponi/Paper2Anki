from loguru import logger
from tools.util import get_log_name
import sys

# YOU NEED TO REMOVE THE OLD CONFIG BEFORE REWRITING IT
logger.remove()
logger.add(get_log_name())
logger.add(sys.stderr, level="WARNING")
