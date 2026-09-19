import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
inputdata = input("Put Your Data In Here:")
svg_img = qrcode.make (inputdata, image_factory=factory)

svg_name = input("What Will You Name You File:")
svg_img.save(".svg" + svg_name)

