from flask import Flask,flash, request, redirect, url_for
from flask import request
from face import fileoperation
from face import faceoperation
import os
app = Flask(__name__)

db="E:/python_workspace/face_deepface1/dataset551"   
dataset="dataset"
@app.route("/faceapi/record/validation", methods=['PUT'])
def record_validation():
     devicename = request.args.get('devicename')
     devicedb=os.getcwd()
     devicedb=f"{devicedb}/{dataset}/{devicename}/"
    #    if not os.path.exists(final_directory):
     print("devicedb=",devicedb)
     print("devicename1=",os.path.exists(devicedb))
     id=""
     status="failed"
     
     if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
     elif os.path.exists(devicedb)==False:
           status="failed:device not available"
     else:
        status,filename=fileoperation.dosave(request)
    
        print(f"{filename}==temp file save status:",status)

        status, id=faceoperation.finderoneface(devicename,filename)
        print("id=",id)
        print("status=",status)
        if os.path.exists(filename): os.remove(filename)
     reponse = {
            "id": id,
             "status": status
                }

     

     return reponse
@app.route("/faceapi/record/create", methods=['PUT'])
def record_create():
    devicename = request.args.get('devicename')
    recordname = request.args.get('recordname')
    # devicename = request.args.get('devicename')
    print("devicename1=",os.path.exists(devicename))
    id=""
    status="failed"
    filename=""
    orgfilename=""

     
    if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
    elif recordname=="" or recordname==" " or recordname==None:
          status="failed:kindly provide the recordname in param"
    else:         
        status,filetemppath,orgfilename=fileoperation.dosavetemp(request)


        print("status=",status)
        print("filename=",filetemppath)
        print("orgfilename=",orgfilename)
        status, id= faceoperation.recordcreate(devicename,recordname,filetemppath,orgfilename)
    reponse = {
            "id": id,
             "status": status
                }
    return reponse
@app.route("/faceapi/record/delete", methods=['DELETE'])
def record_delete():
    devicename = request.args.get('devicename')
    recordname = request.args.get('recordname')
    # devicename = request.args.get('devicename')
    print("devicename1=",os.path.exists(devicename))
    id=""
    status="failed"
    filename=""
    orgfilename=""

     
    if devicename=="" or devicename==" " or devicename==None:
          status="failed:kindly provide the devicename in param"
    elif recordname=="" or recordname==" " or recordname==None:
          status="failed:kindly provide the recordname in param"
    else:         
          status, id= faceoperation.recorddelete(devicename,recordname)

     
    reponse = {
            "id": id,
             "status": status
                }
    return reponse


if __name__ == '__main__':
    devicename="common"
    # run() method of Flask class runs the application 
    # on the local development server.
    # app.run()
    imgpath="E:/python_workspace/college_face_automation1/college_face_automation/temp/1.jpg"
    # db="E:/python_workspace/face_deepface1/dataset551"

    status, name=faceoperation.finderoneface(devicename,imgpath)
    print("name=",name)
    print("status=",status)
    # # finder = service.find(img1_path=imgpath, db=db, model_name="VGG-Face",
    #                       detector_backend="opencv",distance_metric="cosine",
    #                       align=True,enforce_detection=True,anti_spoofing=False)


 
    # print("finder len=",len(finder))
    
    # print("finder =",finder[0])
    # afinder=numpy.asarray(finder[0])
    # print("afinder12=",str(afinder[0]))
    # out_arr = numpy.char.split(str(afinder[0])," ") 
    # print("out_arr=",out_arr)
    # final=str(out_arr.item(0)).split(", """)
    # print("out_arr1=",final[0])
    # print("out_arr1=",final)
    # array1=str(afinder[0])
    # array2=array1.split(" ")
    # print("ss=",array2[0])
    # basefilename = Path(array2[0]).stem
    # print("basefilename=",basefilename)

# createdir(temp)