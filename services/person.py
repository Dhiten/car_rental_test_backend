from models.person import Person as PersonModel
from schemas.person import PersonCreate

class PersonService():

    def __self__(self, db) -> None:
        self.db = db

    def get(self):
        persons = self.db.query(PersonModel).all()

        self.db.close()
        return persons

    def get_person(self, id: int):
        person = self.db.query(PersonModel).filter(PersonModel.id == id).first()

        self.db.close()
        return person

    def create(self, person: PersonCreate):
        new_person = PersonModel(**person.dict())

        self.db.add(new_person)
        self.db.commit()
        self.db.refresh(new_person)
        self.db.close()
        return new_person
    
    def update(self, id: int, person: PersonCreate):
        person_db = self.db.query(PersonModel).filter(PersonModel.id == id).first()

        person_db.name = person.name if person.name else person_db.name
        person_db.cpf = person.cpf if person.cpf else person_db.cpf
        person_db.email = person.email if person.email else person_db.email
        person_db.phone = person.phone if person.phone else person_db.phone
        self.db.commit()
        self.db.close()
        return person_db

    def delete(self, id: int):
        person_db = self.db.query(PersonModel).filter(PersonModel.id == id).first()
        
        self.db.delete(person_db)
        self.db.commit()
        self.db.close()
        return person_db