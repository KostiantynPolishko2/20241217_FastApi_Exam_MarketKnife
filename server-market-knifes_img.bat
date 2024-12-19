docker build --tag server-market-knifes:v1.0.0 .

docker run --detach --publish 8000:8000 --name market-knifes server-market-knifes:v1.0.0