readme.txt

:Author: kalipy
:Email: kalipy@debian
:Date: 2021-01-28 16:25

#起步
安装：

npm install -g @vue/cli
# OR
yarn global add @vue/cli
创建一个项目：

vue create my-project
# OR
vue ui

官网：https://cli.vuejs.org/zh/

注意:vue-cli3版本之后没有config文件夹和vue.config.js了，要自己手动创建
请看:https://cli.vuejs.org/zh/config/#%E5%85%A8%E5%B1%80-cli-%E9%85%8D%E7%BD%AE


-------------------------------------------------
打包构建项目
    1. yarn build

    2. 把生成的dist文件夹下的index.html拖到浏览器运行

    3. 问题:
        webpack vue-cli等打包后生成的项目的资源路径默认都是以"/"根目录开始的，要改为相对路径，请自己创建vue.config.js配置文件，进行配置
        请看:https://cli.vuejs.org/zh/config/#%E5%85%A8%E5%B1%80-cli-%E9%85%8D%E7%BD%AE
