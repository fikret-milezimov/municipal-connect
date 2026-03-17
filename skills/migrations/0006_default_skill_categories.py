from django.db import migrations


def create_skill_categories(apps, schema_editor):
    SkillCategory = apps.get_model("skills", "SkillCategory")
    categories = [
        "IT & Programming",
        "Home Repair",
        "Cleaning Services",
        "Education & Tutoring",
        "Health & Fitness",
    ]
    for name in categories:
        SkillCategory.objects.get_or_create(name=name)


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0005_alter_skill_categories"),
    ]

    operations = [
        migrations.RunPython(create_skill_categories, migrations.RunPython.noop),
    ]
