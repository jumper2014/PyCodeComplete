# coding=utf-8
# 使用sysconfig

import sysconfig

print sysconfig.get_config_var('Py_ENABLE_SHARED')
print sysconfig.get_config_var('LIBDIR')
print sysconfig.get_config_vars('AR', "CXX")


print sysconfig.get_scheme_names()
print sysconfig.get_path_names()

print sysconfig.get_python_version()
print sysconfig.get_platform()

# return true if current python installation was built from source
print sysconfig.is_python_build()

print sysconfig.get_config_h_filename()
print sysconfig._get_makefile_filename()