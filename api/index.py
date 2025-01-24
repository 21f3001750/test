import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        query_components = parse_qs(urlparse(self.path).query)
               
        names = query_components.get('name', [])
        with open('q-vercel-python.json','r') as f:
            json_obj=json.loads(f.read())
        d={"marks":[]}
        for data in json_obj:
        
            if names in data['name']:
                d['marks'].append(data['marks'])
           
    
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write(json.dumps(d).encode('utf-8'))
        return