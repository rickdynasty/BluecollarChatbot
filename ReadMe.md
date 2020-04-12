
## 1. 安装rasa
### 1.1 环境要求
- python 3.6+
- mitie
- jieba
### 1.2 安装步骤
**(1). 安装rasa**
```shell
# 当前版本为1.7.0
# 该命令运行时间较长，会安装完所有的依赖
pip --default-timeout=500 install -U rasa
```
**(2). 安装mitie**
```shell
# 在线安装Mitie
pip install git+https://github.com/mit-nlp/MITIE.git
pip install rasa[mitie]
```

**(3). 安装jieba**  
```shell
# 安装Jieba中文分词
pip install jieba
```

## 2. 训练模型  
&emsp;当所有样本和配置文件准备好后，接下来就是训练模型了，打开命令终端执行下面的命令，该命令会同时训练NLU和Core模型。
```shell
rasa train
```

## 3. 测试assistant
&emsp;在命令终端，输入下面命令：

```shell
rasa shell
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

