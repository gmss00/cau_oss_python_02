import math #math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기
class Line:
    def __init__(self, length=1):
        if type(length)!=int and type(length)!=float:
            length=1
        elif length<=0:
            length=1
        self.__length = length

    def set_length(self, length):
        if type(length)== (int or float) and length>0:
            self.__length=length

    def get_length(self):
        return self.__length
def area_square(line):
    #docstring의 작성방법은 다음과 같습니다
    """함수에 대한 간략한 설명을 작성합니다.
    Args:매개변수를 나열합니다
       매개변수이름1(타입):매개변수에 대한 설명
    매개변수이름2(타입):매개변수에 대한 설명
    Returns:
        반환타입:반환값에 대한 설명"""
    return line.get_length()**2
def area_circle(line):
    #예시
    """길이를 입력받아 원의 넓이를 구하는 함수입니다.
    Args:
        line(Line):반지름의 길이입니다
    Returns:
        int or float:원의 넓이를 반환합니다."""
    return line.get_length() ** 2 * math.pi
def area_regular_triangle(line):
    return line.get_length()**2*math.sqrt(3)/4
