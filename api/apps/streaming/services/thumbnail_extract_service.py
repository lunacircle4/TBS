import cv2

class ThumbnailExtractService:
    def __init__(self, url):
        self.url = url
    
    def call(self):
        # ffmpeg에서 사진을 추출한후
        # 사진을 임시로 저장하고
        # 사진에 대한 포인터를 반환한다.

        vcap = cv2.VideoCapture(self.url)
        res, im_ar = vcap.read()
        im_ar = cv2.resize(im_ar, (200, 200), 0, 0, cv2.INTER_LINEAR)
        
        #to save we have two options
        #1) save on a file
        #cv2.imwrite(save_on_filename, im_ar)

        #2)save on a buffer for direct transmission
        res, thumb_buf = cv2.imencode('.png', im_ar)

        # '.jpeg' etc are permitted
        #get the bytes content
        return thumb_buf.tostring()