# fastapi-docker-logs

> At the moment, an synchronous library is used to work with the Docker API, plans are to replace it with an asynchronous one.

### Methods
![image](https://user-images.githubusercontent.com/64792903/159360254-62f73e42-3cf6-4a97-ad18-5245b1fa9f63.png)

--- 
### Logs
![image](https://user-images.githubusercontent.com/64792903/159360978-3dc803cb-16ee-4d00-bbba-21d9a3119f07.png)


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
