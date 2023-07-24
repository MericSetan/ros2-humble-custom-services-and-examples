# ros2-humble-custom-services-and-examples








## create example package
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
## create a interface package

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


paketleri oluşturduktan sonra 
hata almadıysak eğer 
servisimizi oluşturmaya başlayalım

1) servis dosyasını oluşturalım
```
cd ros2_ws/src/custom_service_interface/srv
vim MySrv.srv
```
--- burada istekleri(request) ve yanıtları(response) oluşturuyoruz. isim olarak büyük harfle başlaması gerekmektedir
```
string meslek
float32 tecrube
---
int64 maas 
```
--- meslek  ve tecrübe bizim isteklerimizdir. maas ise bizim yanıtımız olacaktır. yapı olarak aslında mesaj gibidirler. aralarına üç adet - eklendirğinde (---) servis yapısında istenilen request ve response tanımlanmış olur.

2) package.xml dosyaına eklenecek olan 
   
```
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
CMakeLists.txt  dosyaına eklenecek olan : 
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
bu şekilde custom_service_interface paketimizin hazırlıklarını bitirmiş oluyoruz.
sırada custom_service_example paketimiz var. BU paket içerisinde python programlama dilini kullanarak interface paketinde oluşturduğumuz srv dosyasını kullanarak server ve client dosyalarını oluşturacağız.


1)

custom_service_examples paketi içerisinde bulunan 
package.xml dosyasına servis dosyasını oluşturduğumuz paketi ekliyoruz:
```
<depend>custom_service_interface</depend>
```

2) server ve client dosyalarının hazırlanması
bu iki dosyayı belirli dizinden inceleyerek yapısını anlayabilirsiniz.

ardından yapılacaklar

3)
custom_service_examples paketi içerisinde bulunan 
setup.py dosyasına  dosyasını oluşturduğumuz düğümleri ekliyoruz:
```
...
 entry_points={
        'console_scripts': [
            "my_server = custom_service_example.custom_service_server:main",
            "my_client = custom_service_example.custom_service_client:main"
        ],
...
```

1) tum islemler bittiğine göre çalışma alanımızı derleyebiliriz
   
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


![image](https://github.com/MericSetan/ros2-humble-custom-services-and-examples/assets/65041863/5d9572f3-1e12-46f2-ae48-cbcdaaff60a4)







