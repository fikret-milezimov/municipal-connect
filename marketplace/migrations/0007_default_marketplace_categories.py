from django.db import migrations


def create_marketplace_categories(apps, schema_editor):
    MarketplaceCategory = apps.get_model("marketplace", "MarketplaceCategory")
    categories = [
        "Electronics",
        "Furniture",
        "Clothing",
        "Home & Garden",
        "Other",
    ]
    for name in categories:
        MarketplaceCategory.objects.get_or_create(name=name)


class Migration(migrations.Migration):
    dependencies = [
        ("marketplace", "0006_alter_marketplaceitem_category"),
    ]

    operations = [
        migrations.RunPython(create_marketplace_categories, migrations.RunPython.noop),
    ]
