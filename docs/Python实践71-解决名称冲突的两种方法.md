### 名称冲突
- 如果两个包中定义的函数，类，或者子模块互相重名，那么就可能会导致名称冲突，例如:
```
from analysis.utils import inspect
from frontend.utils import inspect    # 覆盖前一句导入的inspect 
```

### 解决方法1
- 在import语句中，通过as语句，给引入当前作用域中的属性重新起名，例如：
```
from analysis.utils import inspect as analysis_inspect
from frontend.utils import inspect as frontend_inspect
```
- 凡是通过import语句引入的内容，都可以通过as子句来改名，及时引入整个模块，也依然能用as为其改名。

### 解决方法2
- 每次使用模块时都从最高层的路径来时，完整地写出各模块的名称。例如：
```
import analysis.utils
import frontend.utils
```
- 然后通过analysis.utils.inspect和frontend.utils.inspect这样完整的路径来访问这两个模块中的函数。