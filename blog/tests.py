from django.test import TestCase

# Create your tests here.
def like_upload(request):
	# 파일객체가 하나도 없다면 작업을 멈추고 리턴합니다.
	if request.FILES.__len__() == 0:
		message = "업로드할 파일이 없습니다."
		return JsonResponse({"message": message})


	uploadFile = request.FILES['file'];
	# csv파일이 아니라면 작업을 멈추고 리턴합니다.
	if uploadFile.name.find('csv') < 0 :
		message = "파일형식이 잘못되었습니다"
		return JsonResponse({"message": message})


	# 여기서 read()를 실행할 경우 타입이 byte로 읽힙니다.
	# 이것을 utf8로 디코드해서 문자열을 볼 수 있도록 바꿔둡니다. 
	read = uploadFile.read().decode('utf8')
	# 줄바꿈이 생기는 것을 기준으로 배열로 담아둡니다.
	readLine = read.split('\n')

	for line in readLine:
		print(line)