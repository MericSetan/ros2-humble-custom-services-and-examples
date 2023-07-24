#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
# olusturdugumuz servisi import ediyoruz
from custom_service_interface.srv import MySrv

class MyClient(Node):
    def __init__(self):
        super().__init__("my_client")
        #client olusutur
        self.client = self.create_client(MySrv,"maas_hesapla")
        # servisi cagir ve yanit bekle
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("tekrar deneniyor")
               

    def send_request(self,meslek,tecrube):
        # istekleri esitle
        request = MySrv.Request()
        request.meslek= meslek
        request.tecrube = tecrube 
        # geri donus nesnesi ve fonksiyonu olustur
        future  =self.client.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self,future):
        # yanıtı al
        response = future.result()
        self.get_logger().info(f"maas: {response.maas}")

# temel olarak bir dugum olusturuyoruz       
def main(args = None):
    rclpy.init(args=args)
    node = MyClient()
    node.send_request("doktor",8.2)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()