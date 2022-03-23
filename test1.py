"""
 * Project name(项目名称)：Python去除字符串中空格
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:41
 * Version(版本): 1.0
 * Description(描述)： Python strip()方法
strip() 方法用于删除字符串左右两个的空格和特殊字符
str.strip([chars])
其中，str 表示原字符串，[chars] 用来指定要删除的字符，可以同时指定多个，如果不手动指定，则默认会删除空格以及制表符、回车符、换行符等特殊字符。
 """

if __name__ == '__main__':
    str1 = "   The method is used to remove spaces and special characters on the left and right sides of a string  "
    print(str1)
    print(str1.strip())
    str1 = "\t\tThe method is used to remove spaces and special \tcharacters on the left and right sides of a string  "
    print(str1)
    print(str1.strip("\t"))

    input()
