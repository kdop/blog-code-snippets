"""
from rest_framework import serializers

def get_serializer():
    return type(
        "SerializerName",
        (serializers.Serializer,),
        {
            "prop1": serializers.IntegerField(...),
            "prop2": serializers.IntegerField(...),
            ...
        }
    )
"""
