# -*- coding: utf-8 -*-  
import cv2  
import numpy as np  
from find_obj import filter_matches,explore_match  
from matplotlib import pyplot as plt  
  
def getSift():  
    ''''' 
    �õ����鿴sift���� 
    '''  
    img_path1 = '../../data/home.jpg'  
    #��ȡͼ��  
    img = cv2.imread(img_path1)  
    #ת��Ϊ�Ҷ�ͼ  
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    #����sift����  
    sift = cv2.SIFT()  
    #��ͼ�����ҵ��ؼ��� Ҳ����һ������#kp, des = sift.detectAndCompute  
    kp = sift.detect(gray,None)  
    print type(kp),type(kp[0])  
    #Keypoint�������ͷ��� http://www.cnblogs.com/cj695/p/4041399.html  
    print kp[0].pt  
    #����ÿ�����sift  
    des = sift.compute(gray,kp)  
    print type(kp),type(des)  
    #des[0]Ϊ�ؼ����list��des[1]Ϊ���������ľ���  
    print type(des[0]), type(des[1])  
    print des[0],des[1]  
    #���Կ�������885��sift������ÿ������Ϊ128ά  
    print des[1].shape  
    #�ڻҶ�ͼ�л�����Щ��  
    img=cv2.drawKeypoints(gray,kp)  
    #cv2.imwrite('sift_keypoints.jpg',img)  
    plt.imshow(img),plt.show()  
  
def matchSift():  
    ''''' 
    ƥ��sift���� 
    '''  
    img1 = cv2.imread('../../data/box.png', 0)  # queryImage  
    img2 = cv2.imread('../../data/box_in_scene.png', 0)  # trainImage  
    sift = cv2.SIFT()  
    kp1, des1 = sift.detectAndCompute(img1, None)  
    kp2, des2 = sift.detectAndCompute(img2, None)  
    # ����ƥ���㷨,�������������������(L2(default),L1)���Ƿ񽻲�ƥ��(Ĭ��false)  
    bf = cv2.BFMatcher()  
    #����k�����ƥ��  
    matches = bf.knnMatch(des1, des2, k=2)  
    # cv2.drawMatchesKnn expects list of lists as matches.  
    #opencv2.4.13û��drawMatchesKnn��������Ҫ��opencv2.4.13\sources\samples\python2�µ�common.py��find_obj�ļ����뵱ǰĿ¼��������  
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)  
    explore_match('find_obj', img1, img2, kp_pairs)  # cv2 shows image  
    cv2.waitKey()  
    cv2.destroyAllWindows()  
  
def matchSift3():  
    ''''' 
    ƥ��sift���� 
    '''  
    img1 = cv2.imread('../../data/box.png', 0)  # queryImage  
    img2 = cv2.imread('../../data/box_in_scene.png', 0)  # trainImage  
    sift = cv2.SIFT()  
    kp1, des1 = sift.detectAndCompute(img1, None)  
    kp2, des2 = sift.detectAndCompute(img2, None)  
    # ����ƥ���㷨,�������������������(L2(default),L1)���Ƿ񽻲�ƥ��(Ĭ��false)  
    bf = cv2.BFMatcher()  
    #����k�����ƥ��  
    matches = bf.knnMatch(des1, des2, k=2)  
    # cv2.drawMatchesKnn expects list of lists as matches.  
    #opencv3.0��drawMatchesKnn����  
    # Apply ratio test  
    # ��ֵ���ԣ����Ȼ�ȡ��A ��������ĵ�B���������C���ν�����ֻ�е�B/C  
    # С����ֵʱ��0.75���ű���Ϊ��ƥ�䣬��Ϊ����ƥ����һһ��Ӧ�ģ�������ƥ����������Ϊ0  
    good = []  
    for m, n in matches:  
        if m.distance < 0.75 * n.distance:  
            good.append([m])  
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], None, flags=2)  
    cv2.drawm  
    plt.imshow(img3), plt.show()  
  
matchSift()  