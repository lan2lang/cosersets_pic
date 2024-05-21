### **网址**： [首页 | Cosersets](https://www.cosersets.com/1/main) （图集）

#### 主程序

```
目前可用：循环实现地址爬取.py(生成下载链接)，fast_download.py下载图片
```

**角色**：

```html
 <div class="cell" >    
```

遍历出所有的主角：即标签内的文本

132个



**下载**：

先尝试下载一个目录下的所有图片

 https://www.cosersets.com/1/main/七月喵子/粉嫩的水手服

下载具体页面成功



### **后台请求地址**：

 https://www.cosersets.com/api/list/1?path=%2FFushii_%E6%B5%B7%E5%A0%82%2F%E8%BF%91%E8%B7%9D%E7%A6%BB%E6%81%8B%E7%88%B1&password=&orderBy=&orderDirection= 

地址： https://www.cosersets.com/api/list/1?path= 

参数： path   /Fushii_海堂/洛丽塔

### 待办

- [ ] 及时关闭请求
- [x] 设置请求间隔
- [ ] 断点续传
- [ ] 视频太大可能会下载失败（请手动删除视频链接，或者调大请求间隔）



### **已处理**：

1. 长时间连接会出现远程服务器关闭连接(已优化)
   3. 动态设置用户标识（已实现）
2. 未实现协程下载（已实现）aiohttp
4. 不支持三层目录和视频的下载（已实现）

