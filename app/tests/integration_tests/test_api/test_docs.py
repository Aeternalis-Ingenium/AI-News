async def test_get_docs_page(async_client):
    response = await async_client.get("/docs")
    assert response.status_code == 200
