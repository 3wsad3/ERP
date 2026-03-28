# 环境基准地址
# BASE_URL = "http://192.168.10.142:80/api/cloud-api"

# excel格式的测试用例文件配置
#EXCEL_FILE = "./data/测试用例完整版.xlsx"
EXCEL_FILE = "./data/接口自动化测试用例.xlsx"
SHEET_NAME = "Sheet1"

# mysql配置
# DB_HOST = "192.168.10.142"
# DB_PORT = 3306
# DB_NAME = "xingyun"
# DB_USER = "root"
# DB_PASSWORD = "xiaobeiup2025"

# mysql资源销毁
SQL1 = ('SELECT * from base_data_product ORDER BY create_time desc;')
SQL2 = 'SELECT * from base_data_product ORDER BY create_time desc;'


# 飞书相关的配置文件
# webhook地址
WEBHOOK = "https://open.feishu.cn/open-apis/bot/v2/hook/ced991bd-df7e-4720-be97-f2cf1a392936"

# 项目名称
PROJECT = "星云ERP"

# 是否发送飞书消息的开关
FEISHU_IS_SEND = True

# 测试报告的地址
import os
# if os.environ["ENV"] == "test":
if os.environ.get("ENV") == "test":
    REPORT_PATH = "http://192.168.10.171:8080/view/all/job/ERP_git_pord/allure/"
# elif os.environ["ENV"] == "prod":
elif os.environ.get("ENV") == "prod":
    REPORT_PATH = "http://www.baidu.com/"
    