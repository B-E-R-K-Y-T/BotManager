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
