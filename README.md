UMENG 分享组件aar格式包，使用aar包，所有umeng相关的资源就不用再放到项目中，让项目文件变得干净。

喜欢项目干净的同学，可以试试!

其他库依赖在这个项目中

https://github.com/liaohuqiu/umeng-libs

库发布到了mavenCentral，最新版本是 1.0.1.3-SNAPSHOT

Maven 中:

```
<dependency>
    <groupId>in.srain.3rd</groupId>
    <artifactId>umeng-share</artifactId>
    <version>1.0.1.3-SNAPSHOT</version>
    <type>aar</version>
</dependency>
```

gradle:

```
allprojects {
    repositories {
        jcenter()
        mavenCentral();
        maven {
            url 'https://oss.sonatype.org/content/repositories/releases'
        }
        maven {
            url 'https://oss.sonatype.org/content/repositories/snapshots'
        }
        maven {
            url 'https://raw.githubusercontent.com/liaohuqiu/umeng-libs/master/repository'
        }
    }
}
```



