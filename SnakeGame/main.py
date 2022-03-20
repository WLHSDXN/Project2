import math
import random
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0) #0为自己的摄像头
cap.set(3, 1280)        # 宽
cap.set(4, 720)         # 高

detector = HandDetector(detectionCon=0.8, maxHands=1)

class SnakeGameClass:
    def __init__(self,pathFood):             # 构造方法
        self.points = []            # 蛇身上所有的点
        self.lengths = []           # 每个点之间的长度
        self.currentLength = 0      # 蛇的总长
        self.allowedLength = 150    # 蛇允许的总长度
        self.previousHead = 0, 0    # 第二个头结点

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

        self.score = 0
        self.gameOver = False

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)


    def update(self, imgMain, currentHead):     # 实例方法

        if self.gameOver:
            cvzone.putTextRect(imgMain, "Game Over", [300, 400],
                               scale=7, thickness=5, offset=20)
            cvzone.putTextRect(imgMain, f'Your Score:{self.score}', [300, 550],
                               scale=7, thickness=5, offset=20)
        else:
            px, py = self.previousHead
            cx, cy = currentHead

            self.points.append([cx, cy])             # 添加蛇的点列表节点
            distance = math.hypot(cx - px, cy - py)  # 两点之间的距离
            self.lengths.append(distance)            # 添加蛇的距离列表内容
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length Reduction 收缩长度
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

            # Check if snake ate the food 是否吃了食物
            rx, ry = self.foodPoint
            # if rx < cx < rx + self.wFood and ry < cy < ry + self.hFood:
            #     print("ate")
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                print(self.score)

            # Draw Snake 画蛇
            if self.points:
                for i, point in enumerate(self.points):
                     if i != 0:
                        self.points[i-1] = tuple(self.points[i-1])  # 转换数据格式22
                        self.points[i] = tuple(self.points[i])  # 转换数据格式22
                        cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                # 对列表最后一个点也就是蛇头画为紫色点

                self.points[-1] = tuple(self.points[-1])  # 转换数据格式22
                cv2.circle(imgMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            # Draw Food 画食物
            # rx, ry = self.foodPoint
            imgMain = cvzone.overlayPNG(imgMain, self.imgFood,(rx - self.wFood // 2, ry - self.hFood // 2))

            cvzone.putTextRect(imgMain, f'Your Score:{self.score}', [50, 80],scale=3, thickness=5, offset=10)

            # Check for Collision 检查是否缠绕
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))  # 重塑为一个行数未知但只有一列且每个元素有2个子元素的矩阵
            cv2.polylines(imgMain, [pts], False, (0, 200, 0), 3)
            # 第三个参数是False，我们得到的是不闭合的线
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            print(minDist)
            # 参数True表示输出该像素点到轮廓最近距离

            if -1 <= minDist <= 1:
                print("Hit")
                self.gameOver = True
                self.points = []  # 蛇身上所有的点
                self.lengths = []  # 每个点之间的长度
                self.currentLength = 0  # 蛇的总长
                self.allowedLength = 150  # 蛇允许的总长度
                self.previousHead = 0, 0  # 第二个头结点
                self.randomFoodLocation()


        return imgMain

game = SnakeGameClass("donut.png")


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # 将手水平翻转
    hands, img = detector.findHands(img, flipType=False)  # 左手是左手，右手是右手，映射正确

    if hands:
        lmList = hands[0]['lmList']     # hands是由N个字典组成的列表
        pointIndex = lmList[8][0:2]     # 只要食指指尖的x和y坐标
        pointIndex = tuple(pointIndex)  #转换数据格式22
        # print(type(img))
        # cv2.circle(img, pointIndex, 20, (200, 0, 200), cv2.FILLED)
        img = game.update(img,pointIndex)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver = False