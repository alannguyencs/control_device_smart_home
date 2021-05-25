from constants import *
import xlrd
import workbook_extractor
import handler


device_path = "{}device.xlsx".format(DATA_PATH)
workbook = xlrd.open_workbook(device_path)
devices = workbook_extractor.collect_devices(workbook)

request_path = "{}request.xlsx".format(DATA_PATH)
workbook = xlrd.open_workbook(request_path)
requests = workbook_extractor.collect_requests(workbook)
for request in requests:
    print("request:", request)
    called_devices = handler.handle(request, devices)

    for device_score, id, action_0_score, action_1_score in called_devices[:5]:
        action = 'action_0' if action_0_score > action_1_score else 'action_1'
        print ("score = {:.2f}, device = {}, type = {}, action = {}".
               format(device_score, devices[id]['name'], devices[id]['type'], devices[id][action]))
    print ('---------------------\n')