import requests
from cacofonisk import AmiRunner, BaseReporter

try:
    class ReportAllTheThings(BaseReporter):
        def on_b_dial(self, caller, targets):
            target_channels = [target.name for target in targets]
            caller_number = caller.caller_id.num
            print("{} is now calling {}".format(
            caller_number, ', '.join(target_channels),))
            response = requests.post('https://alexcredit.ua/sip/getDepartmentByMobile',
                                     data={'mobile': caller_number})
            department_info = response.json()
            if department_info['department'] == 1:
                print('Station must to route number into Support')
            elif department_info['department'] == 2:
                print('Station must to route number into Collection')
            else:
                print('Else in support')
        #def on_up(self, caller, target):
            #target_number = target.caller_id.num
            #caller_number = caller.caller_id.num
            #print("{} is now in conversation with {}".format(caller_number, target_number))

        #def on_hangup(self, caller, reason):
            #caller_number = caller.caller_id.num
            #print("{} is no longer calling (reason: {})".format(caller_number, reason))
except Exception as e:
    print('Report Class:' + e)


reporter = ReportAllTheThings()
runner = AmiRunner(['tcp://admin:password@192.168.0.11:5038'], reporter)
runner.run()