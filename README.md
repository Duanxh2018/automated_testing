# robot framework + python实现http接口自动化测试框架

用robot和python实现http接口自动化测试工具，测试数据存在excel表格中

测试步骤：
1、通过编写测试用例，用例数据存放到表格中；

2、修改rfcode文件下配置信息中RequestHeaders.txt中Host地址和config.txt中的用例的存放路径（按实际填写）

3、修改pycode下Common_Excel.py和Common_Exec.py中的用例的存放路径（按实际填写）

4、启动RF，执行用例（备注：执行的sheet页面可通过修改代码中的代码进行修改）