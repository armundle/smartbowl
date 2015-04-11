import requests

def BoomerIsFed():
	return requests.post("http://ec2-54-149-172-249.us-west-2.compute.amazonaws.com:3002/send")


if __name__=='__main__':
	print BoomerIsFed()
