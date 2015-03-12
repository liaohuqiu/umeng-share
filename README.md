UMENG 分享组件aar格式包，使用aar包，所有umeng相关的资源就不用再放到项目中，让项目文件变得干净。

喜欢项目干净的同学，可以试试!

其他库依赖在这个项目中

https://github.com/liaohuqiu/umeng-libs

库发布到了mavenCentral，最新版本是 1.0.1.4-SNAPSHOT

```
<dependency>
    <groupId>in.srain.3rd</groupId>
    <artifactId>umeng-share</artifactId>
    <version>1.0.1.4-SNAPSHOT</version>
    <type>aar</version>
</dependency>
```

或者

```
compile 'in.srain.3rd:umeng-share:1.0.1.4-SNAPSHOT@aar'
```


项目依赖umeng的其他jar包，需要配置maven 源

Maven 中

```
<repository>
    <id>github-srain-umeng-lib</id>
    <url>https://raw.githubusercontent.com/liaohuqiu/umeng-libs/master/repository</url>
    <releases>
        <enabled>true</enabled>
    </releases>
    <snapshots>
        <enabled>true</enabled>
    </snapshots>
</repository>
```

gradle

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
