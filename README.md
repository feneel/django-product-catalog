# Remarcable Product Catalog

### Overview
This Django project demonstrates searchable and filterable product catalog tailored for construction tech industry

### Features
- Category and Tag based filtering
- Search by product name functionality
- Relational modeling between Product, Category and Tag

## Setup Instructions

Step 1-  Clone the repo: ```git clone https://github.com/feneel/django-product-catalog.git```

Step 2- Setup your virtual environment: 
     ```python -m venv env 
        source env/bin/activate
        cd product_catalog```

Step 3- Install dependencies: ```pip install -r requirements.txt```

Step 4- Run migrations: ```python manage.py migrate```

Step 5- Load the seed data: ```python manage.py loaddata seed_data.json```

Step 6- Start development server: ```python manage.py runserver```



## Project Details
- Product:
  - name: CharField
  - description: TextField
  - price: DecimalField
  - category: ForeignKey-> Category
  - tags: ManytoMany-> Tag

- Category
  - name: CharField
- Tag:
  - name: CharField

