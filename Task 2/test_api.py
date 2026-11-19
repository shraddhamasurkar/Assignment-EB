"""Pytest coverage for the JSONPlaceholder posts, comments, and users APIs."""

from time import perf_counter

import pytest
import requests
from pydantic import BaseModel, ConfigDict, ValidationError

BASE_URL = "https://jsonplaceholder.typicode.com"


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    model_config = ConfigDict(extra="ignore")

    postId: int
    id: int
    name: str
    email: str
    body: str


class Geo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    lat: str
    lng: str


class Address(BaseModel):
    model_config = ConfigDict(extra="ignore")

    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


ENDPOINTS = [
    pytest.param("posts", Post, id="posts"),
    pytest.param("comments", Comment, id="comments"),
    pytest.param("users", User, id="users"),
]


@pytest.mark.parametrize(("endpoint", "schema"), ENDPOINTS)
def test_endpoint_returns_valid_schema_within_two_seconds(endpoint, schema):
    """Each listed endpoint returns HTTP 200 and data matching its Pydantic model."""
    start = perf_counter()
    response = requests.get(f"{BASE_URL}/{endpoint}", timeout=2)
    elapsed = perf_counter() - start

    assert response.status_code == 200
    assert elapsed < 2, f"/{endpoint} took {elapsed:.3f}s (limit: 2s)"

    data = response.json()
    assert isinstance(data, list), f"/{endpoint} should return a JSON array"
    assert data, f"/{endpoint} should return at least one record"
    for index, record in enumerate(data):
        try:
            schema.model_validate(record)
        except ValidationError as error:
            pytest.fail(f"Invalid /{endpoint} record at index {index}: {error}")
