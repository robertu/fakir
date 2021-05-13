import pytest
import datetime
from django.utils import timezone
from fakir.models import Firma, NumeracjaFaktur, LicznikFaktur, Faktura, JednostaMiary, StawkaPodatku, PozycjaFaktury

@pytest.mark.django_db
def test_licznika():
    date = timezone.now()
    nr = NumeracjaFaktur.objects.create(wzorzec='TEST/{d}/{m}/{r}/{n}')
    assert nr.numer() == nr.wzorzec.format(d=date.day, m=date.month, r=date.year, n=0)

@pytest.mark.django_db
def test_pozycji():
    date = timezone.now()

    nr = NumeracjaFaktur.objects.create(wzorzec='FV/{d}/{m}/{r}/{n}')
    faktura = Faktura.objects.create(numeracja=nr, data_sprzedazy=date, data_wystawienia=date - datetime.timedelta(days=2))

    j_m = JednostaMiary.objects.create(nazwa='ilosc')
    st_podatku = StawkaPodatku.objects.create(nazwa='VAT', stawka=0.23)

    for i in range(10):
        pozycja = PozycjaFaktury.objects.create(faktura=faktura, nazwa='Item' + str(i+1), jm=j_m, ilosc=3, cena=16.00, wartosc_netto=12.32, stawka_podatku=st_podatku)

    assert pozycja.nazwa == 'Item10'

@pytest.mark.django_db
@pytest.mark.xfail
def test_faktury():
    date = timezone.now()
    nr = NumeracjaFaktur.objects.create(wzorzec='FV/{d}/{m}/{r}/{n}')
    faktura = Faktura.objects.create(numeracja=nr, data_sprzedazy=date - datetime.timedelta(days=2), data_wystawienia=date)
    assert faktura.data_sprzedazy > faktura.data_wystawienia


