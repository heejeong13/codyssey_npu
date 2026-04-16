class Simulator:
    def __init__(self):
        pass

    def run(self):
        print('=== Mini NPU Simulator ===')
        print('[모드 선택]')
        print('1. 사용자 입력 (3X3)')
        print('2. data.json 분석')
        selectedMode = input('선택: ')

        if selectedMode == '1':
            print('mode1')
        elif selectedMode == '2':
            print('mode2')
        else:
            print('모드는 1 혹은 2만 존재합니다.')