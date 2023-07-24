#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
# olusturdugumuz servisi import ediyoruz
from custom_service_interface.srv import MySrv


class MyServer(Node):
    def __init__(self):
        super().__init__("my_server")
        self.server = self.create_service(MySrv,"maas_hesapla",self.callback)

    def callback(self,request,response):
        # ana servis yapisini olusturdugumuz bolum
        # gelen istekler ile bir yanit donduruyoruz
        if request.meslek == "doktor" and request.tecrube > 3.5:
            response.maas = 15000
        elif request.meslek == "muhendis" and request.tecrube < 3.5:
            response.maas = 9000
        else:
            response.maas = 0   
        return response
    
# temel olarak bir dugum olusturuyoruz     
def main(args = None):
    rclpy.init(args=args)
    node = MyServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()