"""Defines the base Model from which all other models inherit."""

import datetime

from decimal import Decimal
from typing import Any, Dict, List, Optional

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
    def count_all(cls) -> int:
        """Fetches the total stored quantity of a resource.

        Returns:
            The quantity of the given resource found in the database.
        """
        return cls.query.count()

    @classmethod
    def delete_by_id(cls, resource_id: int) -> Optional[int]:
        """Deletes a resource by id.

        Args:
            resource_id: The id of the resource to be deleted.

        Returns:
            resource_id if successful, None otherwise.
        """
        error = False
        try:
            resource = cls.query.get(resource_id)
            resource.delete()
        except:
            error = True
            db.session.rollback()
        finally:
            db.session.close()

        if not error:
            return resource_id

    @classmethod
    def fetch_all(
        cls,
        order_by: Optional[object] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetches all of a resource, ordered.

        Args:
            order_by: SQLAlchemy ORDER BY criterion (see SQLAlchemy docs)

        Returns:
            An ordered list of all matching resources or None.
        """
        resources = cls.query.order_by(order_by).all()
        if resources:
            return [resource.json() for resource in resources]

    @classmethod
    def fetch_all_filtered(
            cls,
            filter_by: object,
            order_by: Optional[object] = None
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetches all of a resource, ordered and filtered.

        Args:
            filter_by: SQLAlchemy filtering criterion (see SQLAlchemy docs)
            order_by: SQLAlchemy ORDER BY criterion (see SQLAlchemy docs)

        Returns:
            A filtered and ordered list of all matching resources or None.
        """
        resources = cls.query.filter_by(**filter_by).order_by(order_by).all()
        if resources:
            return [resource.json() for resource in resources]

    @classmethod
    def fetch_by_id(cls, resource_id: int) -> Optional[Dict[str, Any]]:
        """Fetches a resource by id.

        Args:
            resource_id: The id of the requested resource.

        Returns:
            The requested resource or None.
        """
        response = cls.query.get(resource_id)
        if response:
            return response.json()

    @classmethod
    def fetch_first_filtered(
        cls,
        filter_by: object,
        order_by: Optional[object] = None
    ) -> Optional[Dict[str, Any]]:
        """Fetches the first resource from a filtered and ordered set of
        results.

        Args:
            filter_by: SQLAlchemy filtering criterion (see SQLAlchemy docs)
            order_by: SQLAlchemy ORDER BY criterion (see SQLAlchemy docs)

        Returns:
            The requested resource or None.
        """
        return cls.query.filter_by(**filter_by)\
                        .order_by(order_by)\
                        .first()\
                        .json()

    @classmethod
    def fetch_page(
        cls,
        page: int,
        per_page: int
    ) -> Optional[List[Dict[str, Any]]]:
        """Fetches resources from the database sorted by id and paginated.

        Args:
            page: The page number to fetch.
            per_page: The maximum number of results to show per page.

        Returns:
            A list containing one page of resources.
        """
        resources = cls.query.order_by(cls.id).paginate(page, per_page)
        if resources:
            return [resource.json() for resource in resources.items]

#    @classmethod
#    def get_required_fields(cls) -> List[str]:
#        """Fetches all columns required to create this resource type."""
#        required = []
#        for column in cls.__table__.columns:
#            is_autoincrement = ('int' in str(column.type).lower()
#                                and column.autoincrement)
#            if ((not column.nullable and not column.primary_key)
#                    or (column.primary_key and not is_autoincrement)):
#                required.append(column.name)
#        return required
#
#    @classmethod
#    def optional_fields(cls) -> List[str]:
#        """Fetches all nullable columns for this resource type."""
#        nullable = []
#        for column in cls.__table__.columns:
#            if column.nullable:
#                nullable.append(column.name)
#        return nullable
#
#    @classmethod
#    def primary_key(cls) -> str:
#        """Fetches the name of of the primary key attribute of this resource"""
#        return list(cls.__table__.primary_key.columns)[0].key


db = SQLAlchemy(model_class=Model)
