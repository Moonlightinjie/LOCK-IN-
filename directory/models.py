from django.db import models

# Creating a table for the parishes in Jamaica

class Parish(models.Model):
    name = models.CharField(max_length=60, unique=True)
    # This tells python were making a table called Parish

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "parishes"
    # This organizes all the parishes in alphabetical order

    def __str__(self):
        return self.name
    # Changes how rows are displayed as text


# Creating a table for the types of specialists (e.g. Cardiology)

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "specialties"

    def __str__(self):
        return self.name


class Service(models.Model):
    """A service or procedure, e.g. 'MRI scan' or 'Cataract surgery'."""
    name = models.CharField(max_length=150)
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name="services")
    is_procedure = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


# Creating a table specifically for an area in Kingston
# (Provider replaces the unfinished Clinics table: each row is one clinic or hospital)

class Provider(models.Model):
    name = models.CharField(max_length=200)
    parish = models.ForeignKey(Parish, on_delete=models.PROTECT, related_name="providers")
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    last_confirmed = models.DateField(null=True, blank=True,
                                      help_text="Date this info was last verified with the provider")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProviderService(models.Model):
    # Links a provider to a service, with price and availability.
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="offerings")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="offerings")
    price_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text="JMD")
    price_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                    help_text="JMD (leave blank if a single price)")
    next_available = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["provider", "service"], name="unique_provider_service")
        ]

    def __str__(self):
        return f"{self.provider} - {self.service}"