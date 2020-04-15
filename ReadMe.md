详细的教程文档请移步：[Rasa使用系列](http://bluecollarhub.cn/?categoryId=80)

备注：Rasa使用系列翻译自[Rasa官方文档](https://rasa.com/docs/rasa/)，并结合了项目实战经验，欢迎star和issues，我们共同讨论、学习！

## 1. 安装rasa
### 1.1 环境要求
- python 3.6+
- mitie
- jieba

### 1.2 安装步骤
**1.2.1. 安装rasa**
```shell
# 当前版本为1.7.0
# 该命令运行时间较长，会安装完所有的依赖
pip --default-timeout=500 install -U rasa
```

**1.2.2. 安装mitie**
```shell
# 在线安装Mitie
pip install git+https://github.com/mit-nlp/MITIE.git
pip install rasa[mitie]
```

**1.2.3. 安装jieba**  

```shell
# 安装Jieba中文分词
pip install jieba
```

## 2. 训练模型  
&emsp;训练NLU和Core模型。
```shell
rasa train
```

```使用Supervised_Embedding训练NLU和Core模型
rasa train --config configs/jieba_supervised_embeddings_config.yml
```

## 3. 运行服务  

**（1）启动Rasa服务**
```shell
# 启动rasa服务
# 该服务实现自然语言理解(NLU)和对话管理(Core)功能
# 注：该服务的--port默认为5005，如果使用默认则可以省略
python -m rasa run --port 5005 --endpoints configs/endpoints.yml --credentials configs/credentials.yml --debug
```

**（2）启动Action服务**
```shell
# 启动action服务
# 注：该服务的--port默认为5055，如果使用默认则可以省略
Python -m rasa run actions --port 5055 --actions actions --debug 
```

**（3）启动server.py服务**
```shell
python server.py
```

当**Rasa Server**、**Action Server**和**Server.py**运行后，在浏览器输入测试：

` http://127.0.0.1:8088/ai?content="查询广州明天的天气"`

### 测试数据模型
**使用test_stories.md测试数据模型**
```test
rasa test --e2e --stories test/test_stories.md
```
**使用交叉验证估计模型的概括程度**
```使用标识--cross-validation进行交叉验证
rasa test nlu -u data/nlu.md --config config.yml --cross-validation
```
**评估训练模型**
``` 待摸索
rasa test core --stories test/test_stories.md --out results
```

## License
> ```
> Copyright 2020 chengling
> 
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
> 
>    http://www.apache.org/licenses/LICENSE-2.0
> 
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
> ```

