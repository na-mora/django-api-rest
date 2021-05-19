from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

# Create your models here.
class UserManager(BaseUserManager):
    def _create_usuario(self, nombre_usuario, email, nombre, apellido, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            nombre_usuario =nombre_usuario,
            email = email,
            nombre = nombre,
            apellido = apellido,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_user (self, nombre_usuario, email, nombre, apellido, password = None, **extra_fields):
        return self._create_usuario(nombre_usuario, email, nombre, apellido, password, False, False, **extra_fields)

    def create_superuser(self, nombre_usuario, email, nombre, apellido, password = None, **extra_fields):
        return self._create_usuario(nombre_usuario, email, nombre, apellido, password, True, True,**extra_fields)

class User (AbstractBaseUser, PermissionsMixin):
    nombre_usuario = models.CharField(max_length=255, unique= True)
    email = models.EmailField('Correo Electronico', max_length=255, unique= True)
    nombre = models.CharField('Nombres', max_length=255, blank=True, null = True)
    apellido = models.CharField('Apellidos', max_length=255, blank=True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to= 'perfil/', max_length = 255, null = True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural ='Usuarios'

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido']

    def natural_key(self):
        return (self.nombre_usuario)

    def __str__(self):
        return "Usuario {0}, con nombre Completo: {1} {2}".format(self.nombre_usuario, self.apellido, self.nombre)

