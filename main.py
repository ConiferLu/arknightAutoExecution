if __name__ == '__main__':
    import pyautogui
    import time
    with open('log.txt', 'w') as fp:
        fp.write(time.strftime("%m/%d", time.localtime()) + '\n')

    # pyautogui.PAUSE = 2.5
    # pyautogui.position()
    #
    # screenWidth, screenHeight = pyautogui.size()
    # print(screenWidth, screenHeight)
    # currentMouseX, currentMouseY = pyautogui.position()
    # print(currentMouseX, currentMouseY)
    #
    # pyautogui.moveTo(100, 200, duration=0.2)


    # b = pyautogui.alert(text='要开始程序么？', title='请求框', button='OK')
    # print(b)  # 输出结果为OK
