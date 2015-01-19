# 一个将 JSON 转化为 JSONP 的 Service

## 使用方法
接受 GET 方法的 HTTP 请求，其中 callback 参数和 url 参数为必选，callback 为 JSONP 回调函数名，url 为原始 JSON 服务 URL。

请求 JSON：

	GET https://api.github.com/users/octocat/orgs

请求 JSON：

    GET http://localhost:5000/?url=https%3A%2F%2Fapi.github.com%2Fusers%2Foctocat%2Forgs&callback=callback
