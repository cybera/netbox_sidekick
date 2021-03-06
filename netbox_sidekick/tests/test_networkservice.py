from django.urls import reverse

from netbox_sidekick.models import (
    LogicalSystem, RoutingType,
    NetworkServiceType, NetworkService,
)

from .utils import BaseTest


class NetworkServiceTest(BaseTest):
    # Logical System
    def test_logicalsystem_basic(self):
        v = LogicalSystem.objects.get(name="Peering")
        self.assertEqual(v.slug, "peering")

    def test_view_logicalsystem_index(self):
        resp = self.client.get(
            reverse('plugins:netbox_sidekick:logicalsystem_index'))
        self.assertContains(resp, 'Peering')

    def test_view_logicalsystem_detail(self):
        v = LogicalSystem.objects.get(id=1)
        resp = self.client.get(v.get_absolute_url())
        self.assertContains(resp, 'Peering')
        self.assertContains(resp, "East University&#x27;s peering service")

    # Network Service Type
    def test_networkservicectype_basic(self):
        v = NetworkServiceType.objects.get(name="Peering")
        self.assertEqual(v.slug, "peering")

    def test_view_networkservicetype_index(self):
        resp = self.client.get(
            reverse('plugins:netbox_sidekick:networkservicetype_index'))
        self.assertContains(resp, 'Peering')

    def test_view_networkservicetype_detail(self):
        v = NetworkServiceType.objects.get(id=1)
        resp = self.client.get(v.get_absolute_url())
        self.assertContains(resp, 'Peering')
        self.assertContains(resp, "East University&#x27;s peering service")

    # Network Service
    def test_networkservice_basic(self):
        v = NetworkService.objects.get(member__name='East University')
        self.assertEqual(v.name, "East University's peering service")

    def test_view_networkservice_index(self):
        resp = self.client.get(
            reverse('plugins:netbox_sidekick:networkservice_index'))
        self.assertContains(resp, "East University&#x27;s peering service")

    # Routing Type
    def test_routingtype_basic(self):
        v = RoutingType.objects.get(name="BGP")
        self.assertEqual(v.slug, "bgp")

    def test_view_routingtype_index(self):
        resp = self.client.get(
            reverse('plugins:netbox_sidekick:routingtype_index'))
        self.assertContains(resp, 'BGP')

    def test_view_routingtype_detail(self):
        v = RoutingType.objects.get(id=1)
        resp = self.client.get(v.get_absolute_url())
        self.assertContains(resp, 'BGP')
        self.assertContains(resp, "East University&#x27;s peering service")
