from PIL import Image
from os import listdir


def picPostfix():  # ����׺�ļ���
    postFix = set()
    postFix.update(['bmp', 'jpg', 'png', 'tiff', 'gif', 'pcx', 'tga', 'exif',
                    'fpx', 'svg', 'psd', 'cdr', 'pcd', 'dxf', 'ufo', 'eps', 'JPG', 'raw', 'jpeg'])
    return postFix


def getDiff(width, high, image):  # ��Ҫ�ü���w*h��image��Ƭ 
    diff = []
    im = image.resize((width, high))
    imgray = im.convert('L')  # ת��Ϊ�Ҷ�ͼƬ ���ڴ���
    pixels = list(imgray.getdata())  # �õ��������� �Ҷ�0-255

    for row in range(high): # ��һ������ߵ����ص���бȽ�
        rowStart = row * width  # ��ʼλ���к�
        for index in range(width - 1):
            leftIndex = rowStart + index  
            rightIndex = leftIndex + 1  # ����λ�ú�
            diff.append(pixels[leftIndex] > pixels[rightIndex])

    return diff  #  *�õ�����ֵ���� �������ת��Ϊhash��*


def getHamming(diff=[], diff2=[]):  # ������������人������
    hamming_distance = 0
    for i in range(len(diff)):
        if diff[i] != diff2[i]:
            hamming_distance += 1

    return hamming_distance


if __name__ == '__main__':

    width = 32
    high = 32  # ѹ����Ĵ�С
    dirName = ""  # ���·��
    allDiff = []
    postFix = picPostfix()  #  ͼƬ��׺�ļ���

    dirList = listdir(dirName)
    cnt = 0
    for i in dirList:
        cnt += 1
        print cnt  # ���Բ���ӡ ��ʾ������ļ�����
        if str(i).split('.')[-1] in postFix:  # �жϺ�׺�ǲ�����Ƭ��ʽ
            im = Image.open(r'%s\%s' % (dirName, unicode(str(i), "utf-8")))
            diff = getDiff(width, high, im)
            allDiff.append((str(i), diff))

    for i in range(len(allDiff)):
        for j in range(i + 1, len(allDiff)):
            if i != j:
                ans = getHamming(allDiff[i][1], allDiff[j][1])
                if ans <= 5:  # �б�ĺ������룬�Լ�����ʵ���������
                    print allDiff[i][0], "and", allDiff[j][0], "maybe same photo..."