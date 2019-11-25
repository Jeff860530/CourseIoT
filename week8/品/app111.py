from flask import Flask, request, abort
from flask import render_template
from flask import make_response
import csmapi
csmapi.ENDPOINT  = 'https://2.iottalk.tw'  #Please fill the used IoTtalk server URL.


app = Flask(__name__)

@app.route('/<mac_addr>/<count>/<count1>/<count2>/<count3>/<count4>/', methods=['GET', 'POST'])
def SwitchSetCount(mac_addr, count,count1,count2,count3,count4):
    try:
        registered_address=mac_addr
        profile = csmapi.pull(registered_address, 'profile') #Pull the profile of RemoteControl
        if profile:
            device_feature_list = profile['df_list']
            print("Device feature list = ", device_feature_list)

        control_channel_output = csmapi.pull(registered_address, '__Ctl_O__') #Pull the Output of Control Channel
        if control_channel_output:
            selected_device_feature_flags = control_channel_output[0][1][1]['cmd_params'][0]
            print("Selected device feature flags = ", selected_device_feature_flags)
            print(type(selected_device_feature_flags))
            a=str(selected_device_feature_flags)
            b=a.count('1', 0, 9)
            b1=a.count('1',9,18)
            b2=a.count('1',18,27)
            b3=a.count('1',27,36)
            b4=a.count('1',36,45)
            return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=b,count1=b4,count2=b1,count3=b2,count4=b3))
    except:
        return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count),count1=int(count1),count2=int(count2),count3=int(count3),count4=int(count4)))

if __name__ == "__main__":
    app.run('127.0.0.1', port=80, threaded=True, use_reloader=False)
