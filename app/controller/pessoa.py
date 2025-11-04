from controller.generic import create_crud_router
from ps_pessoas_fastapi_lib.model.models import Pessoa
from ps_pessoas_fastapi_lib.model.dto import PessoaCreate, PessoaUpdate, PessoaRead

router = create_crud_router(
    model=Pessoa,
    create_schema=PessoaCreate,
    update_schema=PessoaUpdate,
    read_schema=PessoaRead,
    prefix="/pessoas",
    tags=["pessoas"],
)