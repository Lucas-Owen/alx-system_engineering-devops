#!/usr/bin/python3
"""This module defines number_of_subscribers function"""


def number_of_subscribers(subreddit):
	"""
	Queries the reddit API
	Returns the number of subscribers for the given subreddit
	"""
curl "https://www.reddit.com/r/lifehacks/about.json" ^
  -H "authority: www.reddit.com" ^
  -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "accept-language: en-US,en;q=0.9" ^
  -H "cache-control: max-age=0" ^
  -H "cookie: rdt=d2215c49f5aa2fb6319b9cf2f0f3e79b; edgebucket=HAjlnx6mpWx843ktTv; loid=000000000ndnqlszm4.2.1699337405777.Z0FBQUFBQmxTZFM5QTZKYkNndk04NGdhX1I4U1BGb0VLTGI2NmhqaHhObF9nTHYzcnJZSVdDMVhfRE8xRDNKLXExUmZXOGJBU1VwZUM4ZkJrYmZhTlBwVTF4SHZoOFBSSWt3QXlJdENaOGxiS2NoQVd5c19WQnNua3RpVU5QdTdYVHZHcEpUQ2liRlY; csrf_token=d8bfd2e32e229794cc3f7e4f8d201a7b; token_v2=eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJsb2lkIiwiZXhwIjoxNjk5NDIzODA1Ljc3ODA5OSwiaWF0IjoxNjk5MzM3NDA1Ljc3ODA5OSwianRpIjoiRFhyaWZXQXZVejJsc2JpOEZtbEdmZWY4S015WDBBIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml9uZG5xbHN6bTQiLCJsY2EiOjE2OTkzMzc0MDU3NzcsInNjcCI6ImVKeGtrZEdPdERBSWhkLWwxejdCX3lwX05odHNjWWFzTFFhb2szbjdEVm9jazcwN2NENHBIUDhuS0lxRkxFMnVCS0c0eXBsNzgxNFdMSVZNMDVRR3RheEFrcWIwSkRXV2Q1b1NGV3hHNW5LbEhTczBlR0NhVXVXU3VTMzB1TFFKemQxWTlPekVxTXBsNVVGVm9QVlVqVzFNWVh0aWZMT3gycENLNjNJcUUxZ1d5bWZ4b2g5eTlkWS1mN2JmaEhZd3JLZ0tEX1RPdUZWd1lfSERGSFpfVDAxNnRpNVkxTjdyUVdxZjYzRzc5bG16ME96Y2ZxN25yNDFrWEk2aC1RbjI3NjVmUWdjZWVWNW0xQUdNV01PUE11eklPdnlyRHFCeVFRRmpDZUxUQ09USzVkdF9DYlpyMDdfRzdSTV9mRFBpcGpmODFnelVjd25pMEtmeDlSc0FBUF9fSV9yYXVRIiwiZmxvIjoxfQ.qX5vO0R2yNVKIMOrbicDVX0r53KR7aYHAcrDYuogqoEikVUtDZXQBlo-j7s2BDlmXipUVs6Tucn6yhuUrF33kFCQupeDm2X_J5N6dCb_BqNEnFOkAalcuHgWntj2jVgahQxoqJRAr8pIxdrMOyid9MJFulzAzM4Yr5dhsEicgsusVaXgy3n442tZHuR6cHRhd0mVCUD9A7mRH82V6VItEVntZfpyuoJWElg--lRyNU7XYgBD8S-wQkIDwpkhqSOj9rhfCZ36u4thMABp0wsKnKuphnhgEDFHqiwa1_JVucPvnFvh142vf9BtCoFMBCnSmud_a3pFBVQ7hd-cKxRy2A; csv=2; session_tracker=gjdpkddjdfdgfmjenm.0.1699337521141.Z0FBQUFBQmxTZFV4QmxZSnhwWlMzUnRuZFlUVjNKR0NXLXBmX1Y2TmN5akRxOXQxVUdacy1JSXRJVnVSZ2p5R1RsRklOaTFZSWQtTFhhblhNYjVva3V2bGVYcFVYakNxc21teXRWQjlLVi1lUjBMNHVyYjhWbVREcDE5YVZqRlVwemVvNERfbUJ4V1c" ^
  -H "sec-ch-ua: ^\^"Chromium^\^";v=^\^"118^\^", ^\^"Google Chrome^\^";v=^\^"118^\^", ^\^"Not=A?Brand^\^";v=^\^"99^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  -H "sec-fetch-dest: document" ^
  -H "sec-fetch-mode: navigate" ^
  -H "sec-fetch-site: none" ^
  -H "sec-fetch-user: ?1" ^
  -H "upgrade-insecure-requests: 1" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" ^
  --compressed
