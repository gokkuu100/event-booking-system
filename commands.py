import click
from sqlalchemy.orm import Session
from models import Venue, Event, Booking, Base
from database import SessionLocal, engine
from datetime import datetime

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Venue name", help="Name of the venue")
@click.option("--capacity", prompt="Venue capacity", type=int, help="Venue capacity")
def add_venue(name, capacity):
    session = SessionLocal()
    venue = Venue(name=name, capacity=capacity)
    session.add(venue)
    session.commit()
    session.close()
    click.echo(f"Added venue: {name}")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    cli()


