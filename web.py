import logging
from flask.logging import default_handler
from flask import Flask, redirect
from src.douyu import DouYu
from src.huya import HuYa
from src.bilibili import BiliBili
import loguru

logger = loguru.logger

web = Flask('__main__')


@web.route('/douyu/<id>')
def douyu(id):
    try:
        logger.info(f"{id}获取成功")
        return redirect(DouYu(id).get_real_url())
    except Exception as e:
        logger.error(e)


@web.route('/huya/<id>')
def huya(id):
    try:
        logger.info(f"{id}获取成功")
        return redirect(HuYa(id).get_real_url()['bd_flv'])
    except Exception as e:
        logger.error(e)


@web.route('/bilibili/<id>')
def bilibili(id):
    try:
        logger.info(f"{id}获取成功")
        return redirect(BiliBili(id).get_real_url())
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    logging.disable()
    web.logger.removeHandler(default_handler)
    logger.info("当前服务运行在 http://127.0.0.1:5867/")
    logger.info("目前支持斗鱼 douyu/虎牙 huya/B站 bilibili")
    logger.info("Bilibili区域性失效，等待上游算法更新.")
    web.run(port=5867, host='0.0.0.0')
