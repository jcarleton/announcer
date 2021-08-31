import json
import yaml
import status

jsonexport = []

def main():
    with open("proc.yaml", 'r') as procStream:
        data_loaded = yaml.safe_load(procStream)

    for processes in data_loaded['proc']:
        proc = status.procStat(processes)
        jsonexport.append(proc)
        # print(proc)

    # create JSON object
    json.dumps(jsonexport)

    with open('payload.json', 'w', encoding='utf-8') as payload:
        json.dump(jsonexport, payload, ensure_ascii=False, indent=4)

    # debug output
    # print(jsonexport)

main()
