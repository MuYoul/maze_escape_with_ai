import logging
from logging.handlers import RotatingFileHandler

# 로거 설정
def setup_logger():
    logger = logging.getLogger("MazeGameLogger")
    logger.setLevel(logging.INFO)

    # 콘솔 핸들러 설정
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)

    # 파일 핸들러 설정
    fh = RotatingFileHandler('maze_game.log', maxBytes=500000, backupCount=5)
    fh.setLevel(logging.INFO)
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)

    return logger

# 사용 예시
# logger = setup_logger()
# logger.info("This is a test log message.")
