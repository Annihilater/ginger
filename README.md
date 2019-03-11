# ginger
基于 Flask 的 RESTful API 项目（为之前的 fisher 项目创建 API）。



服务器地址、端口、版本号：http://localhost:5000/v1

| 功能               | Method | URL                       | DATA                                                         |
| ------------------ | ------ | ------------------------- | ------------------------------------------------------------ |
| 搜索书籍           | GET    | /book/search?q={key_word} | 无需登录                                                     |
| 获得书籍详情页     | GET    | /book/\<int:isbn\>/detail | 无需登录                                                     |
| 客户端注册         | POST   | /client/register          | {<br/>    "account": "nihao@qq.com",     "secret": "88888888",     "type": 100,     "nickname": "nihao" } |
| 新建礼物           | POST   | /gift/\<int:isbn\>        |                                                              |
| 获取 Token         | POST   | /token                    |                                                              |
| 校验 Token 信息    | POST   | /secret                   |                                                              |
| 超级管理员查询用户 | GET    | /user/\<int:uid\>         | 需要超级管理员 Token                                         |
| 超级管理员删除用户 | DELETE | /user/\<int:uid\>         | 需要超级管理员 Token                                         |
| 登录用户自我查询   | GET    | /user                     | 需要 Token                                                   |
| 登录用户自我删除   | POST   | /user                     | 需要 Token                                                   |
| 测试               | GET    | /book/                    | 无需登录                                                     |

