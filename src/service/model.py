input_lvs = [
    {
        'X': (18, 201, 1),
        'name': 'Area in sq meters',
        'terms': {
            'extra small': ('trapmf', 18, 18, 20, 28),
            'small': ('trapmf', 21, 30, 37, 47),
            'medium': ('trapmf', 40, 49, 58, 70),
            'large': ('trapmf', 59, 72, 85, 94),
            'extra large': ('trapmf', 86, 95, 200, 200),
        }
    },

    {
        'X': (0, 1.0001, 0.0001),
        'name': 'Proximity to Metro station in km',
        'terms': {
            'close': ('trapmf', 0, 0, .133, .249),
            'average': ('trapmf', .135, .266, .4, .511),
            'far': ('trapmf', .401, .533, 1, 1),
        }
    },

    {
        'X': (0, 1.0001, 0.0001),
        'name': 'Proximity to the city center in km',
        'terms': {
            'close': ('trapmf', 0, 0, .175, .305),
            'average': ('trapmf', .198, .325, .55, .645),
            'far': ('trapmf', .555, .65, 1, 1)
        }
    },

    {
        'X': (2.8, 5.1, 0.1),
        'name': 'Ceiling height in m',
        'terms': {
            'low': ('trapmf', 2.8, 2.8, 2.9, 3.1),
            'medium': ('trimf', 2.9, 3.2, 3.6),
            'high': ('trapmf', 3.2, 3.7, 5.1, 5.1)
        }
    }
]

output_lv = {
    'X': (0, 1.01, 0.001),
    'name': 'Apartment price',
    'terms': {
        'extra cheap': ('trapmf', 0, 0, .007, .011),
        'cheap': ('trimf', .009, .013, .019),
        'average': ('trimf', .016, .03, .039),
        'premium': ('trapmf', .032, .04, .102, .125),
        'vip': ('trapmf', .105, .15, 1, 1)
    }
}

rule_base = [
    (('extra small', 'close', 'close', 'low'), 'cheap'),
    (('extra small', 'close', 'close', 'medium'), 'average'),
    (('extra small', 'close', 'close', 'high'), 'premium'),
    (('extra small', 'close', 'average', 'low'), 'average'),
    (('extra small', 'close', 'average', 'medium'), 'average'),
    (('extra small', 'close', 'average', 'high'), 'premium'),
    (('extra small', 'close', 'far', 'low'), 'cheap'),
    (('extra small', 'close', 'far', 'medium'), 'cheap'),
    (('extra small', 'close', 'far', 'high'), 'average'),

    (('extra small', 'average', 'close', 'low'), 'cheap'),
    (('extra small', 'average', 'close', 'medium'), 'average'),
    (('extra small', 'average', 'close', 'high'), 'average'),
    (('extra small', 'average', 'average', 'low'), 'cheap'),
    (('extra small', 'average', 'average', 'medium'), 'cheap'),
    (('extra small', 'average', 'average', 'high'), 'average'),
    (('extra small', 'average', 'far', 'low'), 'cheap'),
    (('extra small', 'average', 'far', 'medium'), 'cheap'),
    (('extra small', 'average', 'far', 'high'), 'cheap'),

    (('extra small', 'far', 'close', 'low'), 'cheap'),
    (('extra small', 'far', 'close', 'medium'), 'average'),
    (('extra small', 'far', 'close', 'high'), 'average'),
    (('extra small', 'far', 'average', 'low'), 'extra cheap'),
    (('extra small', 'far', 'average', 'medium'), 'extra cheap'),
    (('extra small', 'far', 'average', 'high'), 'cheap'),
    (('extra small', 'far', 'far', 'low'), 'extra cheap'),
    (('extra small', 'far', 'far', 'medium'), 'extra cheap'),
    (('extra small', 'far', 'far', 'high'), 'cheap'),

    (('small', 'close', 'close', 'low'), 'average'),
    (('small', 'close', 'close', 'medium'), 'premium'),
    (('small', 'close', 'close', 'high'), 'premium'),
    (('small', 'close', 'average', 'low'), 'average'),
    (('small', 'close', 'average', 'medium'), 'average'),
    (('small', 'close', 'average', 'high'), 'premium'),
    (('small', 'close', 'far', 'low'), 'average'),
    (('small', 'close', 'far', 'medium'), 'average'),
    (('small', 'close', 'far', 'high'), 'premium'),

    (('small', 'average', 'close', 'low'), 'average'),
    (('small', 'average', 'close', 'medium'), 'average'),
    (('small', 'average', 'close', 'high'), 'premium'),
    (('small', 'average', 'average', 'low'), 'cheap'),
    (('small', 'average', 'average', 'medium'), 'average'),
    (('small', 'average', 'average', 'high'), 'premium'),
    (('small', 'average', 'far', 'low'), 'cheap'),
    (('small', 'average', 'far', 'medium'), 'cheap'),
    (('small', 'average', 'far', 'high'), 'premium'),

    (('small', 'far', 'close', 'low'), 'average'),
    (('small', 'far', 'close', 'medium'), 'average'),
    (('small', 'far', 'close', 'high'), 'premium'),
    (('small', 'far', 'average', 'low'), 'cheap'),
    (('small', 'far', 'average', 'medium'), 'cheap'),
    (('small', 'far', 'average', 'high'), 'average'),
    (('small', 'far', 'far', 'low'), 'extra cheap'),
    (('small', 'far', 'far', 'medium'), 'extra cheap'),
    (('small', 'far', 'far', 'high'), 'average'),

    (('medium', 'close', 'close', 'low'), 'premium'),
    (('medium', 'close', 'close', 'medium'), 'vip'),
    (('medium', 'close', 'close', 'high'), 'vip'),
    (('medium', 'close', 'average', 'low'), 'premium'),
    (('medium', 'close', 'average', 'medium'), 'premium'),
    (('medium', 'close', 'average', 'high'), 'vip'),
    (('medium', 'close', 'far', 'low'), 'average'),
    (('medium', 'close', 'far', 'medium'), 'premium'),
    (('medium', 'close', 'far', 'high'), 'vip'),

    (('medium', 'average', 'close', 'low'), 'average'),
    (('medium', 'average', 'close', 'medium'), 'premium'),
    (('medium', 'average', 'close', 'high'), 'vip'),
    (('medium', 'average', 'average', 'low'), 'cheap'),
    (('medium', 'average', 'average', 'medium'), 'premium'),
    (('medium', 'average', 'average', 'high'), 'premium'),
    (('medium', 'average', 'far', 'low'), 'cheap'),
    (('medium', 'average', 'far', 'medium'), 'cheap'),
    (('medium', 'average', 'far', 'high'), 'average'),

    (('medium', 'far', 'close', 'low'), 'average'),
    (('medium', 'far', 'close', 'medium'), 'premium'),
    (('medium', 'far', 'close', 'high'), 'premium'),
    (('medium', 'far', 'average', 'low'), 'cheap'),
    (('medium', 'far', 'average', 'medium'), 'cheap'),
    (('medium', 'far', 'average', 'high'), 'average'),
    (('medium', 'far', 'far', 'low'), 'extra cheap'),
    (('medium', 'far', 'far', 'medium'), 'cheap'),
    (('medium', 'far', 'far', 'high'), 'average'),

    (('large', 'close', 'close', 'low'), 'premium'),
    (('large', 'close', 'close', 'medium'), 'vip'),
    (('large', 'close', 'close', 'high'), 'vip'),
    (('large', 'close', 'average', 'low'), 'average'),
    (('large', 'close', 'average', 'medium'), 'premium'),
    (('large', 'close', 'average', 'high'), 'premium'),
    (('large', 'close', 'far', 'low'), 'average'),
    (('large', 'close', 'far', 'medium'), 'average'),
    (('large', 'close', 'far', 'high'), 'vip'),

    (('large', 'average', 'close', 'low'), 'premium'),
    (('large', 'average', 'close', 'medium'), 'premium'),
    (('large', 'average', 'close', 'high'), 'vip'),
    (('large', 'average', 'average', 'low'), 'cheap'),
    (('large', 'average', 'average', 'medium'), 'premium'),
    (('large', 'average', 'average', 'high'), 'vip'),
    (('large', 'average', 'far', 'low'), 'average'),
    (('large', 'average', 'far', 'medium'), 'premium'),
    (('large', 'average', 'far', 'high'), 'premium'),

    (('large', 'far', 'close', 'low'), 'premium'),
    (('large', 'far', 'close', 'medium'), 'vip'),
    (('large', 'far', 'close', 'high'), 'vip'),
    (('large', 'far', 'average', 'low'), 'average'),
    (('large', 'far', 'average', 'medium'), 'premium'),
    (('large', 'far', 'average', 'high'), 'premium'),
    (('large', 'far', 'far', 'low'), 'average'),
    (('large', 'far', 'far', 'medium'), 'average'),
    (('large', 'far', 'far', 'high'), 'premium'),

    (('extra large', 'close', 'close', 'low'), 'premium'),
    (('extra large', 'close', 'close', 'medium'), 'vip'),
    (('extra large', 'close', 'close', 'high'), 'vip'),
    (('extra large', 'close', 'average', 'low'), 'premium'),
    (('extra large', 'close', 'average', 'medium'), 'vip'),
    (('extra large', 'close', 'average', 'high'), 'vip'),
    (('extra large', 'close', 'far', 'low'), 'average'),
    (('extra large', 'close', 'far', 'medium'), 'premium'),
    (('extra large', 'close', 'far', 'high'), 'vip'),

    (('extra large', 'average', 'close', 'low'), 'premium'),
    (('extra large', 'average', 'close', 'medium'), 'vip'),
    (('extra large', 'average', 'close', 'high'), 'vip'),
    (('extra large', 'average', 'average', 'low'), 'average'),
    (('extra large', 'average', 'average', 'medium'), 'average'),
    (('extra large', 'average', 'average', 'high'), 'premium'),
    (('extra large', 'average', 'far', 'low'), 'average'),
    (('extra large', 'average', 'far', 'medium'), 'premium'),
    (('extra large', 'average', 'far', 'high'), 'premium'),

    (('extra large', 'far', 'close', 'low'), 'premium'),
    (('extra large', 'far', 'close', 'medium'), 'premium'),
    (('extra large', 'far', 'close', 'high'), 'vip'),
    (('extra large', 'far', 'average', 'low'), 'average'),
    (('extra large', 'far', 'average', 'medium'), 'premium'),
    (('extra large', 'far', 'average', 'high'), 'premium'),
    (('extra large', 'far', 'far', 'low'), 'average'),
    (('extra large', 'far', 'far', 'medium'), 'average'),
    (('extra large', 'far', 'far', 'high'), 'premium'),

]

distances = {
    "Kyiv": {
        "metro": [0, 15],
        "city": [0, 20]
    }
}
