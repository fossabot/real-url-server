from flask import Flask, redirect
from src.douyu import DouYu
from src.huya import HuYa
from src.bilibili import BiliBili

web = Flask('__main__')


@web.route('/douyu/<id>')
def douyu(id):
    return redirect(DouYu(id).get_real_url())


@web.route('/huya/<id>')
def huya(id):
    return redirect(HuYa(id).get_real_url())


@web.route('/bilibili/<id>')
def bilibili(id):
    return redirect(BiliBili(id).get_real_url())


if __name__ == '__main__':
    web.run(port=5867, host='0.0.0.0')
