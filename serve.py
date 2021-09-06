#!/home/pi/.local/bin/uvicorn
import subprocess
from CarMoveTankSteering import *
from starlette.applications import Starlette
from starlette.responses import FileResponse, PlainTextResponse, Response
from starlette.routing import Route
from starlette.requests import Request
#from gpiozero import CPUTemperature


c=CarMoveTankSteering()


async def homepage(request):
  return FileResponse('index.html')

async def temp(request):
  temp = str(subprocess.check_output(['vcgencmd', 'measure_temp']))
#  print(temp.split('=')[1])
  return PlainTextResponse(temp.split('=')[1].split('\\')[0])

async def motor(request): # scope, receive): #, send):
  if(request.method == 'POST'):
    data = await request.json()

    a = float(data['a'])
    c.a_speed=int(abs(a) * 99)
    if a > 0:
      c.a_forward()
    elif a < 0:
      c.a_backward()
    else: c.a_stop()


    b = float(data['b'])
    c.b_speed=int(abs(b) * 99)
    if b > 0:
#      print("b_forward");
      c.b_forward()
    elif b < 0:
#      print("b_backward");
      c.b_backward()
    else: c.b_stop()

    return PlainTextResponse('Ok')
  else:
    raise HTTPException(status_code=HTTP_405_METHOD_NOT_ALLOWED, detail="method_not_allowed")

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/', motor, methods=['POST']),
    Route('/temp', temp),
])
