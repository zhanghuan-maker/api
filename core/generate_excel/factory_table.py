# from xlwt import *
import uuid

# # 需要xlwt库的支持
# # import xlwt
# file = Workbook(encoding='utf-8')
# # 指定file以utf-8的格式打开
# table = file.add_sheet('data')
# # 指定打开的文件名
#
#
#
#
# table.write(0,0,'ID')
# table.write(0,1,'JSON_CONTENT')
# number=0
# for i in range(1,5):
#     for j in range(2):
#         ID=str(uuid.uuid1())
#         Name='测试工厂'+str(number)
#         JSON_CONTENT='{"id": "'+ID+'", "name": "'+Name+'", "image": null, "domain": "", "address": {"title": "", "address": "", "latitude": 31.196955, "longitude": 121.339752}, "comment": null, "disable": false, "createdBy": "SYSTEM", "updatedBy": "SYSTEM", "disableMsg": "", "taxPayerId": null, "createdDate": 1633795200000, "updatedDate": 1633795200000, "distributorId": 201, "factoryAccount": {"password": "123456", "updatedDate": 1633795200000, "loginUserName": "shell"}, "totalOilVolume": 1000, "factoryContacts": [{"name": "Shell", "phoneNumber": "13699999999"}], "latestOperation": "CREATED", "yingkeFactoryId": null, "yingkeFactoryNo": null, "mainEquipmentType": "", "yingkeFactoryName": null, "defaultRoleForNewUser": "ADMIN", "businessRegistrationName": null}'
#         if j==0:
#             table.write(i,j,ID)
#         else:
#             number = number + 1
#             table.write(i, j, JSON_CONTENT)
#
# file.save('factory.xlsx')


# str='''INSERT INTO `factory` (`ID`, `JSON_CONTENT`) VALUES ('2e67f8e0-1c4a-11ec-8062-acde48001122', '{\"id\": \"2e67f9da-1c4a-11ec-8062-acde48001122\", \"name\": \"测试工厂1\", \"image\": null, \"domain\": \"\", \"address\": {\"title\": \"\", \"address\": \"\", \"latitude\": 31.196955, \"longitude\": 121.339752}, \"comment\": null, \"disable\": false, \"createdBy\": \"SYSTEM\", \"updatedBy\": \"SYSTEM\", \"disableMsg\": \"\", \"taxPayerId\": null, \"createdDate\": 1633795200000, \"updatedDate\": 1633795200000, \"distributorId\": 201, \"factoryAccount\": {\"password\": \"123456\", \"updatedDate\": 1633795200000, \"loginUserName\": \"shell\"}, \"totalOilVolume\": 1000, \"factoryContacts\": [{\"name\": \"Shell\", \"phoneNumber\": \"13699999999\"}], \"latestOperation\": \"CREATED\", \"yingkeFactoryId\": null, \"yingkeFactoryNo\": null, \"mainEquipmentType\": \"\", \"yingkeFactoryName\": null, \"defaultRoleForNewUser\": \"ADMIN\", \"businessRegistrationName\": null}'), ('2e67f3fe-1c4a-11ec-8062-acde48001122', '{\"id\": \"2e67f7be-1c4a-11ec-8062-acde48001122\", \"name\": \"测试工厂0\", \"image\": null, \"domain\": \"\", \"address\": {\"title\": \"\", \"address\": \"\", \"latitude\": 31.196955, \"longitude\": 121.339752}, \"comment\": null, \"disable\": false, \"createdBy\": \"SYSTEM\", \"updatedBy\": \"SYSTEM\", \"disableMsg\": \"\", \"taxPayerId\": null, \"createdDate\": 1633795200000, \"updatedDate\": 1633795200000, \"distributorId\": 201, \"factoryAccount\": {\"password\": \"123456\", \"updatedDate\": 1633795200000, \"loginUserName\": \"shell\"}, \"totalOilVolume\": 1000, \"factoryContacts\": [{\"name\": \"Shell\", \"phoneNumber\": \"13699999999\"}], \"latestOperation\": \"CREATED\", \"yingkeFactoryId\": null, \"yingkeFactoryNo\": null, \"mainEquipmentType\": \"\", \"yingkeFactoryName\": null, \"defaultRoleForNewUser\": \"ADMIN\", \"businessRegistrationName\": null}')'''
# str1='''INSERT INTO `factory` (`ID`, `JSON_CONTENT`) VALUES '''
# for i in range(100):
# str2=str(uuid.uuid1())
# str3="(\'" + str2 + '''\', '{\"id\": \"'''