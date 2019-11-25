from flask import Flask, request, abort
from flask import render_template
from flask import make_response
import csmapi

csmapi.ENDPOINT  = 'https://6.iottalk.tw'  #Please fill the used IoTtalk server URL.

registered_address = 'The registered address of your device'  #Please fill the registered address of your device.

@apptest.route('/<mac_addr>/<count>/', methods=['GET', 'POST'])
def SwitchSetCount(mac_addr, count):
    if profile:
        device_feature_list = profile['df_list']
        print("Device feature list = ", device_feature_list)

    control_channel_output = csmapi.pull(registered_address, '__Ctl_O__') #Pull the Output of Control Channel
    if control_channel_output:
        selected_device_feature_flags = control_channel_output[0][1][1]['cmd_params'][0]
        print("Selected device feature flags = ", selected_device_feature_flags)
    return make_response(render_template('SwitchSet.html', mac_addr=mac_addr, count=int(count)))

if __name__ == "__main__":
    app.run('127.0.0.1', port=8011, threaded=True, use_reloader=False)
