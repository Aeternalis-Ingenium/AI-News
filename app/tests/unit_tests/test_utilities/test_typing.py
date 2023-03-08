from unittest import TestCase

from src.security.hashing.algorithms import Argon2Algorithm, BCryptAlgorithm, SHA256Algorithm, SHA512Algorithm
from src.utility.typing.algorithm import HashingAlgorithmSubClass


class TestHashingAlgorithmCustomType(TestCase):
    def setUp(self) -> None:
        self.argon2 = Argon2Algorithm()
        self.bcrypt = BCryptAlgorithm()
        self.sha256 = SHA256Algorithm()
        self.sha512 = SHA512Algorithm()

    async def test_acceptance_type_for_argon2(self) -> None:
        assert isinstance(self.argon2, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_bcrypt(self) -> None:
        assert isinstance(self.bcrypt, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_hsa256(self) -> None:
        assert isinstance(self.sha256, HashingAlgorithmSubClass)  # type: ignore

    async def test_acceptance_type_for_hsa512(self) -> None:
        assert isinstance(self.sha512, HashingAlgorithmSubClass)  # type: ignore

    def tearDown(self):
        pass
