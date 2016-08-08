# coding=utf-8
# 获取系统平台信息

import platform

print platform.platform() #鑾峰彇鎿嶄綔绯荤粺鍚嶇О鍙婄増鏈彿锛屸�橶indows-7-6.1.7601-SP1鈥�
print platform.version() #鑾峰彇鎿嶄綔绯荤粺鐗堟湰鍙凤紝鈥�6.1.7601鈥�
print platform.architecture() #鑾峰彇鎿嶄綔绯荤粺鐨勪綅鏁帮紝(鈥�32bit鈥�, 鈥榃indowsPE鈥�)
print platform.machine() #璁＄畻鏈虹被鍨嬶紝鈥檟86鈥�
print platform.node() #璁＄畻鏈虹殑缃戠粶鍚嶇О锛屸�檋ongjie-PC鈥�
print platform.processor() #璁＄畻鏈哄鐞嗗櫒淇℃伅锛屸�檟86 Family 16 Model 6 Stepping 3, AuthenticAMD鈥�
print platform.uname() #鍖呭惈涓婇潰鎵�鏈夌殑淇℃伅姹囨�伙紝uname_result(system=鈥橶indows鈥�, node=鈥檋ongjie-PC鈥�,


#杩樺彲浠ヨ幏寰楄绠楁満涓璸ython鐨勪竴浜涗俊鎭細

print platform.python_build()
print platform.python_compiler()
print platform.python_branch()
print platform.python_implementation()
print platform.python_revision()