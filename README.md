# fastapi-docker-logs

> Asynchronous work with Docker API is used.

### Methods
![image](https://user-images.githubusercontent.com/64792903/159360254-62f73e42-3cf6-4a97-ad18-5245b1fa9f63.png)

--- 
### Logs
![image](https://user-images.githubusercontent.com/64792903/159360978-3dc803cb-16ee-4d00-bbba-21d9a3119f07.png)


### Example CI/CD
https://github.com/dotX12/fastapi-docker-logs/blob/master/ci_cd.yml


### How to use in docker?
Example in CI/CD

```
docker run -d --network host \
-v /var/run/docker.sock:/var/run/docker.sock \
-e BASIC_AUTH_USERNAME=${{ secrets.BASIC_AUTH_USERNAME }} \
-e BASIC_AUTH_PASSWORD=${{ secrets.BASIC_AUTH_PASSWORD }} \
--name $(echo $IMAGE_NAME) \
-p 4243:80 \
--restart always \
$(echo $REGISTRY)/$(echo $IMAGE_NAME):$(echo $GITHUB_SHA | head -c7)
```
