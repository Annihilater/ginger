服务器地址、端口、版本号：http://localhost:5000/v1



搜索书籍

`GET /v1/book/search?q={key_word}`



获得书籍详情页

`GET /v1/book/<int:isbn>/detail`



客户端注册
`POST /v1/client/register`



新建礼物
`POST /v1/gift/<int:isbn>`



获取 Token
`POST /v1/token`



校验 Token 信息
`POST /v1/secret`



超级管理员查询用户
`GET /v1/user/<int:uid>`



超级管理员删除用户
`DELETE /v1/user/<int:uid>`



普通用户查询自己
`GET /v1/user`



普通用户删除自己
`DELETE /v1/user/`