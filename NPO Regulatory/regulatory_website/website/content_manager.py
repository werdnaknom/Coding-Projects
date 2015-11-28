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
<<<<<<< HEAD

        ''' Regulatory
                Name, Database Table, Description
        '''
        self.REGULATORY = \
            {"Immunity" :
                            [["AC, DC, and I/O Surge","regulatory_surge",
                            '''To demonstrate power supply and system tolerance for transients on the AC and DC power lines
                            caused by switching or lightning.'''],
                            ["AC Voltage Freq and Source Interrupt","regulatory_interrupt",
                            '''To demonstrate power supply performance with maximum and typical test loads over a range of AC
                            line voltages and frequencies. To simulate power line interruptions lasting for 12mSec at the
                            system level. Power supply certification is 10mSec and this test provides for a small guard band'''],
                            ["Conducted Immunity", "regulatory_conducted_immunity",
                            '''To demonstrate that system products can withstand electromagnetic fields such as those generated
                            by intentional RF transmitters or any other devices that may couple emissions onto the power or I/O
                            cables connected to the installed equipment. This demonstrates compliance to International legal
                            requirements.'''],
                            ["Electrical Fast Transient", "regulatory_electrical_fast_transient",
                            '''To demonstrate that bursts or spikes generated by environmental noise (motors, relays, etc.) will
                            not impair the operation of the product. EFT is applied to the input AC and DC power and all I/O
                            cables. This demonstrates compliance to international legal requirements.'''],
                            ["Flicker and Voltage Fluctuation", "regulatory_flicker",
                            '''To ensure flicker and voltage fluctuations are limited in low-voltage AC supply system.'''],
                            ["Power Frequency Magnetic Fields", "regulatory_pwr_freq_magnetic",
                            '''To demonstrate the immunity of equipment when subjected to power frequency magnetic fields
                            related to the specific location and installation condition of the equipment (i.e., proximity of
                            equipment to the disturbance source). This test demonstrates compliance to international legal
                            requirements. This test is a legal requirement for equipment containing devices susceptible to
                            magnetic fields, examples of which include CRT monitors, Hall Effect elements, electrodynamic
                            microphones and magnetic field sensors. For equipment that does not meet these criteria, this test
                            is not required.'''],
                            ["Power Line Conducted", "regulatory_pwr_line_conducted",
                            '''To investigate whether the level of emissions conducting from a product will interfere with other
                            electronic products. This demonstrates compliance to U.S. (FCC), European (EN) and International
                            (CISPR) legal requirements.'''],
                            ["Power Line Harmonics", "regulatory_power_line_harmonics_id",
                            '''To ensure harmonics from an AC line cord will not create excessive noise on public power lines.
                            This test is applicable to all products with power ratings > 75 Watts and < 1000 Watts. '''],
                            ["Radiated Immunity", "regulatory_radiated_immunity",
                            '''To demonstrate that system products can withstand electromagnetic fields such as those generated
                            by portable radio transceivers (walkie-talkies) or any other devices that will generate continuous
                            wave radiated electromagnetic energy . This demonstrates compliance to European legal
                            requirements.'''],
                            ["Telecom Port Conducted Emissions", "regulatory_telecom_port_conducted_emissions",
                            '''To investigate whether the level of emissions conducting from a product on the telecom ports will
                            interfere with other electronic products. This demonstrates compliance to European (EN) and
                            International (CISPR) legal requirements.'''],
                            ["Voltage Dip and Dropout", "regulatory_dip_and_dropout",
                            '''To demonstrate power supply can withstand power line interruptions caused by faults in the power
                            grind. This may be due to new equipment installations or a result of a sudden large load variation
                            lasting for a duration of between half a cycle to 1 minute. This demonstrates compliance to
                            international legal requirements.''']],
                "Emissions" :
                            [["Telecom Port Conducted Emissions", "regulatory_telecom_port_conducted_emissions",
                            '''To investigate whether the level of emissions conducting from a product on the telecom ports will
                            interfere with other electronic products. This demonstrates compliance to European (EN) and
                            International (CISPR) legal requirements.'''],
                            ["Radiated Emissions", "regulatory_radiated_emissions",
                            '''To investigate whether the level of emissions radiating from a product will interfere with other
                            electronic products. This demonstrates compliance to U.S., European and International legal
                            requirements.''']],
                "ESD" :
                            [["Electrical Discharge", "regulatory_esd",
                            '''To demonstrate that system products can withstand static discharges encountered in normal
                            handling or operation of the equipment. This profile is a hybrid of the Intel ESD test requirements
                            and the IEC test profile.''']],
             }



=======
>>>>>>> parent of f391f91... Regulatory Modifications
