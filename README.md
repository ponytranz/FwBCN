# RenPy 汉化工作流

## 待办事项

- [x] 将翻译文件转换到翻译平台可接受的格式
- [x] 自动化从平台拉取和提交翻译
- [x] 自动化将翻译文件从翻译平台格式转换回 rpy
- [ ] 自动化拉取成员贡献排行 (Paratranz)
- [ ] 自动化转换编译以及打包发布
- [ ] 自动化导出翻译文件和转换格式 (适用于原游戏更新中的项目)

## 已知问题

### 转换成 json 后有少量项目乱序到最后

怀疑是 for of 乱序的问题, 但是无法复现。
写了一个重新排序，但是上传到 Paratranz 没有变化，只能每次拉取翻译时都重新排序了。
下次上传到 Paratranz 之前应该至少来回转换一次检查是否有顺序变化。

### RenPy 引擎问题

<https://github.com/renpy/renpy/issues/2862>
菜单的说明文字使用说话人时，没有被识别为可以翻译的字段。
并且无法使用 `_()` 手动标注为可以翻译的字段。
说话人在游戏内显示正常。
不使用说话人时，可以被识别为可以翻译的字段。

### RenPy 引擎问题 2

在 WSL Ubuntu 环境下无法正常运行 renpy.sh 以进行命令行游戏构建。

```log
Full traceback:
  File "launcher/game/web.rpyc", line 26, in script
    ��t���ӞL{zb�.,�Ӄ"h��xpl#rW �S��+��     �C��F�nN-�*<�������qHWǖr��i������R6�AK<,�����.�����(;�*�<]9����W�[d=40�}M��#�t�
                                                                                                                                    Ћ<�m�4�>L����Eg��#��o`-/)���8N��lT}Q����J
                                                                                                                                                                               ����+-"-�vX�hO���<aJ������TR'*6(8   N��3�9��`O8و%��`O-mTxު��[� �hY�       e�P�@�G �"Մtx��3�8�q&��aPu��8�͝�߰�UǗ:�
  File "/mnt/d/renpy-7.4.6-sdk/renpy/ast.py", line 922, in execute
    renpy.python.py_exec_bytecode(self.code.bytecode, self.hide, store=self.store)
  File "/mnt/d/renpy-7.4.6-sdk/renpy/python.py", line 2218, in py_exec_bytecode
    exec(bytecode, globals, locals)
  File "game/web.rpy", line 29, in <module>
  File "/mnt/d/renpy-7.4.6-sdk/renpy/loader.py", line 985, in load_module
    exec(code, mod.__dict__)
  File "webserver.py", line 6, in <module>
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/site-packages/http/server.py", line 6, in <module>
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/BaseHTTPServer.py", line 102, in <module>
AttributeError: 'module' object has no attribute 'TCPServer'
While running game code:
  File "game/web.rpy", line 29, in <module>
AttributeError: 'module' object has no attribute 'TCPServer'



Full traceback:
  File "/mnt/d/renpy-7.4.6-sdk/renpy/bootstrap.py", line 326, in bootstrap
    renpy.main.main()
  File "/mnt/d/renpy-7.4.6-sdk/renpy/main.py", line 515, in main
    renpy.game.context().run(node)
  File "launcher/game/web.rpyc", line 26, in script
    ��t���ӞL{zb�.,�Ӄ"h��xpl#rW �S��+��     �C��F�nN-�*<�������qHWǖr��i������R6�AK<,�����.�����(;�*�<]9����W�[d=40�}M��#�t�
                                                                                                                                    Ћ<�m�4�>L����Eg��#��o`-/)���8N��lT}Q����J
                                                                                                                                                                               ����+-"-�vX�hO���<aJ������TR'*6(8   N��3�9��`O8و%��`O-mTxު��[� �hY�       e�P�@�G �"Մtx��3�8�q&��aPu��8�͝�߰�UǗ:�
  File "launcher/game/web.rpyc", line 26, in script
    ��t���ӞL{zb�.,�Ӄ"h��xpl#rW �S��+��     �C��F�nN-�*<�������qHWǖr��i������R6�AK<,�����.�����(;�*�<]9����W�[d=40�}M��#�t�
                                                                                                                                    Ћ<�m�4�>L����Eg��#��o`-/)���8N��lT}Q����J
                                                                                                                                                                               ����+-"-�vX�hO���<aJ������TR'*6(8   N��3�9��`O8و%��`O-mTxު��[� �hY�       e�P�@�G �"Մtx��3�8�q&��aPu��8�͝�߰�UǗ:�
  File "/mnt/d/renpy-7.4.6-sdk/renpy/ast.py", line 922, in execute
    renpy.python.py_exec_bytecode(self.code.bytecode, self.hide, store=self.store)
  File "/mnt/d/renpy-7.4.6-sdk/renpy/python.py", line 2218, in py_exec_bytecode
    exec(bytecode, globals, locals)
  File "game/web.rpy", line 29, in <module>
  File "/mnt/d/renpy-7.4.6-sdk/renpy/loader.py", line 985, in load_module
    exec(code, mod.__dict__)
  File "webserver.py", line 6, in <module>
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/site-packages/http/server.py", line 6, in <module>
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/BaseHTTPServer.py", line 102, in <module>
AttributeError: 'module' object has no attribute 'TCPServer'

While running game code:
  File "game/web.rpy", line 29, in <module>
AttributeError: 'module' object has no attribute 'TCPServer'
Traceback (most recent call last):
  File "/mnt/d/renpy-7.4.6-sdk/renpy/editor.py", line 105, in open
    subprocess.call([ "xdg-open", filename ])  # @UndefinedVariable
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/subprocess.py", line 173, in call
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/subprocess.py", line 325, in __init__
  File "/home/tom/ab/renpy-build/tmp/install.android-x86_64/lib/python2.7/subprocess.py", line 978, in _execute_child
OSError: [Errno 2] No such file or directory
```

报错为 `AttributeError: 'module' object has no attribute 'TCPServer'`
RenPy 自带 Python 2.7 环境以及一些编译过的 pyo 运行库，系统上没有安装其他 Python。
反编译 BaseHTTPServer.pyo, 里面 import 了 SocketServer 并使用了其中的 TCPServer, 但反编译 SocketServer 发现 TCPServer 是存在的。

### RenPy 引擎问题 3

对于字符串而不是显式的对话, RenPy 生成翻译文件时并不会给出唯一的 hash 值。
因此我使用文件和行号来生成 Paratranz 的字段 ID, 但是行号会发生变化和导致问题。
例如添加语言选择菜单之后, `y-screens.rpy` 后半段中的字段，行号有 6 行的偏移。

### FwB 项目问题

```log
While running game code:
    File "game/3map.rpy", line 647 in <module>
  NameError: name 'cindysex' is not defined
```
