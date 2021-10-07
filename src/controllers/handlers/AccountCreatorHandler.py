from typing import List
from models.Account.GenericAccount import GenericAccount
from controllers.persistence.PersistenceController import get_db, EntityKeyEnum
from usecases.AccountValidator import validate_account_operation
from models.Account.StandardAccount import StandardAccount


def handle_create_account(account_operation: dict) -> dict:
    account = convert_dict_to_account(account_operation)
    account_already_existed = is_account_already_exists(account)
    validation_result = format_validation_result(
        validate_account_operation(account_already_existed, account), account
    )
    return validation_result


def convert_dict_to_account(acc: dict) -> GenericAccount:
    return StandardAccount.from_dict(acc)


def is_account_already_exists(account: StandardAccount) -> bool:
    not get_db().set_value_if_not_exists(
        EntityKeyEnum.ACCOUNT_KEY.value, account.to_dict()
    )


def format_validation_result(
    violation_list: List[str], account: GenericAccount
) -> List[dict]:
    validation_result = account.to_dict()
    validation_result["violations"] = violation_list
    return validation_result