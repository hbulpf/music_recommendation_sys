# 音乐推荐系统

[![知识共享协议（CC协议）](https://img.shields.io/badge/License-Creative%20Commons-DC3D24.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)
[![GitHub stars](https://img.shields.io/github/stars/hbulpf/music_recommendation_sys.svg?label=Stars)](https://github.com/hbulpf/music_recommendation_sys)
[![GitHub watchers](https://img.shields.io/github/watchers/hbulpf/music_recommendation_sys.svg?label=Watchers)](https://github.com/hbulpf/music_recommendation_sys/watchers)
[![GitHub forks](https://img.shields.io/github/forks/hbulpf/music_recommendation_sys.svg?label=Forks)](https://github.com/hbulpf/music_recommendation_sys/fork)


# 安装与使用

## 安装教程

#### 配置环境

| 组件            | 版本 |
| --------------- | ---- |
| scikit-surprise |  1.1.0    |
| gensim          |  3.8.1    |
| tensorfow       |      |

可以按照[环境配置文档](doc/environments.md)建立运行环境。

## 使用说明

### 启动程序
安装 python flask

```shell script
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
```

生成推荐模型

```shell script
python model.py
```


启动程序

```shell script
python main.py
```

查看 http://localhost:5000/ 访问音乐推荐系统。


### 作为服务启动

```shell script
sh service.sh
```

# 软件架构



# 参考

1. [Python Flask 快速部署网页](https://www.jianshu.com/p/c8b321087eca)
2. [Python Flask Web 框架入门](https://blog.csdn.net/sinat_38682860/article/details/82354342)
2. [Flask 快速入门](http://docs.jinkan.org/docs/flask/quickstart.html#a-minimal-application)
3. [基于python-flask搭建后台](https://blog.csdn.net/WinerChopin/article/details/81060230)



----------------------------------------

**项目规范**

本文使用 [`Markdown`](https://www.markdownguide.org/basic-syntax) 编写, 排版符合[`中文技术文档写作规范`](https://github.com/hbulpf/document-style-guide)。Find Me On [**Github**](https://github.com/hbulpf/music_recommendation_sys) , [**Gitee**](https://gitee.com/hecloudAi/music_recommendation_sys)

**友情贡献**

@[**RunAtWorld**](http://www.github.com/RunAtWorld)  &nbsp;
