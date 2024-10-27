# Airport-Free
## 免费节点，每3h自动更新订阅

- 更新时间（UTC+8）：`<update_time>`
- [v2ray节点多合一](https://cdn.jsdelivr.net/gh/xiaoji235/airport-free/v2ray.txt)（不建议用这个，因为太多了系统ping不过来）
- [v2ray节点多合一](https://ghp.ci/https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt)（如果第一个无法订阅就用这个）

### 已开启jsdelivr CDN加速：

<table style="width:90%">
<tr><td>v2ray</td>
<v2ray_list>
</tr>
<tr><td>clash</td>
<clash_list>
</tr>
</table>

### 如果订阅更新不了再用这个：

<table style="width:90%">
<tr><td>v2ray</td>
<v2rayCDN_list>
</tr>
<tr><td>clash</td>
<clashCDN_list>
</tr>
</table>

## 源码
- 源码已开源，详情请移步[GitHub](https://github.com/xiaoji235/airport-free/tree/main)

## 特点
- 只需将v2ray的py脚本存放到 node/v2/ 当中后前往 <strong>action</strong> 运行workflow后即可看到输出结果。
- 只需将clash的py脚本存放到 node/clash/ 当中后前往 <strong>action</strong> 运行workflow后即可看到输出结果。

## 说明
- 本源码已默认添加了6个节点源（实际只有5个来源站），每隔3个小时自动检测更新，如果有新源欢迎大家前往[issues](https://github.com/xiaoji235/airport-free/issues)提交节点源！
- 修改README.md请前往：<strong>nodes/README.md</strong>

## 问题
- 由于多个网站收录的节点有的可能重复，已做了去重处理，但可能仍有部分重复！
- 部分网站可能会由于长城或站点自身原因将来可能无法访问就可能导致无法更新订阅！

## 提示
- 所有数据来源于互联网，内容真实性请用户自行辨认。
- 本源码仅供Python学习，禁止用于违法犯罪行为，否则后果自负！
