from src.models.sqllite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=1),
            PetsTable(name="Buddy", type="dog", id=12),
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "Fluffy", "id": 1 },
                { "name": "Buddy", "id": 12 }
            ]
        }
    }

    assert response == expected_response
