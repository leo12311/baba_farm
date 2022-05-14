import uiautomator2 as u2#引用ui自动化库
import time
import cv2
import opencv_cust.pic as pic_tool
import uiautomator2 as u2#引用ui自动化库
import time
d = u2.connect()#连接好安卓设备


def click_img(img_path):
    template = cv2.imread(img_path, 0)
    image = d.screenshot(format="opencv")
    res = pic_tool.find_pic(image, template, 0.6)
    if res:
        (x, y) = res
        (a, b) = d.window_size()
        print(x / a, y / b)
        d.click(x / a, y / b)
        return True
    else:
        return False


def exist_img(img_path):
    template = cv2.imread(img_path, 0)
    image = d.screenshot(format="opencv")
    res = pic_tool.find_pic(image, template, 0.6)
    return res

def go_to_task():
    if exist_img('res/baba/task_taobao.png'):
        return
    d.app_stop('com.taobao.taobao')
    d.app_start('com.taobao.taobao')
    d(description="浮层关闭按钮").click_exists(timeout=1)
    d(text="芭芭农场").click(timeout=5)
    # if click_img('res/baba/red_package.png'):
    #     d.press("back")
    #     d(text="芭芭农场").click(timeout=2)
    d(description="浮层关闭按钮").click_exists(timeout=2)
    d(text="继续努力").click_exists(timeout=3)
    if not click_img('res/baba/ji_fei_liao.png'):
        return

def start_taobao():
    d.app_stop('com.taobao.taobao')
    d.app_start('com.taobao.taobao')
    d(description="浮层关闭按钮").click_exists(timeout=1)
    d(text="芭芭农场").click(timeout=5)
    # if click_img('res/baba/red_package.png'):
    #     d.press("back")
    #     d(text="芭芭农场").click(timeout=2)
    d(description="浮层关闭按钮").click_exists(timeout=2)
    d(text="继续努力").click_exists(timeout=3)
    item = d(text="立即领取")
    if item:
        item.click()
        time.sleep(0.5)
        # 领取三个亲密度奖励
        d.click(0.209, 0.44)
        d.click(0.503, 0.434)
        d.click(0.807, 0.436)
        # 点击关闭
        d.click(0.907, 0.205)

    #全部领取
    d.click(0.822, 0.69)
    d(text="关闭").click_exists(timeout=1)
    #点击兔子
    d.click(0.189, 0.684)
    #点击集肥料
    d.click(0.75, 0.898)
    #做任务
    taobao_task()
    #施肥
    fertilize()


def get_bound():
    if d(text="亲密度"):
        d(text="亲密度").click()
        time.sleep(0.5)
        # 领取三个亲密度奖励
        d.click(0.209, 0.44)
        d.click(0.503, 0.434)
        d.click(0.807, 0.436)
        # 点击关闭
        d.click(0.907, 0.205)

def watch_15s():
    time.sleep(0.1)
    for i in range(5):
        d.swipe(500, 500, 500, 300, 0.1)
        time.sleep(3)
    time.sleep(0.3)
    d.press("back")

def taobao_task():
    time.sleep(1)
    if not exist_img('res/baba/task_taobao.png'):
        if not click_img('res/baba/ji_fei_liao.png'):
            return
    time.sleep(1)
    mark = d(text="去签到")
    if mark:
        mark.click()
    question = d(text="去答题")
    if question:
        question.click()
        time.sleep(0.5)
        #选B
        d.click(0.533, 0.904)
        #d.click(0.478, 0.9)
        time.sleep(1)
        #领奖励
        d(textContains="领取奖励").click_exists(timeout=1)
        time.sleep(1)
        click_img('res/baba/ji_fei_liao.png')
    taobo_life = d(text="去淘宝人生扔骰子(0/1)")
    if taobo_life:
        taobo_life.click()
        time.sleep(2)
        d.click(0.488, 0.677)
        time.sleep(2)
        d.click(0.488, 0.677)
        time.sleep(1)
        d.click(0.493, 0.645)
        time.sleep(1)
        d.press("back")

    taote = d(text="去淘特领好礼(0/1)")
    if taote:
        taote.click()
        time.sleep(3)
        go_to_task()

    task_list = ['逛精选好物(0/1)','逛精选商品(0/3)','逛精选商品(1/3)','逛精选商品(2/3)','搜一搜你心仪的宝贝(0/1)','浏览金币小镇得肥料(0/1)','浏览短视频(0/1)','逛精选好货(0/1)','浏览天天领现金(0/1)']
    for task_text in task_list:
        task_item = d(text=task_text)
        if task_item:
            print(task_item)
            task_item.click()
            time.sleep(1)
            shan_mo = d(text="闪魔")
            if shan_mo:
                shan_mo.click()
            if exist_img('res/baba/cash.png'):
                d.click(0.92, 0.254)
            watch_15s()
            go_to_task()
            d.swipe(500, 1000, 500, 700, 0.1)
    print('task_list process done')
    #上划
    d.swipe(500, 1000, 500, 800, 0.1)
    d(text="每日7点/12点/20点/22点各领1次").click_exists(timeout=1)
    time.sleep(1)
    d.click(0.92, 0.232)
    time.sleep(2)
    print('task process done')


#施肥
def fertilize():
    print('start fertilize')
    get_bound()
    if exist_img('res/baba/task_taobao.png'):
        d.click(0.92, 0.232)
    if not exist_img('res/baba/ji_fei_liao.png'):
        return
    while True:
        #点击兔子
        d.click(0.189, 0.684)
        #点击施肥
        d.click(0.546, 0.888)
        time.sleep(1)
        if click_img('res/baba/task_taobao.png'):
            # 施肥完成
            return
        item = d(text="立即领取")
        if item:
            item.click()
            time.sleep(0.5)
            #领取三个亲密度奖励
            d.click(0.209, 0.44)
            d.click(0.503, 0.434)
            d.click(0.807, 0.436)
            #点击关闭
            d.click(0.907, 0.205)
        #点击拆红包
        d.click(0.503, 0.709)
        d(text="关闭").click_exists(timeout=0.1)
        time.sleep(0.3)






def go_to_aplipay_task():
    if exist_img('res/baba/task_alipay.png'):
        return
    d.app_stop('com.eg.android.AlipayGphone')
    d.app_start('com.eg.android.AlipayGphone')
    d(text="芭芭农场").click(timeout=10)
    time.sleep(3)
    d(text="继续努力").click_exists(timeout=1)
    # 全部领取for i in range(3):
    d.click(0.822, 0.606)
    d(text="去领更多肥料").click_exists(timeout=1)
    # d(text="关闭").click_exists(timeout=1)
    # 点击集肥料
    d.click(0.867, 0.812)

def alipay_task():
    time.sleep(1)
    if not exist_img('res/baba/task_alipay.png'):
        # 如果不在任务页签
        if not click_img('res/baba/ling_fei_liao_alipay.png'):
            return
        else:
            time.sleep(1)
    #签到
    d.click(0.827, 0.43)
    #浏览页面

    task_list = ['逛一逛叫醒财神得大礼 (0/1)','逛一逛支付宝会员 (0/1)']

    for task_text in task_list:
        print(task_text + ' start')
        item = d(text=task_text)

        if not item:
            d.swipe(500, 1000, 500, 800, 0.2)
            d.swipe(500, 1000, 500, 800, 0.2)
            d.swipe(500, 1000, 500, 800, 0.2)
            item = d(text=task_text)
        if item:
            (x1,y1) = item.center()
            (x,y) = (x1+385,y1+20)
            (a, b) = d.window_size()
            print(x / a, y / b)
            d.click(x / a, y / b)
            #item.click()
            time.sleep(1)
            watch_15s()
            d(text="领取").click_exists(timeout=0.2)
            if not exist_img('res/baba/task_alipay.png'):
                go_to_aplipay_task()
        print(task_text + ' done')
    time.sleep(1)
    if exist_img('res/baba/task_alipay.png'):
        #领取合种奖励
        d.swipe(500, 1000, 500, 800, 0.1)
        d(text="领取").click_exists(timeout=0.2)
        #关闭任务页签
        d.click(0.925, 0.291)


#施肥
def alipay_fertilize():
    if not exist_img('res/baba/ling_fei_liao_alipay.png'):
        return

    while True:
        #点击全部领取
        #todo
        # if exist_img('res/baba/xx.png')
        #     d.click(0.812, 0.581)
        #点击施肥
        d.click(0.503, 0.815)
        item = d(text="点击领取")
        if item:
            item.click()
            time.sleep(0.3)
            #领取
            d.click(0.488, 0.666)
            time.sleep(0.3)
        if exist_img('res/baba/task_alipay.png'):
            #施肥完成
            break



def start_alipay():
    d.app_stop('com.eg.android.AlipayGphone')
    d.app_start('com.eg.android.AlipayGphone')
    d(text="芭芭农场").click(timeout=10)
    time.sleep(3)
    d(text="继续努力").click_exists(timeout=1)
    #全部领取for i in range(3):
    d.click(0.822, 0.606)
    d(text="去领更多肥料").click_exists(timeout=1)
    #d(text="关闭").click_exists(timeout=1)
    #点击集肥料
    d.click(0.867, 0.812)
    #做任务
    alipay_task()
    #施肥
    alipay_fertilize()
# startTaobao()
# taobao_task()
# fertilize()

# alipay_task()
alipay_fertilize()
# start_taobao()
# start_alipay()
# for i in range(3):
#     start_taobao()
    # start_alipay()