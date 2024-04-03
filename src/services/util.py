from style.snack_bar import SnackBar


class CollectorField:
    field_type = type

    @classmethod
    def fields(cls) -> list[dict]:
        res = []

        for name_attr, type_ in cls.__dict__["__annotations__"].items():
            if type_ is cls.field_type:
                field = getattr(cls, name_attr)

                res.append({field[0]: field[1]})

        return res


def draw_snack_bar_exception_info(page, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        SnackBar(page, f"Ошибка. Подробнее: \"{str(e)}\"").activate_snack_bar()
        raise


async def async_draw_snack_bar_exception_info(page, func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except Exception as e:
        SnackBar(page, f"Ошибка. Подробнее: \"{str(e)}\"").activate_snack_bar()
        raise
