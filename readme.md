### 示例project

[https://github.com/harryhare/python_import_playground](https://github.com/harryhare/python_import_playground)

### 在不涉及包的情况下，引用其他文件

直接 import 文件路径就可以

### 包

包和普通目录的区别只是包多了个`__init__.py` 文件。

有了这个文件后，在import 时则可以用目录名，而不是直接引用文件名。

同时 import 后，只有`__init__.py` 文件中定义/import的东西才能在包外被引用，有点封装/头文件的意思。

所以如果package 路径下有其他文件，

一个办法是在 `__init__.py`  import 这些文件；

另一个办法是 `__all__=["pyfile_name","function_name","varible_name"]`

`__all__`只对 `from xxx import *` 形式的import 有效


### 运行

* PyCharm

    - 右键标记根目录是source root， 然后import 后面的路径要从这个source root 起的路径
    - 自建package 只要 引用对了就可以。
    - 依赖库 由于和python 的环境变量绑定，所以只要设置好 python的编译环境即可。

* 命令行

    - 设置PYTHONPATH

### 和其他语言比较

#### Go

- golang 在不使用 go module 的情况下，源码和依赖库一起被放在 GOPATH 下面
也就是 依赖库和源码在相同的位置。

- 在 使用 go module 后, 源码可以不在 GOPATH 下面，GOPATH 只是依赖库所在的位置。

#### C/C++

- C 的依赖库是由 静态库/动态库/头文件三部分组成，所以这里只考虑直接和代码相关的头文件。

- 我们都知道 #include 有两种方式，

    - `#include <stdio.h>`

    - `#include "mytest.h"`

    - 第一种先查找系统路径，第二种先在本地路径下查找文件

    - 同时，头文件的目录也可以在编译时指定，所以比较下来C 是最灵活的
    - 不过，mess up 系统路径，可能导致各种奇怪的问题，似乎并且没有版本管理系统


### 参考：
1.https://www.cnblogs.com/yinzhengjie/p/8587656.html
2.https://www.jianshu.com/p/ca469f693c31
