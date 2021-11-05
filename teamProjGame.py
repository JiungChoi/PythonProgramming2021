class floatElement: # 부유물 클래스: 점수 클래스(plus)와, 실점(minus) 클래스로 상속한다. 
    def __init__(self, x, y):
        self.x = x # x좌표
        self.y = y # y좌표

class plusElement(floatElement): # 점수 클래스(plus) : 부유물 객체로 부터 상속 받는다. 
    def __init__(self, imgPath, x, y):
        super().__init__(x, y)
        self.img = imgPath # img의 경로

class minusElement(floatElement): # 실점 클래스(plus) : 부유물 객체로 부터 상속 받는다.
    def __init__(self, imgPath, x, y):
        super().__init__(x, y)
        self.img = imgPath # img의 경로


class Game:
    def __init__(self):
        self.userName = input("Insert user info : ")
        self.floatElemets = [[], []] # 0 : plusElement, 1 : minusElement
        self.gameWindowInfo = [640, 480] # 0 : boardWidth, 1 : boardHeight ... default [width : 640, hegiht : 480]

    def windowSet(self, width, height):
        self.gameWindowInfo[0] = width
        self.gameWindowInfo[1] = height

    def userSet(self, name):
        self.userName = name


    def run(self):
        print(f" hi {self.userName}! \nif you want to quit this game press \"q\"! ")
        self.floatElemets[0].append(plusElement("path1", 50, 60))
        self.floatElemets[0].append(plusElement("path2", 5, 6))
        self.floatElemets[0].append(minusElement("path3", 60, 70))
        

'''#       
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            img = frame.copy()
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = dector(gray_img, 1)

            for face in faces:
                shapes = predictor(gray_img, face)
                shapes = face_utils.shape_to_np(shapes)

                for point in shapes:
                    cv2.cicle(img, point, 2, (255, 255, 0))

            cv2.imshow("result", img)
            if cv2.waitkey(1) == ord("q"):
                break

#'''


if __name__ == "__main__":
    # generte the game
    print("Welcome to our game !!")
    game = Game()
    while(True):
        gameMenu = int(input("1. Start game 2. Settings 3. exit : "))

        if (gameMenu == 1): game.run()
        elif (gameMenu == 2):
            editSetting = int(input("1. Display 2.User ... : "))
            if(editSetting == 1):
                while(True):
                    try:
                        width, height = map(int, input("Insert .. [width height] : ").split())
                        break
                    except ValueError:
                        print("Insert right Value")

                game.windowSet(width, height)
            elif(editSetting == 2): game.userSet()
            else: print("Wrong function")
        elif(gameMenu == 3):
            print("exit")
            break
        else: print("Wrong function")
