import logging.handlers
import subprocess
import requests

class SumologicHandler(logging.handlers.HTTPHandler):
    def emit(self, record):
        log_entry = self.format(record)

#        log_url = f'https://{self.host}{self.url}'
        log_url = 'https://{}{}'.format(self.host, self.url)
        headers = {
            'Cache-Control': "no-cache",
            'Content-Type': "application/json"
        }
        response = requests.post(log_url, data=log_entry, headers=headers)


        #command = ['curl', '-s', '-X', 'POST', log_url, '-H', 'content-type: application/json', '-d', log_entry]
        #return subprocess.check_output(command)

        return response
