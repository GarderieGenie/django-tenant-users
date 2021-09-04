import setuptools

setuptools.setup(
    name="django-tenant-users",
    version="0.1",
    description="A Django app to manage users in a multitenant environment",
    packages=setuptools.find_namespace_packages(include=['tenant_users.*']),
    namespace_packages=['tenant_users'],
)
