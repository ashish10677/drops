# DROPS
DROPS stands for Division and Replication of Data in Cloud for Optimized Performance and Speed.

This is a Django Project to showcase DROPS methodology.

## Steps to run project

### 1. Clone the project
`git clone https://github.com/ashish10677/drops.git`

> `cd drops`

### 2. Setup the pip package manager
Check to see if your Python installation has pip. Enter the following in your terminal:
> `pip -h`

### 3. Install the virtualenv package
> `pip install virtualenv`

### 4. Create a virtual environment
> `virtualenv myvenev`

### 5. Activate virtual environment
> `source myvenv/bin/activate`

### 6. Install required packages
> `pip install -r requirements.txt`

### 7. Migrate
>`python manage.py migrate`

### 8. Start the server
>`python manage.py runserver`


The project will be available at 127.0.0.1:8000.
