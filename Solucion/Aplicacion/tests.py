from django.test import TestCase
import unittest
from .models import Productos, MisionyVision

# Create your tests here.
class TestProductos(unittest.TestCase):
    def guardarProducto(self):
        p = Productos(
            nombre="Coronavirus",
            precio=9000,
            descripcion="Mata pacos",
            stock=1800
        )
        valor=0
        try:
            p.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def eliminarProducto(self):
        p = Productos(
            nombre="borrador",
            precio=100,
            descripcion="jaja",
            stock=12
        )
        valor=0
        p.save()
        try:
            p.delete()
            valor=1
        except:
            valor=0

        self.assertEqual(valor,1)

class TestMisionVision(unittest.TestCase):
    def guardarMyV(self):
        myv = MisionyVision(
            nombre="2",
            mision="es la mision...",
            vision="es la vision..."
        )
        valor=0
        try:
            myv.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor,1)

    def eliminarMyv(self):
        myv = MisionyVision(
            nombre="3",
            mision="es la mision...",
            vision="es la vision..."
        )
        valor=0
        myv.save()
        try:
            myv.delete()
            valor=1
        except:
            valor=0

        self.assertEqual(valor,1)


if __name__ == "__main__":
    unittest.main()

