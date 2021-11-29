# -- coding: utf-8 --
import logging, time
def log():
    logger=logging.getLogger()
    logger.handlers.clear()
    logger.setLevel(logging.INFO) # 日志等级debug>info>warning>error>critical
    formatter=logging.Formatter('%(asctime)s - %(filename)s[行号:%(lineno)s] - %(levelname)s - %(message)s')
    console=logging.StreamHandler() # 流处理器，日志输出到控制台
    console.setFormatter(formatter)
    logger.addHandler(console)
    console.close()
    now=time.strftime('%Y%m%d')
    log_file=f'../log/{now}.log'
    file=logging.FileHandler(log_file, encoding='utf-8')
    file.setFormatter(formatter)
    logger.addHandler(file)
    file.close()
    return logger

if __name__ == '__main__':
    log().info('成功')
    log().warning('警告')
    log().error('错误')