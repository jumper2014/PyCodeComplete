### 知乎专栏《Python实践之路》
- https://zhuanlan.zhihu.com/python2018
- 文章目录: docs
- 代码目录: practice
--------------------------------------

## 索引
- 使用Paramiko远程登录免密码登录的机器：paramiko_with_key.py
- 对字典进行排序: sort_dict.py 
- locals()和globals()函数: locals_globals.py
- eval和全局局部名称空间: eval_globals_locals.py
- eval把字符串转换成list, dict, tuple: eval_str.py
- namedtuple: namedtuple_sample.py
- 用不到 50 行的 Python 代码构建最小的区块链: simple_block_chain.py
- 使用defaultdict提供默认值: defaultdict_sample.py, setdefault_sample.py
- 统计列表项出现的次数：count_sample.py, counter_sample.py
- 检查文件是否存在：file_dir_exists.py
- asyncio协程爬取B站: asyncio_sample.py
- 多线程爬取B站：thread_sample.py
- 线程池爬取B站：threadpool_sample.py
- 元类解释：user_metaclass.py
- 使用records第三方库操作MySQL：records_mysql.py

## list
* 检查列表是否为空的最好方法: check_list_empty.py 
* 将字符串逐字或者逐词翻转: reverse_word.py

## dict
* 求字典的交并差集合: dict_viewitems.py


## 类的语法
* str()和repr()的区别: str_and_repr.py
* global_var.py: 在函数中使用全局变量
* split_list_to_chunk.py: 把列表分隔成同样大小的块
* is_digit.py: 检查字符串是不是数字
* yesterday_tomorrow.py: 计算昨天和明天的日期
* last_friday.py: 寻找上一个星期五
* get_line_1.py: 根据指定的行号,从文本文件中读取一行数据
* get_line_2.py: 根据指定的行号,从文本文件中读取一行数据
* get_line_count_1.py: 计算文件行数
* get_line_count_2.py: 计算文件行数
* shuffle_list.py: 用随机顺序处理列表中的元素
* printf_in_python.py: 在python中使用printf
* 2d_array_exchange.py: 二维阵列变换
* return_elem_for_index.py: 如果列表中存在指定索引,就返回该索引的元素
* break_out_of_nested_loops.py: 从多重循环中退出
* use_all_for_import.py: 显示有限的接口到外部
* filter_sample.py: filter的用法
* __doc__sample.py: __doc__的用法
* __iter__sample.py: __iter__ 方法会返回一个迭代器iterator


## 有用的命令行脚本 python_command
* start_http_server.sh: 一行命令启动一个用于分享文件的http服务器

## 语法样例 syntax
* for_else.py: 用for else语句查找素数
* if_else.py: 把if else写在同一行
* switch_with_lambda.py: 用lambda模拟switch语句
* chaining_comparison.py: 链式比较运算符
* swap_variables.py: 快速交换变量的值
* list_copy.py: 完全复制列表,而不是源列表的引用
* list_dict_set_comprehension.py: 列表推导,字典推导,集合推导
* set_duplicate_intersection_difference.py: 查找列表中重复的元素，两个集合求交，求异
* call_asterisk_param.py: 函数调用时，参数使用星号
* double_asterisk_param.py: 函数定义和调用时用两个星号
* list_in_class.py: 类中的列表成员变量是所有对象共享
* kwargs_param.py: 在使用kwargs参数中如果获得键值对
* multi_exception_in_one_line.py: 一行里捕捉多个异常
* static_var_of_class.py: 类的静态变量
* range_vs_xrange.py: range和xrange的使用
* list_and_generator.py: 用range生成list和generator
* higher_order_function.py: 高阶函数
* dir_function.py: dir()和__dir__()函数
* eq_function.py: 函数__eq__()用于判断对象内容是否相等
* underscore.py: 使用下划线忽略不关心的变量
* infile_replace.py: 文本文件中替换字符串
* dict_get.py: 访问字典中键值的两种方法
* exec_eval.py: exec和eval函数的用法
* repr_sample.py: repr函数用来取得对象的规范字符串表示
* apply_func.py: 展示如何使用apply函数
* pass_func_as_param2.py: 将函数作为参数传入
* func_return_func.py: 函数返回另一个函数
* func_return_lambda.py: 返回lambda函数的函数
* user_defined_exception.py: 用户自定义异常类
* user_named_exception_class.py: 用户自定义的异常类
* enumerate.py: 循环访问序列中的元素和索引
* named_slice.py: 命名切片
* zip_reverse_dict.py: 使用zip反转字典
* merge_lists.py: 合并列表
* inner_class.py: 内部类
* dynamic_class.py: 根据参数动态生成类


## 有用的模块 modules
* paramiko_download_file.py: 远程下载文件
* paramiko_remote_exec.py: 远程执行命令
* paramiko_upload_file.py: 远程上传文件
* requests_sample.py: 易用的http网络库
* download_sample.py: 下载文件并保存
* tar_file.py: 压缩和解压*.tar.gz文件
* zip_file.py: 压缩和解压*.zip文件
* config_parser.py: 读取ini配置文件
* csv_sample.py: 读写csv文件
* decimal_sample.py: 十进制数学计算
* openpyxl_read.py: 读取excel文件
* openpyxl_write.py: 写入excel文件
* 线程池的例子: threadpool_sample.py
* 使用sysconfig: sysconfig_sample.py
* 用etree读写xml： etree_sample.py

## 装饰器 decorator
* time_this.py: 记录函数执行时间的装饰器
* log_it.py: 记录函数函数名和调用参数的装饰器

## 内置模块和函数 standard
* is_a_string.py: 判断一个值是否为string
* string_format.py: 用str.format格式化字符串
* string_template.py: 用string.Template格式化字符串
* ord_chr.py: 获得字符的ascii码值
* find_in_index.py: 在字符串中查找字串
* difflib_data.py: 比较序列,特别是文本文件
* stringio_and_cstringio.py: 使用file API来存取内存中的文本内容
* pprint_data.py: 格式化打印
* dir_copy.py: 复制文件夹
* dir_delete.py: 删除文件夹
* file_copy.py: 复制文件
* file_rename.py: 文件重命名
* file_archive.py: 文件压缩
* clock_time.py: 计算CPU用时和间隔时间
* copy_1.py: 返回具有同样内容和属性的对象的拷贝
* copy_2.py: 深度拷贝,对象中的属性和内容被分别和递归地拷贝
* min_max.py: 用heapq求最大最小元素
* thread_pool.py: 一行代码实现多线程/多进程
* defaultdict_sample.py: 演示使用defaultdict提供默认值
* platform_sample.py: 获取系统平台信息
* sys_args.py: 获取系统参数信息
* random_sample.py: 随机函数


## 令人迷惑的语法
* default_list_param.py: 变化的函数默认参数
* defaultdict_tree.py: 用缺省字典表示简单的树
* class_static_var.py: 类静态变量

## BKM 
* 获得hostname: get_host_name.py
* 日期字符串：date_string.py
