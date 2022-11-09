from .rep_name import NewRepositoryName


class AllValidators:
    """
    validator extractor for useful appeal:
        import validators
        @validator.validator_name
    """
    new_rep_name = NewRepositoryName()


validator = AllValidators()