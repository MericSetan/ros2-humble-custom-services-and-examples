# ROS2 Creating Custom Service

## Python bağımlıklı paket oluşturma
1)
```
cd ~/ros2_ws/src
```
2)
```
ros2 pkg create custom_service_examples --build-type ament_python --dependencies rclpy example_interfaces
```
3)
```
cd ..
colcon build --packages-select custom_service_examples 
```
## Interface paketini oluştur

1)
```
cd ~/ros2_ws/src
```
2)
```
ros2 pkg create custom_service_interface
cd custom_service_interface/
mkdir srv
rm -rf include/
rm -rf src/
```
3)
```
cd ../..
colcon build --packages-select custom_service_interface
```


Paketleri olusturduktan ve derledikten sonra hata almadıysak eğer sonraki adıma geçip servis dosyasını oluşturmaya başlayabiliriz.

## Servisin oluşturulması

1) 
```
cd ros2_ws/src/custom_service_interface/srv
vim MySrv.srv
```
<--- Burada istekleri(request) ve yanıtları(response) oluşturuyoruz. !İsim olarak büyük harfle başlaması gerekmektedir. --->
```
string meslek
float32 tecrube
---
int64 maas 
```
--- *meslek*  ve *tecrübe* bizim istek mesajımız olacaktır. Devamında *maas* ise bizim yanıt mesajımız olacaktır. Yapı olarak bakıldığında mesajlara çok benzemektedir. Bu iki mesajın arasına üç adet - eklendiğinde (---) servis yapısında istenilen request ve response mesajları tanımlanmış olur. Bu işlem bittikten sonra yapmamız gereken değişiklikler var:

2) ***package.xml*** dosyasına eklenecek olan: 
   
```
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
***CMakeLists.txt***  dosyasına eklenecek olan : 
```
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/MySrv.srv"
)
ament_export_dependencies(rosidl_default_runtime)
```

3) 
```
cd ~/ros2_ws
colcon build --packages-select custom_service_interface
```
Bu şekilde custom_service_interface paketimizin hazırlıklarını bitirmiş oluyoruz.
Sırada *custom_service_example* paketimiz var. Bu paket içerisinde Python programlama dilini kullanarak *custom_service_interface* paketinde oluşturduğumuz *srv* dosyasını kullanarak server ve client dosyalarını oluşturacağız.

## Client Ve Server dosyalarının oluşturulması
1)

*custom_service_examples* paketi içerisinde bulunan ***package.xml*** dosyasına servis dosyasını oluşturduğumuz paketi ekliyoruz:
```
<depend>custom_service_interface</depend>
```

2) Server ve Client dosyalarının hazırlanması...
   *ros2_ws/src/custom_service_examples/custom_service_examples*
Bu iki dosyayı belirli dizinden inceleyerek yapısını anlayabilirsiniz.

Ardından yapılacaklar

3)
*custom_service_examples* paketi içerisinde bulunan ***setup.py*** dosyasına  dosyasına oluşturduğumuz düğümleri ekliyoruz:
```
...
 entry_points={
        'console_scripts': [
            "my_server = custom_service_example.custom_service_server:main",
            "my_client = custom_service_example.custom_service_client:main"
        ],
...
```
## Sonuç
1) Tüm işlemler bittiğine göre çalışma alanımızı derleyebiliriz.
   
```
cd ~/ros2_ws
colcon build --packages-select custom_service_examples --symlink-install
cd
source .bashrc
```
2)
1. terminalede
```
ros2 run custom_service_examples my_server 
```
2. terminalede
```
ros2 run custom_service_examples my_client
```

![image](https://github.com/MericSetan/ros2-humble-custom-services-and-examples/assets/65041863/7073f728-c258-42d3-a6b9-83d24ee1eed4)









