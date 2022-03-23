"""
 * Project name(项目名称)：Python去除字符串中空格
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:46
 * Version(版本): 1.0
 * Description(描述)： Python lstrip()方法
lstrip() 方法用于去掉字符串左侧的空格和特殊字符。
str.lstrip([chars])
其中，str 和 chars 参数的含义，分别同 strip() 语法格式中的 str 和 chars 完全相同。
 """

if __name__ == '__main__':
    str1 = "   The method is used to remove spaces and special characters on the left sides of a string  "
    print(str1)
    print(str1.lstrip())
    str1 = "\t\tThe method is used to remove spaces and special \tcharacters on the left sides of a string  "
    print(str1)
    print(str1.lstrip("\t"))

    input()
