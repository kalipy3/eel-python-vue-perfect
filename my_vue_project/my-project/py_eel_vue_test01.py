import eel

#暴露给js调用
@eel.expose
def hello_world():
    return "Hello from python"

# 定义html文件所在文件夹名称
eel.init('dist')
#py调用js 必须在eel.init之后调用
eel.say_hello_js("i am py")
# 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
eel.start('index.html', port=0, size=(600,300))
