import os
import os.path
import subprocess
from subprocess import call
import sys
sys.path.append("./mvn-Dependencies")
import config

current_dir = os.path.dirname(os.path.realpath(__file__))

files = config.files
name_space = config.name_space
repository_url = 'https://raw.githubusercontent.com/liaohuqiu/umeng-share/master/mvn-dependencies/repository'
latest_version = '1.0.1.1-SNAPSHOT'

read_me = """

## 资源

将资源打包成aar包，aar包已经发布到中央库，在maven中引入:

```
<dependency>
    <groupId>in.srain.mix</groupId>
    <artifactId>umeng-share</artifactId>
    <version>{latest_version}</version>
    <type>aar</type>
</dependency>
```

在gradle中:

```
compile 'in.srain.mix:umeng-share:{latest_version}'
```

## 依赖库

各个依赖的jar包，通过mavn方式引入:

### For maven

maven库地址:

```
<repository>
    <id>github-srain-umeng-lib</id>
    <url>{repository_url}</url>
    <releases>
        <enabled>true</enabled>
    </releases>
    <snapshots>
        <enabled>true</enabled>
    </snapshots>
</repository>
```

各个依赖组件:

```
{maven_dependencies}
```

### For gradle

依赖库地址:

```
maven {
    url '{repository_url}'
}
```

各个依赖组件:

```
{gradle_dependencies}
```
"""

maven_patten = """
<dependency>
    <groupId>%s</groupId>
    <artifactId>%s</artifactId>
    <version>%s</version>
    <type>%s</version>
</dependency>
"""

gradle_patten = "compile '%s:%s:%s@%s'\n"

maven_dependencies = '';
gradle_dependencies = '';

for file_name, version in files.iteritems():
    name, ext = file_name.split('.')
    maven_dependencies += maven_patten % (name_space, name, version, ext)
    gradle_dependencies += gradle_patten % (name_space, name, version, ext)

outfile = open('README.md', 'w')
read_me = read_me.replace('{maven_dependencies}', maven_dependencies)
read_me = read_me.replace('{gradle_dependencies}', gradle_dependencies)
read_me = read_me.replace('{repository_url}', repository_url)
outfile.write(read_me)
outfile.close()
