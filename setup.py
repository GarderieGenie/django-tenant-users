import setuptools
import versioneer

setuptools.setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name="django-tenant-users",
    description="A Django app to manage users in a multitenant environment",
    packages=setuptools.find_namespace_packages(include=['tenant_users.*']),
    namespace_packages=['tenant_users'],
)
