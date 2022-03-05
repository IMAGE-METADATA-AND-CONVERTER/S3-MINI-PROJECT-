from django.shortcuts import render
from exif import Image as Image1
from pathlib import Path
import os
# Create your views here.
from django.core.files.storage import FileSystemStorage
from PIL import Image

def index(request):
    return render(request,"index.html",{"i":"0"})

def getmetadata(request):
    data={"file":""}
    if request.POST:
        for f in os.listdir("media/"):
            os.remove(os.path.join("media/", f))
        t8=request.FILES["f1"]
        fs = FileSystemStorage()
        fs.save(t8.name, t8)
         
        img_filename = 'media/'+str(t8.name)
        img_path = os.path.abspath(img_filename )
        with open(img_path, 'rb') as img_file:
            img = Image1(img_file)
        data={"file":str(t8.name),"Make":img.get("Make"),"artist":img.get("artist"),
        "exif_ifd_pointer":img.get("_exif_ifd_pointer"),
        "color_space":img.get("color_space"),
        "compression":img.get("compression"),
        "datetime":img.get("datetime"),
        "jpeg_interchange_format":img.get("jpeg_interchange_format"),
        "jpeg_interchange_format_length":img.get("jpeg_interchange_format_length"),
        "orientation":img.get("orientation"),
        "pixel_x_dimension":img.get("pixel_x_dimension"),
        "pixel_y_dimension":img.get("pixel_y_dimension"),
        "resolution_unit":img.get("resolution_unit"),
        "software":img.get("software"),
        "x_resolution":img.get("x_resolution"),
        "y_resolution":img.get("y_resolution")
        }
        print(img.has_exif)
        print(sorted(img.list_all()))
        
        print(data)
        
    return render(request,"meta.html",{"data":data,"i":"1"})

def convert(request):
    filename=""
    src=""
    ext=""
    if request.POST:
        for f in os.listdir("media/"):
            os.remove(os.path.join("media/", f))
        t8=request.FILES["f1"]
        fs = FileSystemStorage()
        fs.save("up_"+t8.name, t8)
        img_filename = 'media/up_'+str(t8.name)
        dpath= os.path.abspath('media/')
        img_path = os.path.abspath(img_filename )
        res = t8.name.split(".")
        im1 = Image.open(img_path)
        st=int(request.POST["f2"])
        src="up_"+t8.name
        if st == 1:
            ext="png"
        else:
            ext="webp"
        im1.save(dpath+"/"+ext+"_conveted_"+res[0]+"."+ext)
        filename=ext+"_conveted_"+res[0]+"."+ext
        
    return render(request,"convert.html",{"i":"2","filename":filename,"orgin":src,"covert":ext})
