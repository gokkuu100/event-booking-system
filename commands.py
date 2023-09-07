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

@cli.command()
@click.option("--name", prompt="Event name", help="Name of the event")
@click.option("--venue", prompt="Venue name", help="Name of the venue")
@click.option("--event-date", prompt="Event date (YYYY-MM-DD)", help="Date of the event in format YYYY-MM-DD")
def add_event(name, venue, event_date):
    session = SessionLocal()
    venue_obj = session.query(Venue).filter_by(name=venue).first()
    if venue_obj:
        try:
            event_date = datetime.strptime(event_date, "%Y-%m-%d")
        except ValueError:
            click.echo("Invalid date format. Please use YYYY-MM-DD.")
            session.close()
            return
        
        event = Event(name=name, venue=venue_obj, date_time=event_date)
        session.add(event)
        session.commit()
        session.close()
        click.echo(f"Created event: {name} at {venue} on {event_date.strftime('%Y-%m-%d')}")
    else:
        click.echo(f"Venue {venue} not found.")

@cli.command()
@click.option("--user", prompt="Your name", help="Your name for the booking")
@click.option("--event", prompt="Event name", help="Name of the event")
def book_event(user, event):
    session = SessionLocal()
    event_obj = session.query(Event).filter_by(name=event).first()
    if event_obj:
        event_date = event_obj.date_time.strftime("%Y-%m-%d")
        booking = Booking(user_name=user, event=event_obj)
        session.add(booking)
        session.commit()
        session.close()
        click.echo(f"Booking made for {event} by {user} on {event_date}")
    else:
        click.echo(f"Event {event} not found.")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    cli()


