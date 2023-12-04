from django.db import models
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from services.uploader import Uploader
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


User = get_user_model()


CITIES = (
    ("Baki", "Baki"),
    ("Gence", "Gence"),
    ("Sumqayit", "Sumqayit"),
    ("Lenkeran", "Lenkeran"),
)

BANS = (
    ("Sedan", "Sedan"),
    ("Cip", "Cip"),
    ("Offroad", "Offroad"),
    ("Crossover", "Crossover"),
)

GEAR = (
    ("Mexaniki", "Mexaniki"),
    ("Avtomat", "Avtomat"),
    ("Variator", "Variator"),
    ("Robotlasdirilmis", "Robotlasdirilmis"),
)

OTURUCU = (
    ("on", "on"),
    ("arxa", "arxa"),
    ("tam", "tam")
)

CONDITIONS = (
    ("Yeni", "Yeni"),
    ("Surulmus", "Surulmus")
)


class Marka(DateMixin):
    name = models.CharField(max_length=255, verbose_name="Marka")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Marka"
        verbose_name_plural = "Markalar"


class Model(DateMixin):
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Model")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Model"
        verbose_name_plural = "Modeller"


class Color(DateMixin):
    name = models.CharField(max_length=255, verbose_name="Name of color")
    color = ColorField(verbose_name="Rəng")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Tags(DateMixin):
    name = models.CharField(max_length=255, verbose_name="Modes")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Condition(DateMixin):
    name = models.CharField(max_length=255, verbose_name="Condition")


    def __str__(self):
        return self.name

    class Meta:
        ordering=  ("-created_at", )
        verbose_name = "Condition"
        verbose_name_plural = "Condition"


class Car(DateMixin, SlugMixin):
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=255, choices=CITIES)
    release_year = models.CharField(max_length=255, verbose_name="Buraxilis ili")
    ban_type = models.CharField(max_length=255, choices=BANS)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    engine = models.CharField(max_length=255, verbose_name="Muherrik")
    km = models.CharField(max_length=255, verbose_name="Probeq")
    gear_box = models.CharField(max_length=255, choices=GEAR)
    oturucu = models.CharField(max_length=255, choices=OTURUCU)
    is_new = models.CharField(max_length=255, choices=CONDITIONS)
    count_of_seats = models.IntegerField()
    owners = models.IntegerField()
    condition = models.ManyToManyField(Condition, null=True, blank=True)
    store_country = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tags, null=True, blank=True)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    user_view_count = models.IntegerField()

    # Python, R --> programming language


    def __str__(self):
        return f"{self.marka}-->{self.model}"


    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Car)
        super(Car, self).save(*args, **kwargs)


class CarImages(DateMixin):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=Uploader.upload_image_to_cars)

    def __str__(self):
        return f"{self.created_at}"

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Car Image"
        verbose_name_plural = "Car Images"


class Selections(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cars = models.ManyToManyField(Car, verbose_name="Cars")
