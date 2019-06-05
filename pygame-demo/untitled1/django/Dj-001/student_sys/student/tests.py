from django.test import TestCase,Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name = "thebalck-",
            sex = 1,
            email = "912182005@qq.com",
            profession = "程序员",
            qq = "123456789",
            phone = "12345678989",
        )
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name="thebalck-1024",
            sex=1,
            email="963852741@qq.com",
            profession="程序员",
            qq="123456789",
            phone="12345678989",
        )
        self.assertEqual(student.sex_show,"男","性别字段内容和展示不一致！")

    def test_filer(self):
        Student.objects.create(
            name="thebalck-1024",
            sex=1,
            email="963852741@qq.com",
            profession="程序员",
            qq="123456789",
            phone="12345678989",
        )
        name = "theblack-"
        students = Student.object.filter(name=name)
        self.assertEqual(students.count(),1,
                         "应该只存在一个名称为{}的记录".format(name))

    def test_index(self):
        #测试首页的可用性
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code,200,"status code must be 200!")

    def test_post_student(self):
        client = Client()
        data = dict(
            name="test_for_post",
            sex=1,
            email="789456123@qq.com",
            profession="程序员",
            qq="78945613",
            phone="74185296396",
        )
        response = client.post("/",data)
        self.assertTrue(b"test_for_post" in response.content,
                        "response content must contain 'test_for_post'")