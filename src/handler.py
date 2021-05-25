

def remove_non_alpha_characters(text):
    return ''.join(c for c in text if (c.isalpha() or c.isdigit() or c == ' '))

def get_words(sentence):
    sentence = remove_non_alpha_characters(sentence)
    return sentence.split(" ")

def count_matching_words(words, sentence):
    count = 0
    for word in words:
        count += int(word in sentence)
    return count

def compute_matching_score(words_a, words_b):
    a_in_b = count_matching_words(words_a, words_b)
    b_in_a = count_matching_words(words_b, words_a)
    matching_score = (a_in_b + b_in_a) / (len(words_a) + len(words_b))
    return matching_score

def compute_matching_request_device(request, device):
    request_words = get_words(request)
    device_words = get_words(" ".join(list(device.values())))
    action_0_words = get_words(device['action_0'])
    action_1_words = get_words(device['action_1'])

    device_score = compute_matching_score(request_words, device_words)
    action_0_score = compute_matching_score(request_words, action_0_words)
    action_1_score = compute_matching_score(request_words, action_1_words)
    return device_score, action_0_score, action_1_score

def handle(request, devices):
    called_devices = []
    for id, device in enumerate(devices):
        device_score, action_0_score, action_1_score = compute_matching_request_device(request, device)
        called_devices.append((device_score, id, action_0_score, action_1_score))
    called_devices.sort(reverse=True)
    return called_devices



