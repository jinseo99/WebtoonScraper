import contextlib
import tempfile
import urllib.request


def retrieve(req, filepath):
    with contextlib.closing(urllib.request.urlopen(req)) as fp:
        headers = fp.info()

        tfp = open(filepath, 'wb')

        with tfp:
            result = filepath, headers
            bs = 1024*8
            size = -1
            read = 0
            blocknum = 0
            if "content-length" in headers:
                size = int(headers["Content-Length"])

            while True:
                block = fp.read(bs)
                if not block:
                    break
                read += len(block)
                tfp.write(block)
                blocknum += 1
