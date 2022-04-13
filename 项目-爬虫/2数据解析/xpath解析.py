# xpath 是在xml中搜索内容的一门语言
#html 属于 xml
#注意节点关系，父节点、子节点、同胞节点
#安装lxml模块
from lxml import etree
xml = '''
<root>
    <id>1</id>
    <name>麻花藤</name>
    <price>1.99</price>
        <nick id="10000">1</nick>
        <nick id="10001">1</nick>
    <author>
        <nick id="20000">王者农药</nick>
        <nick id="20001">全军吃鸡</nick>
            <div>
                <nick>姜子牙</nick>
            </div>
    </author>
    <partner>
        <nick id="dnf">毒奶粉</nick>
        <nick id="40000">撸啊撸</nick>
    </partner>
</root>
'''#自定义一个xml文件，当然也可以是html等超文本文件
tree = etree.XML(xml)#以XML形式打开xml文件
result1 = tree.xpath("/root")
print(result1)#此时输出的是对象
result2 = tree.xpath("/root/name/text()")#查找name路径下的text文件，返回一个集合
print(result2)
result3=tree.xpath("/root/author//text()")#//表示author下的所有子路径
print(result3)
result4=tree.xpath("/root/*/nick/text()")#表示任意父路径下的nick路径中的text文件
print(result4)#注意，有无*输出的内容区别
result5=tree.xpath("/root//nick/text()")
print(result5)
result6=tree.xpath("/root//nick/@id")#用@拿属性值
print(result6)