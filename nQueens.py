import random
import time

global queensNumber #برای مشخص کردن تعداد وزیر ها که به صورت عمومی تعریف شده است


#کلاس وزیر ها که در حقیقت یک حالت از مسئله ی ما به وجود می آورد
class Queens:


    #در این تابع سازنده مقادیر لیستی از مکان وزیر ها و هزینه(تعداد عدم برخورد) به ابجکت کویینز نسبت داده شده است
    def __init__(self , queens = [],cost = 0, childs = []):
        self.queens = queens
        self.cost = self.Cost()
        # self.childs = childs
        self.Mediator()


    #برای تبدیل مختصات وزیر ها به تصویری مانند صفحه شطرنج استفاده میشود
    def Board(self):
        queens = self.queens
        n = len(queens)
        board = [['*' for i in range(n)]for i in range(n)]
        for i in range(n):
            board[i][queens[i]] = 'Q'
        return board


    #کلاس بالایی را به نمایش میگذارد
    def Display(self):
        board = self.Board()
        for item in board:
            print(item)


    #برای محاسبه ی برخورد وزیر ها استفاده میشود
    def Cost(self):
        queens = self.queens
        n = len(queens)
        max = n*(n-1)/2#ماکسیموم تعداد برخورد ها
        cost = 0
        for i in range(n):
            for j in range(i + 1, n):
                cost += self.CheckInterSection(queens[i], queens[j], i, j)
        self.cost =int(max - cost)#تعداد برخورد ها - ماکسیموم مقدار بخورد ها = تعداد عدم برخورد


    #با این شرط ها بررسی میکند که آیا دو وزیر با هم برخورد عمودی یا اریب دارند یا خیر
    def CheckInterSection(self, a, b, i, j):
        if a == b:
            return 1
        elif abs(a - b) == abs(i - j):
            return 1
        return 0

    #برای تولید لیستی از فرزندان به کار میرود(برای بهینه تر شدن حذف شده)
    # def Childs(self):
    #     queens = self.queens
    #     n = len(queens)
    #     childs = []
    #     for i in range(n):
    #         for j in range(n):
    #             q = self.ChildGenerator(queens, i, j)
    #             if q != None:
    #                 childs.append(q)
    #     self.childs = childs


    # برای تولید لیستی از فرزندان به کار میرود(برای بهینه تر شدن حذف شده)
    # def ChildGenerator(self , queens, i, j):
    #     q = queens.copy()
    #     if j != queens[i]:
    #         q[i] = j
    #         return q


    #حالت رندوم اولیه ای را تولید میکند
    def SetQueens(self, n):
        self.queens = [random.randrange(0, n) for i in range(n)]


    #مقادیر مربوط به کوییز را ست میکند(برای جلوگیری از به وجود آمدن مشکل در حالات اولیه نوشته شده است)
    def Mediator(self):
        if self.queens==[]:
            self.SetQueens(queensNumber)
        self.Cost()
        # self.Childs()#برای بهینه شدن حذف شده است


    #تابع آزمون هدف بر اساس ماکسیمم شدن تعداد عدم برخورد ها
    def GoalCheck(self):
        n = len(self.queens)
        if self.cost == int((n*(n-1))/2): return True
        return False


    #برای بهینه شدن حذف شده است
    # def RandomChildSelect(self):
    #     childs = self.childs
    #     return random.choices(childs)[0]


    #به جای اینکه بیاییم و برای هر ابجکت وزیر یک لیست طولانی از فرزندانش را بسازیم ، فقط در زمان نیاز به سراغ این تابع می اییم تا برایمان یک فرزند رندوم تولید کند
    def RandomChildMake(self):
        queens = self.queens.copy()
        n = len(queens)
        l = [i for i in range(n)]
        choice = random.choice(l)
        l.pop(queens[choice])
        queens[choice] = random.choice(l)
        return queens


#شبیه سازی حرارت
def SimulatedAnnealing(queens):
    current = queens
    t = 1
    fitnessCounter = 0
    while True:
        Temp = int(1000000/(t))#تابع تعیین حرارت بر اساس زمان و کاهش ان به مرور
        # if Temp == 0: print(f"fittnes:{fitnessCounter}"); return current#برای دیدن حالت پایانی در صورت به پاسخ کامل نرسیدن
        if Temp == 0:
            print(f"temp reached 0 and the current queens number that are in right place is '{current.cost}'")
            current.Display()
            return fitnessCounter#شرط خروج در صورت کم شدن حرارت
        next = Queens(current.RandomChildMake())#تولید یک حالت بعدی تصادفی
        comparingValue = next.cost - current.cost#مقایسه ی هزینه ها
        if comparingValue >= 0 :current = next# اگر حالت جدید بهتر بود حالت فعلی را برابر حالت جدید میگذارد
        else:#اگر حالت فعلی بهتر بود با احتمالی مرتبط با حرارت میتواند به حالت جدید هم  برود
            populationList = [next,current]
            next_weight = (2.71)**(comparingValue/Temp)
            choice= random.choices(populationList,weights=[next_weight, 1-next_weight])
            current = choice[0]
        if current.GoalCheck():#تابع آزمون هدف
            print("goal reached")
            current.Display()
            return fitnessCounter
        fitnessCounter+=1
        t+=1


""".............simulated annealing.................."""

print("Enter n_queens: ")
queensNumber = int(input())
i=5
avg = 0


while i >0 :
    q = Queens()
    f = (SimulatedAnnealing(q))
    print(f"fitness: {f}")
    if f != 0:
        avg +=f
    i -=1


print(f"avg: {avg/20}")
input()
