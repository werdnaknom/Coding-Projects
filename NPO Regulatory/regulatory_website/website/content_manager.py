__author__ = 'ammonk'


class Content():
    def __init__(self):
        self.CUSTOMER = ["OEMGEN",
                         "Dell",
                         "HP",
                         "Lenovo",
                         "SuperMicro",
                         ]

        self.SILICON = ["Fortville",
                        "Sageville",
                        "Red Rock Canyon",
                        "Niantic",
                        "Powerville",
                        ]
        ''' Content Name, Address, Page Class'''
        self.TOC = [["Dashboard", "/", "dashboard"],
                    ["Calendar", "/calendar/", "calendar"],
                    ["Product List", "/products/", "products"],
                    ["Add Product", "/add_product/", "addProduct"],
                    ["Add Testplan", "/testplan/add_testplan", "Add Product Testplan"]
                    ]
        self.DATABASE = "db/website.db"
