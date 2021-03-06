import json


async def test_hello_python(test_cli):
    req_data = json.dumps({
        'field_1': 'print',
        'field_2': 'Hello Python'
    })
    res = await test_cli.post('/stage/one/hello_python', data=req_data)
    assert res.status == 200
    res_data = await res.json()
    assert res_data['data']['result'] is True
    await test_cli.close()
