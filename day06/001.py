# 현재 디렉토리 확인
import os
import sys

# 현재 작업디렉토리 확인
print(os.getcwd())

# python 파일의 위치 확인
print(f'파일위치 확인 : {os.path.abspath(__file__)}')
print(f'__file__ : {__file__}')
