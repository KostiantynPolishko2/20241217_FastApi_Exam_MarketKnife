import uvicorn
import os
from dotenv import load_dotenv
from config_server import ConfigServer
from app_knife.__init__ import init_routes as init_knife_routes
from app_auth.__init__ import init_routes as init_auth_routes
from app_redis.__init__ import init_routes as init_redis_routes

load_dotenv()

handle_server = ConfigServer('knife')
app = handle_server()

init_auth_routes(app)
# init_knife_routes(app)
# init_redis_routes(app)

host = os.environ['SERVER_HOST']
port = int(os.environ['SERVER_PORT'])

if __name__ == '__main__':
    # pass
    uvicorn.run(app, host=host, port=port)