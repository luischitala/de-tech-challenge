from internal.usecase.utils import response_schema

RESPONSE_404_NOT_FOUND = response_schema(
    example={'successful': False, 'detail': 'Not found'},
    description='Not found',
    status_code=404,
)