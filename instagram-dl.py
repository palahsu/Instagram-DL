# Sorry, This is encrypted!
# As there are a lot of Copy Cats we encrypted our Codes.

# Telegram Group: http://t.me/linux_repo
 

import base64, codecs
magic = 'I0lNUE9SVFMKZnJvbSBvcyBpbXBvcnQgbGluawpmcm9tIHRraW50ZXIgaW1wb3J0ICoKZnJvbSBzcmMgaW1wb3J0IGxvYWQKZnJvbSBQSUwgaW1wb3J0IEltYWdlVGssSW1hZ2UKaW1wb3J0IHRraW50ZXIKCiNWYXJpYWJsZQojSW5zdGFncmFtIERvd25sb2FkZXIgUHJvID0gbG9hZAppbnB1dF9mb250ID0gKCdWZXJkYW5hJywxMCkKc2NyZWVuX2ZvbnQgPSAoJ1ZlcmRhbmEnLDI1KQpidG5fZm9udCA9ICgnVmVyZGFuYScsMTUpCmJnX2NvbG9yPScjMTExMTExJwpmb250X2NvbG91cj0nd2hpdGUnCgoKCgojRnVuY3Rpb25zCmRlZiBnZXQoKToKICAgIHVybD1saW5rLmdldCgpCiAgICBzZWxlY3Q9b3B0aW9uLmdldCgpCiAgICAKICAgIGlmIGxvYWQuY29ubmVjdGlvbigpPT1UcnVlOgogICAgICAgIGlmIHNlbGVjdD09MToKICAgICAgICAgICAgbG9hZC5kb3dubG9hZF9wb3N0KHVybCkKICAgICAgICAgICAgYmFubmVyLmRlbGV0ZSgwLEVORCkKICAgICAgICAgICAgYmFubmVyLmluc2VydCgwLGxvYWQucmVzdWx0KQogICAgICAgIGVsaWYgc2VsZWN0PT0yOgogICAgICAgICAgICBsb2FkLmRvd25sb2FkX3BwKHVybCkKICAgICAgICAgICAgYmFubmVyLmRlbGV0ZSgwLEVORCkKICAgICAgICAgICAgYmFubmVyLmluc2VydCgwLGxvYWQucmVzdWx0KQogICAgZWxzZToKICAgICAgICBiYW5uZXIuZGVsZXRlKDAsRU5EKQogICAgICAgI'
love = 'TWuoz5ypv5coaAypaDbZPjvGz8tFJ50MKWhMKDvXDbXPvZtVRphIF5WPzSjpQ1HnltcPzSjpP5aMJ9gMKElrFtaAGtmrQD2AlpcPzSjpP50nKEfMFtaFJ5mqTSapzSgVREiq25fo2SxMKVaXDcupUNhnJAiozWcqT1upPtap3WwKSkcL29hYzywolpcPzSjpP5wo25znJq1pzHbLzSwn2qlo3IhMQ1vM19wo2kipvxXo3O0nJ9hCHyhqSMupvtcPz9jqTyiov5mMKDbZFxXLaEhCIObo3EiFJ1uM2HbMzyfMG0ap3WwKSkvqT4hpT5aWlxXnJ1aCHygLJqyYz9jMJ4bW3AlL1kpnTIuMP5jozpaXDcvMm1WoJSaMIEeYyObo3EiFJ1uM2HbnJ1aXDbXPtbwqTy0oTHXGTSvMJjbLKOjYUEyrUD9W0yhp3EuM3WuoFORo3qhoT9uMTIlVULkYwHaYTMaCFq3nTy0MFpfLzp9LzqsL29fo3VfnaImqTyzrG0aL2IhqTIlWlxhM3WcMPulo3p9ZPkwo2k1oJ49ZPxXqTy0oTHtCHkuLzIfXTygLJqyCJWaYTWxCGNcVPNXqTy0oTHhM3WcMPuwo2k1oJ49ZPklo3p9ZFxXPtbwnTIuMNcZLJWyoPuupUNfnJ1uM2H9LzpfnaImqTyzrG0aL2IhqTIlWlkvMQ0jXF5apzyxXUWiqm0kYTAioUIgow0jYUOuMUt9ZGZjXDbXPtbwqKWfVTIhqUW5Pzkcozf9H3ElnJ5aIzSlXPxXGTSvMJjbLKOjYUEyrUD9W1Oup3EyVSIFGQbaYTMioaD9XPp4WlxfMzp9W3qbnKEyWlkvMm0aVmRkZGRkZFpcYzqlnJDbpz93CGVfL29fqJ1hCGNfp3EcL2g5CIpfpTSxrQ0kZGNcPzkcozf9EJ50paxbLK'
god = 'BwLGJkPTEsZm9udD1pbnB1dF9mb250KQpsaW5rLmdyaWQocm93PTIsY29sdW1uPTAsc3RpY2t5PVcscGFkeD0yMjApCkxhYmVsKGFwcCx0ZXh0PSdJbWFnZSAmIFZpZGVvIERvd25sb2FkZXInLGZvbnQ9KCc1JyksanVzdGlmeT0nY2VudGVyJyxmZz0nd2hpdGUnLGJnPScjMTExMTExJykuZ3JpZChyb3c9Myxjb2x1bW49MCxwYWR5PTEwKQoKI3JhZGlvIGJ1dHRvbnMKcmFkaW9fcHJvX3BpYz1TdHJpbmdWYXIoKQpyYWRpb19wb3N0PVJhZGlvYnV0dG9uKGFwcCx2YXJpYWJsZT1vcHRpb24sdmFsdWU9MSx0ZXh0PSdJbWFnZScsZmc9Zm9udF9jb2xvdXIKICAgICAgICAgICAgICAgICAgICAgICAsYmc9YmdfY29sb3IsYWN0aXZlYmFja2dyb3VuZD1iZ19jb2xvcixhY3RpdmVmb3JlZ3JvdW5kPWJnX2NvbG9yLHNlbGVjdGNvbG9yPWJnX2NvbG9yLGZvbnQ9MTApCnJhZGlvX3Byb19waWM9UmFkaW9idXR0b24oYXBwLHZhcmlhYmxlPW9wdGlvbix2YWx1ZT0yLHRleHQ9J1ZpZGVvJyxmZz1mb250X2NvbG91cixiZz1iZ19jb2xvciwKICAgICAgICAgICAgICAgICAgICBhY3RpdmViYWNrZ3JvdW5kPWJnX2NvbG9yLGFjdGl2ZWZvcmVncm91bmQ9YmdfY29sb3IsZm9udD0xMCxzZWxlY3Rjb2xvcj1iZ19jb2xvcikKcmFkaW9fcHJvX3BpYy5ncmlkKHJvdz00LGNvbHVtbj0wLHN0aWNreT1FLHBhZHg9MjAwKQpyYWRpb19wb3N0LmdyaWQocm9'
destiny = '3CGDfL29fqJ1hCGNfp3EcL2g5CIpfpTSxrQ0kAmNcPtbwHzImqJk0PzWuoz5ypw1SoaElrFuupUNfMz9hqQ1mL3WyMJ5sMz9hqPkvMm1vM19wo2kipvkvMQ0jYTMaCJMioaEsL29fo3IlYUEyrUE2LKWcLJWfMG1fo2SxYaWyp3IfqPkdqKA0nJM5CFqwMJ50MKVaXDcvLJ5hMKVhM3WcMPulo3p9AFkwo2k1oJ49ZPkjLJE5CGR1XDcvLJ5hMKVhnJ5mMKW0XQNfoT9uMP5lMKA1oUDcPtbwMT93ozkiLJDtLaEhPzEiq25fo2SxK2W0ow1PqKE0o24bLKOjYTygLJqyCJW0ovkvLJAeM3WiqJ5xCJWaK2AioT9lYTSwqTy2MJWuL2gapz91ozD9LzqsL29fo3VfnaImqTyzrG0aL2IhqTIlWlkvMQ0jVPkwo21gLJ5xCJkuoJWxLGcaMKDbXFxXMT93ozkiLJEsLaEhYzqlnJDbpz93CGLfL29fqJ1hCGNfpTSxrG0kAFxXPtbwL3WyMUEmPvAZLJWyoPuupUNfqTI4qQ0aGJSxMFOvrIkhDJ1mnTIhH2uuoaHtWvODLJkunUA1VPLtDJWcpxuup2ShZwNjAFpfMzp9W3qbnKEyWlkvMm1vM19wo2kipvkdqKA0nJM5CFqwMJ50MKVaXF5apzyxXUWiqm03YTAioUIgow0jXDbwGTSvMJjbLKOjYUEyrUD9W1Eio2jtMz9lVTEiq25fo2SxnJ5aVUMcMTIiplOuozDtpTuiqT9mVTMlo20tFJ5mqTSapzSgVTMlo20tHT9mqPOZnJ5eWlkzMm0aq2ucqTHaYTWaCJWaK2AioT9lYTc1p3EcMax9W2AyoaEypvpcYzqlnJDbpz93CGtfL29fqJ1hCGNcPtbXLKOjYz1unJ5fo29jXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))