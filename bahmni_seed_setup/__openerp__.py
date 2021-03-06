{
    "name": "Bahmni Seed Data setup",
    "version": "1.0",
    "depends": ["base","product", "stock", "sale", "sale_stock", "bahmni_pharmacy_product"],
    "author": "ThoughtWorks Technologies Pvt. Ltd.",
    "category": "Setup",
	"summary": "Initial data setup",
    "description": """
    """,
    'data': [
        'data/settings.xml',
        'data/product_category_setup.xml',
        'data/suppliers_seed_setup.xml',
        'data/warehouse_seed_setup.xml',
        'data/filters.xml',
        'data/discount_heads.xml',
        'data/unit_of_measures.xml',
        'data/payment_method.xml',
        'data/products.xml',
    ],
    'demo': [],
    'auto_install': False,
    'application': True,
    'installable': True,
}
