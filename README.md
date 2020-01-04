# Academic-Report-Detection
## Usage
This real-time monitoring cawler can automatically search for the academic report news released by USTC, and sent emails to the appointed email address. In addition, the program can detect news which contains the specified keywords.

这个程序是中科大学术报告收集器，运行后可以自动收集各个学院放出来的学术报告信息，并发送到某指定邮箱。同时，用户也可以指定关键词，只有含有关键词的学术报告新闻才会被检测并发送。
## Setup
```
# Detect and send emails to the appointed address
python crawler.py --mail-to xxx@gmail.com
# Detect based on keywords
python craoler.py --mail-to xxx@gmail.com keyword1 keyword2
```


## 运行
```
# 监控并发送报告信息到指定邮箱
python crawler.py --mail-to xxx@gmail.com
# 只监控某些特定关键词
python crawler.py --mail-to xxx@gmail.com 关键词1 关键词2
```
