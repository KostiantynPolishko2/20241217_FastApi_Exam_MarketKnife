import uvicorn
from config_server import ConfigServer
from app_knife.__init__ import init_routes as init_knife_routes
from app_auth.__init__ import init_routes as init_auth_routes
import os
from dotenv import load_dotenv

load_dotenv()

handle_server = ConfigServer('knife')
knife_server = handle_server()

init_auth_routes(knife_server)
# init_knife_routes(knife_server)

host = os.environ['SERVER_HOST']
port = int(os.environ['SERVER_PORT'])

if __name__ == '__main__':
    uvicorn.run(knife_server, host=host, port=port)