from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse

router = APIRouter(
    prefix='/product',
    tags=['Http request: Product'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.get('/', response_class=RedirectResponse, include_in_schema=False)
def docs():
    return RedirectResponse(url='/docs')

@router.get('/all-product')
def get_products_all()->str:
    return 'all'