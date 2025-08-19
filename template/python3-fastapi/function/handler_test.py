import pytest
from dotenv import load_dotenv

from .handler import handle
from .handler_types import RequestModel


@pytest.fixture(scope='session', autouse=True)
def load_env() -> None:
    load_dotenv()


@pytest.mark.asyncio
async def test_handle() -> None:
    # assert (await handle(RequestModel(data={'foo': 'bar'}))).data == {'foo': 'bar'}
    pass
