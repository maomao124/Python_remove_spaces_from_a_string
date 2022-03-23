"""
 * Project name(项目名称)：Python去除字符串中空格
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 20:48
 * Version(版本): 1.0
 * Description(描述)： Python rstrip()方法
rstrip() 方法用于删除字符串右侧的空格和特殊字符
 """

if __name__ == '__main__':
    str1 = "   The method is used to remove spaces and special characters on the right sides of a string  "
    print(str1)
    print(str1.rstrip())
    str1 = "\t\tThe method is used to remove spaces and special \tcharacters on the right sides of a string\t\t"
    print(str1)
    print(str1.rstrip("\t"))

    input()
