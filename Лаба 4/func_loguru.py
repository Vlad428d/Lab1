from loguru import logger
def log_demo_message(msg):
    logger.info(f"Лог: {msg}")
    return "Записано в лог"
