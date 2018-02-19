#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:31:50 2018

@author: nllerandi
"""

import http.client

conn = http.client.HTTPSConnection("app.spongecell.com")

payload = "{\"query\":\"{\\n  concept(id: 134578) {\\n    name\\n  }\\n}\\n\"}"

headers = {
    'cookie': "production_person_credentials=88343e0b4d88083f0f0f15a4aed3094fab57a8b24b58db4b53c7ebc6e37b285cd38635e53fc9dbc0ebe902bbbba3c1f953e4c57879e762297dbbdc6bda86ccc7%253A%253A10417; XSRF-TOKEN=aG9l6H50qcs629xkuoLNYpn7pXtlIyfQk1tha5PsGmOfihG5ABDAeXnKuaRDQnR8J%252FzvE%252FScvByFqZYL0Ut0Jw%253D%253D; request_method=POST; _spongecell_loves_u=VlNCYzhUeTF3U2RVc3ZHbkUzbzBKRCtHSkxiZUZhTG95UnNqNzE5RERvMmxnMUFnY3Byb3FFelZqNDAvMmlXMit0L1hidklyc2dTVUhnVGc0VVpYL0cybFYxMk5SRjBpVms2OTZMaDh2UEZkMjk3eWw1TFh3bkpXc1Ird0pKQkUyaTlCcGtCMEtnR2tEWGtaVkFPemVMSllpRXUvWGY5dVU4RFpSRTJ1NTAvZDgybEY3dTJscitlU3J4bWJtU01rYXdVUVltVUF5OXJnNUtCbnNwT1J1MXBCSDB2Skg4QTdrMGtiRmQ4R2EwbElrUDduNW9YR3p1TE0reUlpVXU5S1hmN2ExQjdDRW5aU1BRNnRNZExaTi82cWljdW5teGJGU21QNWFCQnF1bXZjN0VQM1RJOWkvVnY3cDVNYm43TC92MHkxKzgyQ0NHYlpPY1pCMGtJSjNjaVY3YTd2YVNrMGZvRFphY3YvQmZZQk51a1FsZDVqUFFXUFVUa09ubVJLWGp0U0FZZGxGYkdCaklxRDBQTkcrYzNWUHJ6VUs2cXpqYXVYbjdIb2l1S2JES0Z2NXloK2M3eEhPQXJiV28vZmthQ0tSUVdDN0U3SHN3UEtKMGJ3WmJmSkptdS9OUmZJcVVFM3A0UDYrdjQ9LS15d3FJMWZobG92RWtMeWwxME5ZRWpBPT0%253D--49a6f9980c074e4e6ef76598883c8f7feea40215",
    'content-type': "application/json"
    }

conn.request("POST", "/api/queries?user_credentials=y3XBMdRIPkgJXsXOmNnd", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))