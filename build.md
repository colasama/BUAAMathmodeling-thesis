# 手动TeX转论文方式

## 添加内容

**修改：**\documentclass[bachelor,openany,oneside,color]{buaathesis}

% 参考文献

\usepackage{cjkindent} %首行缩进

\usepackage{gbt7714}

\usepackage{amsmath}
\citestyle{numerical}

**begin之前**

\renewcommand {\thetable} {\thechapter{}-\arabic{table}}
\renewcommand {\thefigure} {\thechapter{}-\arabic{figure}}

**begin之后**

% 页眉页脚样式
\pagestyle{mainmatter}

\include{data/com_info}

% 封面、任务书、声明
\titlech
% 目录
\tableofcontents

**title之后**

\mainmatter

## 注释掉的内容

%注释掉 %\setcounter{secnumdepth}{-\maxdimen} % remove section numbering

% 正文页码样式
\mainmatter

每章节前面：
\setcounter{table}{0}
\setcounter{figure}{0}

## 替换的内容

代码块替换为：
\begin{gather\*}
\end{gather\*}

\subsubsection 替换为 \section
\subsection 替换为 \chapter
`\\label\{(.*)\}\}` 替换为 null
`\\hyper(.*)%` 替换为 null

↑这两步可能不需要