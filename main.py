import http.server
import socketserver
import json
import os
from llama_index import GPTSimpleVectorIndex

index = GPTSimpleVectorIndex.load_from_disk('index.json')

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(body)

        # 校验必要参数是否存在
        if 'body' not in data:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Missing body parameter'}).encode())
            return

        ret = index.query(data['body'])

        # 处理 POST 请求，此处只返回 JSON 数据
        result = {'errno': 200, 'data': ret+''}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

port = int(os.environ.get('LLAMA_SRV_PORT', 8080))

with socketserver.TCPServer(("", port), MyRequestHandler) as httpd:
    print("Serving at port", port)
    httpd.serve_forever()