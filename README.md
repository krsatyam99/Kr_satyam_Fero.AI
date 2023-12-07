# Problem Statement
#### An e-commerce API using Django Rest Framework to manage customers, orders, and products.The system should be able to handle multiple customers, each having multiple orders, and each order containing multiple products with corresponding quantities.

## Set up Project Steps:
1.clone the project using git clone https://github.com/krsatyam99/Kr_satyam_Fero.AI.git \
2. pip install -r requirements.txt\
3.python manage.py makemigrations\
4. python manage.py migrate.\
5.Python mnanage.py createsuperuser\
6.Python manage.py runserver
#### Project Structure [**Note: All The business Logics and validations are Written In serializers.py File ]
![Screenshot (27)](https://github.com/krsatyam99/Kr_satyam_Fero.AI/assets/103446420/9d0b34a9-8248-4ddc-83d3-83cfb6612e62)

## PostMan collection 
Link https://api.postman.com/collections/24162967-ec370446-852c-4482-bd72-d1a18456de69?access_key=PMAT-01HH1YSSKVTDMW4MGDPCTYVS6F
## Important Api end points
###### api/ products/ [name='product-create']
###### api/ detail_products/<int:pk>/ [name='product-detail']
###### api/ list_products/ [name='product-list']
###### api/ customers/ [name='customer-list']
###### api/ customers/create/ [name='customer-create']
###### api/ customers/<int:pk>/ [name='customer-update']
###### api/ orders/ [name='order-list-create']
###### api/ allorders/ [name='order-list']
###### api/ name_wise_orders/ [name='order-list-name']
###### api/ product_wise_orders/ [name='order-list-product']
###### api/ updateorder/<int:pk>/ [name='update-order']


### Business Diagram
![Fero Ai](https://github.com/krsatyam99/Kr_satyam_Fero.AI/assets/103446420/591aa6dc-717d-4912-9136-dd2ef46c3201)


### Admin Panel
![Fero Api](https://github.com/krsatyam99/Kr_satyam_Fero.AI/assets/103446420/a02d4eb6-f854-41ad-92de-f72fee27a8b5)



## Genericviews and types used in the project
In Django REST Framework (DRF), generic views are a set of pre-built class-based views that provide common patterns for performing CRUD (Create, Retrieve, Update, Delete) operations on models. These generic views help in reducing code duplication and boilerplate by providing a standardized way to handle common actions.
### generics.CreateAPIView
In Django REST Framework (DRF), generics.CreateAPIView is a class-based view that provides a generic implementation for creating a new object.
Purpose: Used for handling HTTP POST requests to create a new object.
Inheritance: Inherits from generics.GenericAPIView and mixins.CreateModelMixin.
### generics.RetrieveAPIView
In Django REST Framework (DRF), generics.RetrieveAPIView is a class-based view that provides a generic implementation for retrieving a single object.
Purpose: Used for handling HTTP GET requests to retrieve a single object based on its primary key.
Inheritance: Inherits from generics.GenericAPIView and mixins.RetrieveModelMixin.
### generics.ListAPIView
In Django REST Framework (DRF), generics.ListAPIView is a class-based view that provides a generic implementation for retrieving a list of objects.
Purpose: Used for handling HTTP GET requests to retrieve a list of objects.
Inheritance: Inherits from generics.GenericAPIView and mixins.ListModelMixin.
### generics.UpdateAPIView
In Django REST Framework (DRF), generics.UpdateAPIView is a class-based view that provides a generic implementation for updating a single object.
Purpose: Used for handling HTTP PUT and PATCH requests to update a single object based on its primary key.
Inheritance: Inherits from generics.GenericAPIView and mixins.UpdateModelMixin.
### generics.RetrieveUpdateDestroyAPIView
In Django REST Framework (DRF), generics.RetrieveUpdateDestroyAPIView is a class-based view that combines the functionality for retrieving, updating, and destroying (deleting) a single object based on its primary key. This view is a combination of generics.RetrieveAPIView, generics.UpdateAPIView, and generics.DestroyAPIView.
generics.RetrieveUpdateDestroyAPIView:
Purpose: Used for handling HTTP GET (retrieve), PUT and PATCH (update), and DELETE (destroy) requests for a single object based on its primary key.
Inheritance: Inherits from generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, and mixins.DestroyModelMixin.

#### Thanks and Regards
Kumar Satyam
https://www.linkedin.com/in/kumar-satyam-769340243/
