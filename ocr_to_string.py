#pip install pillow
#파이썬에서 이미지 처리 (OpenCV는 영상처리)
#http://pythonstudy.xyz/python/article/406-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B2%98%EB%A6%AC-Pillow
from PIL import Image

#pip install pytesseract
from pytesseract import *

#프로그램을 실행시킬 때마다 설정을 다르게 해주고 싶을 때 사용
import configparser

#운영 체제 인터페이스
import os



#config parser초기화
config=configparser.ConfigParser()
#config file읽기, 파일이 위치한 디렉토리
config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')



#이미지 -> 문자열 추출
def imgTostr(fullPath, outTxtPath, fileName, lang='eng'): #디폴트는 영어로 추출
    #이미지 경로
    img=Image.open(fullPath)
    #경로를 병합하여 새 경로 생성
    txtName=os.path.join(outTxtPath,fileName.split('.')[0])

    #추출(이미지파일, 추출언어, 옵션)
    #preserve_interword_spaces : 단어 간격 옵션을 조절하면서 추출 정확도를 확인
    #psm(페이지 세그먼트 모드: 이미지 영역안에서 텍스트 추출범위모드)

    outText=image_to_string(img,lang=lang,config='--psm 1 -c preserve_interword_spaces=1')

    print('[OCR Result]')
    print('FileName: ',fileName)
    print('\n\n')

    #출력
    print(outText)

    #추출 문자 텍스트 파일 쓰기
    strTotxt(txtName, outText)



#문자열 -> 텍스트파일 개별 저장
def strTotxt(txtName, outText):
    with open(txtName + '.txt','w',encoding='utf-8') as f:
        f.write(outText)



#메인 시작
if __name__ == "__name__":
    #텍스트 파일 저장 경로
    outTxtPath=os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath']

    #OCR 추출 작업 메인
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath']):
        for fname in files:
            fullName=os.path.join(root, fname)
            #한글+영어 추출(kor, eng, kor+eng)
            imgTostr(fullName,outTxtPath,fname,'kor+eng')
            
