FROM registry.cn-shanghai.aliyuncs.com/devcon/spiderdev:2.4
ADD . /app
WORKDIR /app
RUN mkdir /app/log
RUN chmod +x /app/start.sh
RUN python3 -m pip install arrow -i https://pypi.tuna.tsinghua.edu.cn/simple/
CMD ["/app/start.sh"]


