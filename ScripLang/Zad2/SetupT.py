from distutils.core import setup, Extension

module1 = Extension('hello',
                    sources = ['t.c'])

setup (name = 'PackagdaesaName',
       version = '1.1',
       description = 'This is a demo package',
       ext_modules = [module1])
