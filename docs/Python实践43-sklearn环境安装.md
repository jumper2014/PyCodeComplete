### 安装依赖包的步骤
- 为了保证环境干净和安装顺利，最好使用pipenv创建一个全新的Python开发环境，然后通过pipenv shell进入（参考Python实践32）
- 安装numpy包, pip install numpy
- 安装scipy包，pip install scipy
- 安装pandas包，pip install pandas
- 安装sklearn包，pip install sklearn
- 安装matplotlib包，pip install matplotlib


### 依赖包介绍
- Numpy是Python中科学计算的核心库。它提供一个高性能多维数据对象，以及操作这个对象的工具。
- scipy包含致力于科学计算中常见问题的各个工具箱。它的不同子模块相应于不同的应用。像插值，积分，优化，图像处理，统计，特殊函数等等。scipy是Python中科学计算程序的核心包; 它用于有效地计算numpy矩阵，来让numpy和scipy协同工作。
- Pandas最初被作为金融数据分析工具而开发出来，因此 pandas 为时间序列分析提供了很好的支持。 Pandas 的名称来自于面板数据（panel data）和python数据分析 （data analysis）。
- scikit-learn是Python的一个开源机器学习模块，它建立在NumPy，SciPy和matplotlib模块之上能够为用户提供各种机器学习算法接口，可以让用户简单、高效地进行数据挖掘和数据分析。
- Matplotlib是Python中最常用的可视化工具之一，可以非常方便地创建海量类型的2D图表和一些基本的3D图表。