Real-Url-Server

---

用一个链接直达直播源。

通过Flask建立服务器，使用直观的Url获取直播流。

---

本项目基于Python3.

本项目依赖于[real-url](https://github.com/wbt5/real-url) ，没有[real-url](https://github.com/wbt5/real-url) 就没有本项目。

---

1. 安装依赖库

```shell
pip install -r requirements.txt
```

2. 启动服务

```shell
python3 web.py
```

---

直播间链接：

http://<ip>:5867/<douyu/huya/bilibili>/<room_id>

e.g. 获取斗鱼房间号为100的直播源：

```
http://127.0.0.1:5867/douyu/100
```

此链接可直接放入播发器内播放。