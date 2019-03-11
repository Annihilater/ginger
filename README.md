# ginger
基于 Flask 的 RESTful API 项目（为之前的 fisher 项目创建 API）。



服务器地址、端口、版本号：http://localhost:5000/v1

| 功能               | Method | URL                       |
| ------------------ | ------ | ------------------------- |
| 搜索书籍           | GET    | /book/search?q={key_word} |
| 获得书籍详情页     | GET    | /book/<int:isbn>/detail   |
| 客户端注册         | POST   | /client/register          |
| 新建礼物           | POST   | /gift/<int:isbn>          |
| 获取 Token         | POST   | /token                    |
| 校验 Token 信息    | POST   | /secret                   |
| 超级管理员查询用户 | GET    | /user/<int:uid>           |
| 超级管理员删除用户 | DELETE | /user/<int:uid>           |
| 普通用户查询自己   | GET    | /user                     |
| 普通用户删除自己   | DELETE | /user                     |

