def get_input():
    return {
        "Organization": {
            "type": "class",
            "params": {
                "members": {
                    "type": "List[Member]",
                    "default": "[]"
                },
                "name": {
                    "type": "string"
                }
            },
            "methods": {
                "get_males": {
                    "return": "List[Member]"
                },
                "add_member": {
                    "params": {
                        "member": {
                            "type": "Member"
                        }
                    },
                    "return": "List[Member]"
                }
            }
        },
        "Sex": {
            "type": "Enum[string]",
            "members": {
                "Male": "male",
                "Female": "female"
            }
        },
        "Member": {
            "type": "class",
            "params": {
                "name": {
                    "type": "string"
                },
                "age": {
                    "type": "int"
                },
                "sex": {
                    "type": "Sex"
                }
            },
            "methods": {
                "get_name": {
                    "return": "string"
                },
                "get_sex": {
                    "return": "Sex"
                }
            }
        }
    }
