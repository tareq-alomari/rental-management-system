from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import SystemSetting

class SystemSettingTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='password', email='admin@example.com')
        self.user = User.objects.create_user(username='user', password='password', email='user@example.com')
        self.setting = SystemSetting.objects.create(key='TEST_KEY', value='123', value_type='INTEGER', is_public=True)
        self.private_setting = SystemSetting.objects.create(key='PRIVATE_KEY', value='Secret', is_public=False)

    def test_list_settings_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('/api/v1/settings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_list_settings_public_user(self):
        # Regular user should only see public settings
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/v1/settings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that we only got the public one
        keys = [s['key'] for s in response.data]
        self.assertIn('TEST_KEY', keys)
        self.assertNotIn('PRIVATE_KEY', keys)

    def test_update_setting_admin(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.patch(f'/api/v1/settings/{self.setting.id}/', {'value': '456'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.setting.refresh_from_db()
        self.assertEqual(self.setting.value, '456')

    def test_update_setting_forbidden_for_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(f'/api/v1/settings/{self.setting.id}/', {'value': '999'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
