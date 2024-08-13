from distutils.core import setup, Extension

def main():
    setup(name="c_extensions_nils",
          version="1.0.0",
          description="Python interface for the fibonnaci C library function",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("c_ext_module", ["python_c_extension_module.c"])])

if __name__ == "__main__":
    main()