# variable scope
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# 함수내 변수 (local) 1 순위
# 함수내 함수에서 local 변수가 없으면 해당 함수를 포함하는 함수로 올라가서 변수를 찾는다. (Enclosed) - 2 순위
# 함수에 local이 없고 enclosed가 아니면 전역(Global)에서 변수를 찾는다. 3순위
# 전역 변수도 없으면 import 된 모듈에서 찾는다. Built-in
