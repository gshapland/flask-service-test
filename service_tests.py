import os
import service
import unittest
import tempfile

class ServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, service.app.config['DATABASE'] = tempfile.mkstemp()
        service.app.config['TESTING'] = True
        self.app = service.app.test_client()
        #with service.app.app_context():
        #    service.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(service.app.config['DATABASE'])
        
    def test_user(self):
        r = self.app.get('/user/test_name', follow_redirects=True)
        assert('test_name' in r.data)

if __name__ == '__main__':
    unittest.main()