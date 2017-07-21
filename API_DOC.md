# APIS

***
# 注册
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/signup/ |无| POST|

**URL Params**
```
无
```


**POST data(json):**
```
{
    "username": string,    //用户名
    "password": string     //用户密码
}
```

**Return data(json):**
```
{
    "created":id           //用户id
}
```
**Status Code**
```
200 OK
400 用户名或邮箱重复
502 服务器端错误
```
***
# 登录 
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/signin/||POST|


**URL Params**
```
无
```

**POST Data(json)**
```
{
    'username':string,     //用户名
    'password':string   //用户密码
}
```
**Return data(json):**
```
{
    "id":int
    "token": string
}
```
**Status Code**
```
200 OK
403 禁止访问，用户验证出错
502 服务器端错误
```
# 上传时间 

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/uploadtime/<int:id>/ |无| PUT|


**URL Params**

```
id: 用户ID
```
**POST Data(json)**

```
{
    "my_id":int  #用户id
    "time":int   #每次的总时间 
}
```

**Return data(json):**

```
{
    ＂status＂:200 　#200代表上传成功
}
```

# 获得宠物信息：
### 因为只在宠物这里需要获得时间，便没写获得时间的API
|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/getinfo/<int:id> |无| GET|
**POST Data(json)**

```
无
```

**Return data(json):**

```
{
    "name":String,
    "owner_id":int,
    "time":float,
    "forgive_time":int
}
```
***
# 原谅他:
### 每次调用这个方法都会减少一次原谅次数，初始默认原谅次数为５，最低为０.
### 为０时调用改方法不会做再减少次数，仅仅只会return一个该用户的原谅次数．

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/forgive/ |无| POST|
**POST Data(json)**
```
{
    'my_id':id
}
```
