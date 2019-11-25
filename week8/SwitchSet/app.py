import csmapi

from flask import Flask, request, abort
from flask import render_template
from flask import make_response

app = Flask(__name__)

csmapi.ENDPOINT  = 'https://6.iottalk.tw'  #Please fill the used IoTtalk server URL.

#registered_address = 'jefftest'  #Please fill the registered address of your device.
@app.route('/<mac_addr>',methods=['GET', 'POST'])
def SwitchSetCount(mac_addr, count=1,count1=1,count2=1,count3=1,count4=1):
    try:
        registered_address = mac_addr
        profile = csmapi.pull(registered_address, 'profile') #Pull the profile of RemoteControl
        if profile:
            device_feature_list = profile['df_list']
            print("Device feature list = ", device_feature_list)
            
        control_channel_output = csmapi.pull(registered_address, '__Ctl_O__') #Pull the Output of Control Channel
        print(registered_address)
        if control_channel_output:
            selected_device_feature_flags = control_channel_output[0][1][1]['cmd_params'][0]
            print(control_channel_output)
            print("Selected device feature flags = ", selected_device_feature_flags)#11000..
            flagstr=str(selected_device_feature_flags)
            count =flagstr.count('1',0, 9)
            print(count)
            count1=flagstr.count('1',9,18)
            print(count1)
            count2=flagstr.count('1',18,27)
            print(count2)
            count3=flagstr.count('1',27,36)
            print(count3)
            count4=flagstr.count('1',36,45)
            print(count4)
            return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count),count1=int(count4),count2=int(count1),count3=int(count3),count4=int(count2)))
        #count = selected_device_feature_flags.count('1')
        #print('Switch number on iottalk',count)
    except Exception as e:
        print('haha')
        print(count,count1,count2,count3,count4)
        print('ErrMsg:', e)
        return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count),count1=int(count4),count2=int(count1),count3=int(count3),count4=int(count2)))
#    finally:
#        return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count),count1=int(count4),count2=int(count1),count3=int(count3),count4=int(count2)))
if __name__ == "__main__":
    app.run('127.0.0.1', port=6967, threaded=True, use_reloader=False)
