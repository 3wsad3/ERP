import os
import pytest
import sys
import logging

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) == 2:
        if sys.argv[1] == "test":
            # 测试环境的地址
            os.environ["URL"] = "http://192.168.10.142:80"
            # 我这边的测试环境的数据没有变化，实际情况可能会发生改变
            # 根据实际情况来修改下面的字典内的值就好了
            os.environ["DB"] = str({
                "host": "192.168.10.142",
                "port": 3306,
                "database": "xingyun",
                "user": "root",
                "password": "123456"
            })
            os.environ["ENV"] = "test"

        elif sys.argv[1] == "prod":
            # 生产环境的环境变量
            os.environ["URL"] = "http://192.168.10.142:80/api/cloud-api"
            os.environ["DB"] = str({
                "host": "192.168.10.142",
                "port": 3306,
                "database": "xingyun",
                "user": "root",
                "password": "123456"
            })
            os.environ["ENV"] = "prod"
        else:
            logging.error("请传入正确的执行命令：python run.py test 或者 python run.py prod")

    else:
        logging.error("请传入正确的执行命令：python run.py test 或者 python run.py prod")

    pytest.main(["-vs", "./testcases/test_runner.py", "--alluredir", "./report/json_report", "--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")

    from utils.send_feishu_msg import send_feishu_message    # 发送测试报告消息
    send_feishu_message()