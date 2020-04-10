# coding: utf-8
import os
import sys
import codecs

path = "D:\\code\\fuckingTeX\\BUAAmathmodel-master\\"   #项目路径
f_path = path + "artesttrue.tex"    #原始文件
f_newpath = path + "article.tex"    #目标文件
f_temppath = path + "temp.tex"      #临时文件

f = codecs.open(f_path,"r",encoding='utf-8')
f_new = codecs.open(f_newpath,'w',encoding='utf-8')
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
liste = f.readlines() 

for li in liste:
    if "\\section" in li:#这里是替换的内容
        f_temp.write(li.replace("\\section", '\\title'))
    else:
        f_temp.write(li)
f_temp.close()

f_temp = codecs.open(f_temppath,'r',encoding='utf-8')
liste = f_temp.readlines() 
f_temp.close()
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
for li in liste:
    if "\\subsection" in li:#这里是替换的内容
        f_temp.write(li.replace("\\subsection", '\\chapter'))
    else:
        f_temp.write(li) 
f_temp.close()  

f_temp = codecs.open(f_temppath,'r',encoding='utf-8')
liste = f_temp.readlines() 
f_temp.close()
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
for li in liste:
    if "\\subsubsection" in li:#这里是替换的内容
        f_temp.write(li.replace("\\subsubsection", '\\section'))
    else:
        f_temp.write(li) 
f_temp.close()  

f_temp = codecs.open(f_temppath,'r',encoding='utf-8')
liste = f_temp.readlines() 
f_temp.close()
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
for li in liste:
    if "\[" in li:#这里是替换的内容
        f_temp.write(li.replace("\[", '\\begin{gather*}'))
    else:
        f_temp.write(li) 
f_temp.close()  

f_temp = codecs.open(f_temppath,'r',encoding='utf-8')
liste = f_temp.readlines() 
f_temp.close()
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
for li in liste:
    if "\]" in li:
        f_temp.write(li.replace("\]", '\\end{gather*}'))
    else:
        f_temp.write(li)
f_temp.close()

f_temp = codecs.open(f_temppath,'r',encoding='utf-8')
liste = f_temp.readlines() 
f_temp.close()
f_temp = codecs.open(f_temppath,'w',encoding='utf-8')
for li in liste:
    if "chapter{引言}" in li:
        f_temp.write("\\chapter*{引言}\\label{header-n7}}") #在目录里添加引言和摘要的不参与标号
        f_temp.write("\\addcontentsline{toc}{chapter}{引言}")
    elif "chapter{摘要}" in li:
        f_temp.write("\\chapter*{摘要}\\label{header-n12}}")
        f_temp.write("\\addcontentsline{toc}{chapter}{摘要}")
    else:
        f_temp.write(li)
f_temp.close()

#---------------这里是一个完成了替换的分割线---------------
f_tempp = codecs.open(f_temppath,'r',encoding='utf-8')
list2 = f_tempp.readlines()
for line in list2:
    if "\\documentclass[" in line:
        print("1")
        f_new.write("\documentclass[bachelor,openany,oneside,color]{buaathesis}\n")
    elif "]{article}" in line:
        print("2")
        continue
    elif '\\usepackage{lmodern}' in line:
        f_new.write("\\usepackage{cjkindent}\n")
        f_new.write("\\usepackage{gbt7714}\n")
        f_new.write("\\usepackage{amsmath}\n")
        f_new.write("\\citestyle{numerical}\n")
        f_new.write(line)
    elif "\\setcounter{secnumdepth}" in line:
        f_new.write("\\renewcommand {\\thetable} {\\thechapter{}-\\arabic{table}}\n")
        f_new.write("\\renewcommand {\\thefigure} {\\thechapter{}-\\arabic{figure}}\n")
    elif "\\begin{document}" in line:
        f_new.write(line)
        f_new.write("\\pagestyle{mainmatter}\n")
        f_new.write("\\include{data/com_info}\n")
        f_new.write("\\titlech\n")
        f_new.write("\\tableofcontents\n")
        
    elif "\\label{header-n2}}" in line:
        f_new.write(line)
        f_new.write('\\mainmatter')
    elif "\\chapter" in line:
        f_new.write(line)
        f_new.write('\\setcounter{table}{0}')
        f_new.write('\\setcounter{figure}{0}')

    else:
        f_new.write(line)
f.close()
f_tempp.close()
f_new.close()
os.chdir(path)
os.system("xelatex "+f_newpath)
os.system("bibtex "+f_newpath)
os.system("xelatex "+f_newpath)
os.system("xelatex "+f_newpath)