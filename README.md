# BUAAMathmodeling-thesis

北航数学建模 LaTeX 模板 @ 专用版本（草

## 项目说明

基于北航开源俱乐部维护的的北航毕设论文的 LaTeX 模板修改的数学建模论文模板

## 依赖

模板依赖 v2.0 及以上版本的 ctex 包，请使用较新版本的 LaTeX 发行版。

目前已经测试的 LaTeX 发行版包括：

+ TeXLive 2015、TeXLive 2016、TeXLive 2019（** 推荐 **）
+ CTeX 2.9.3

对于老版本的 LaTeX 发行版，请通过包管理器升级 ctex 的版本。

**作者的使用环境：完整安装TeX Live 2019 + Typora + Pandoc**

## 使用方法
0. \[推荐\]从Typora输出.tex文件之后，调整`build.py`的参数，然后运行`build.py`脚本一键生成.pdf。
--------- 原使用方法 ---------
1. 可以使用命令行或 PowerShell 等，配合项目中的 `mamske.bat` 批处理文件进行编译，详细使用方法请见 `mamske.bat` 文件；

2. 使用 Makefile，需要所使用的命令行环境支持 Make，cd 到 BUAAthesis 相应目录，目前支持以下功能

+ `make bachelor` # 编译本科生的 LATEX（文件默认项，亦可直接输入 make）
+ `make master` # 编译研究生的 LATEX 文件
+ `make clean` # 删除编译过程中生成的文件（除了 pdf）
+ `make depclean` # 删除编译过程中生成的文件（包括 pdf）

3. 使用 Visual Studio Code 等软件进行编译，请使用 `xelatex->bibtex->xelatex*2` 方式进行编译；
