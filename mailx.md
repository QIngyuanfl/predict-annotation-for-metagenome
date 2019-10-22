# Linux服务器邮箱通知服务
mailx 是 一款linux自带的邮件服务命令行工具，可以及时反馈系统状态及脚本运行状态。方便分析人员，减少检查的时间以及漏查的问题
## mailrc 配置
```rc
set smtp-use-starttls
set ssl-verify=ignore
set smtp=smtp://smtp.qq.com:587
set smtp-auth=login
set smtp-auth-user=username@qq.com
set smtp-auth-password=password
set from=user@qq.com
set nss-config-dir=/sysdata/Meta/.certs
```
## 将第三方公钥添加到信任名单
```sh
$ echo -n | openssl s_client -connect smtp.qq.com:587 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /sysdata/Meta/.certs/qq.crt
$ certutil -A -n "GeoTrust SSL CA" -t "C,," -d /sysdata/Meta/.certs -i  /sysdata/Meta/.certs/qq.crt
$ certutil -A -n "GeoTrust Global CA" -t "C,," -d /sysdata/Meta/.certs -i  /sysdata/Meta/.certs/qq.crt
$ certutil -A -n "GeoTrust SSL CA - G3" -t "Pu,Pu,Pu" -d /sysdata/Meta/.certs/./ -i  /sysdata/Meta/.cert/qq.crt
$ certutil -L -d /sysdata/Meta/.certs
```
## 基本命令
```
$ echo "your content" |mailx -v -s "yout title" username@domain.com
$ mailx -v -s "your title"  username@domain.com < file.txt
```
