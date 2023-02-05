from models.person import Person as PersonModel
from schemas.person import PersonCreate

class PersonService():
    
    # def __init__(self, db) -> None:
    #     self.db = db

    def get(self):
        persons = self.query(PersonModel).all()

        self.close()
        return persons

    def get_person(self, id: int):
        person = self.query(PersonModel).filter(PersonModel.id == id).first()

        self.close()
        return person

    def create(self, person: PersonCreate):
        new_person = PersonModel(**person.dict())

        self.add(new_person)
        self.commit()
        self.refresh(new_person)
        self.close()
        return new_person
    
    def update(self, id: int, person: PersonCreate):
        person_db = self.query(PersonModel).filter(PersonModel.id == id).first()

        person_db.name = person.name if person.name else person_db.name
        person_db.cpf = person.cpf if person.cpf else person_db.cpf
        person_db.email = person.email if person.email else person_db.email
        person_db.phone = person.phone if person.phone else person_db.phone
        self.commit()
        self.close()
        return person_db

    def delete(self, id: int):
        person_db = self.db.query(PersonModel).filter(PersonModel.id == id).first()
        
        self.delete(person_db)
        self.commit()
        self.close()
        return person_db