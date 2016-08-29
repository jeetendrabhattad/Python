from xml.dom import minidom
 
doc = minidom.parse("employee.xml")
print type(doc)
print doc
# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")
print type(name)
print name[0]
print name[0].firstChild
print(name[0].firstChild.data)
print(name[1].firstChild.data)
employees = doc.getElementsByTagName("emp")
for emp in employees:
        sid = emp.getAttribute("id")
        nickname = emp.getElementsByTagName("nickname")[0]
        salary = emp.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))
