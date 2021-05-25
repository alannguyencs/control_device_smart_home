from collections import OrderedDict

def collect_devices(workbook):
    devices = []
    sheet = workbook.sheet_by_name('Sheet1')
    for row_id in range(1, sheet.nrows):
        if not sheet.cell(row_id, 0).value: continue #empty cell
        device = OrderedDict()
        device['name'] = sheet.cell(row_id, 0).value.lower()
        device['type'] = sheet.cell(row_id, 1).value.lower()

        actions = sheet.cell(row_id, 2).value.lower().split(',')
        device['action_0'] = " ".join([action.strip().split('/')[0] for action in actions])
        device['action_1'] = " ".join([action.strip().split('/')[1] for action in actions])
        devices.append(device)

    return devices

def collect_requests(workbook):
    requests = []
    sheet = workbook.sheet_by_name('Sheet1')
    for row_id in range(sheet.nrows):
        request = sheet.cell(row_id, 0).value.lower()
        requests.append(request)

    return requests

