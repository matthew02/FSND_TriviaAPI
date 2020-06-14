"""Defines the base Model from which all other models inherit."""

import datetime

from abc import abstractmethod
from decimal import Decimal
from typing import Any, Dict, List, Optional

from flask import abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Model():
    """This is the base class for database models."""

    __abstract__: bool = True
    __table__: Optional[SQLAlchemy] = None

    def json(self) -> Dict[str, Any]:
        """Returns this resource as a dictionary."""
        json = {}
        for column in self.__table__.columns.keys():
            value = getattr(self, column, None)
            if isinstance(value, Decimal):
                json[column] = float(value)
            elif isinstance(value, datetime.datetime):
                json[column] = value.isoformat()
            elif isinstance(value, datetime.time):
                json[column] = value.strftime('%H:%M:%S')
            else:
                json[column] = value
        return json

    def delete(self) -> None:
        """Deletes this resource from the database."""
        db.session.delete(self)
        db.session.commit()

    def insert(self) -> None:
        """Inserats this resource into the database."""
        db.session.add(self)
        db.session.commit()

    def update(self, **attributes: Any) -> None:
        """Updates this resource with new data and saves it to the database."""
        for k, v in attributes.items():
            if 'date' in k:
                setattr(self, k, datetime.date.fromisoformat(v))
            else:
                setattr(self, k, v)
        db.session.commit()

    @classmethod
    @abstractmethod
    def validate_all(cls, json: Dict[str, Any]) -> None:
        """Type validates the fields in the given dict against the attributes
        of this resource. Also verifies that any given foreign keys represent
        an actual resource present in the database."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def validate_some(cls, json):
        """Validates only the populated attributes of this resource."""
        raise NotImplementedError

    @classmethod
    def description(cls) -> Dict[str, str]:
        """Fetches a description of this model including key names and types."""
        description = {}
        for column in cls.__table__.columns:
            column_description = str(column.type)
            if not column.nullable:
                column_description += ' (required)'
            description[column.name] = column_description
        return description

    @classmethod
    def count_all(cls):
        """Fetches the total number of rows in the database."""
        return cls.query.count()

    @classmethod
    def delete_by_id(cls, resource_id: int) -> None:
        """Deletes a resource from the database."""
        resource = cls.query.get(resource_id)
        if not resource:
            abort(404)
        resource.delete()

    @classmethod
    def fetch_all(cls, order_by: Optional[object] = None) -> List[Dict[str, Any]]:
        """Fetches all resources from the database."""
        resources = cls.query.order_by(order_by).all()
        if not resources:
            abort(404)
        return [resource.json() for resource in resources]

    @classmethod
    def fetch_all_filtered(cls, filter_by, order_by: Optional[object] = None):
        """Fetches all resources matching a filter from the database."""
        resources = cls.query.filter_by(**filter_by).order_by(order_by).all()
        if not resources:
            abort(404)
        return list(resource.json() for resource in resources)

    @classmethod
    def fetch_by_id(cls, resource_id: int) -> List[Dict[str, Any]]:
        """Fetches a resource from the database."""
        resource = cls.query.get(resource_id)
        if not resource:
            abort(404)
        return resource.json()

    @classmethod
    def fetch_one_filtered(cls, filter_by, order_by: Optional[object] = None):
        """Fetches a resource from the database with the given filter."""
        resource = cls.query.filter_by(**filter_by).order_by(order_by).first()
        if not resource:
            abort(404)
        return resource

    @classmethod
    def fetch_page(cls, page, per_page) -> List[Dict[str, Any]]:
        """Fetches resources from the database sorted by id and paginated."""
        resources = cls.query.order_by(cls.id).paginate(page, per_page)
        if not resources:
            abort(404)
        return [resource.json() for resource in resources.items]

    @classmethod
    def get_required_fields(cls) -> List[str]:
        """Fetches all columns required to create this resource type."""
        required = []
        for column in cls.__table__.columns:
            is_autoincrement = ('int' in str(column.type).lower()
                                and column.autoincrement)
            if ((not column.nullable and not column.primary_key)
                    or (column.primary_key and not is_autoincrement)):
                required.append(column.name)
        return required

    @classmethod
    def optional_fields(cls) -> List[str]:
        """Fetches all nullable columns for this resource type."""
        nullable = []
        for column in cls.__table__.columns:
            if column.nullable:
                nullable.append(column.name)
        return nullable

    @classmethod
    def primary_key(cls) -> str:
        """Fetches the name of of the primary key attribute of this resource"""
        return list(cls.__table__.primary_key.columns)[0].key


db = SQLAlchemy(model_class=Model)
