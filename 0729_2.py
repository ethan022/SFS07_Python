class Info:
    def __init__(self, breed):
        self._breed = breed


class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
        return f"동물 소리를 냅니다."

    def move(self):
        return f"동물이 움직입니다."


class Dog(Animal, Info):
    def __init__(self, name, age, breed):
        # 슈퍼 클래스(부모 클래스) 생성자 호출
        Animal.__init__(self, name, age)
        Info.__init__(self, breed)
        # self.breed = breed

    # 메서드 오버라이딩
    def speak(self):
        return f"{self._name}: {self._breed} 멍멍!"
        # return super().speak()

    # 서브 클래스 고유 메서드
    def tail(self):
        return f"{self._name}이(가) 꼬리를 흔듭니다!"


print(f"=========== 상속 =============")
dog = Dog("멍멍이", 3, "진돗개")
print(dog.move())  # 부모 클래스
print(dog.speak())  # 오버라딩
print(dog.tail())  # 자식 클래스
