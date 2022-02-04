from flask.cli import FlaskGroup

from app import app, db
from models import SuperHeroes, Chronicles

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("add_default_content_to_tables")
def add_default_content_to_tables():
    db.session.add(SuperHeroes(
        name="SpiderMan",
        power=5,
        is_villain=False
    )),
    db.session.add(SuperHeroes(
        name="IronMan",
        power=7,
        is_villain=False
    )),
    db.session.add(SuperHeroes(
        name="Thanos",
        power=10,
        is_villain=True
    )),
    db.session.add(SuperHeroes(
        name="Joker",
        power=6,
        is_villain=True
    ))
    db.session.commit()

    db.session.add(Chronicles(
        hero_id=1,
        year=2021,
        text='Fight against all enemies'
    )),
    db.session.add(Chronicles(
        hero_id=2,
        year=2021,
        text='Is died'
    )),
    db.session.add(Chronicles(
        hero_id=3,
        year=2021,
        text='Powerfull boy'
    ))
    db.session.add(Chronicles(
        hero_id=4,
        year=2021,
        text='Nice smile'
    ))
    db.session.commit()


if __name__ == "__main__":
    cli()

