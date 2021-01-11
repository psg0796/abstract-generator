def get_input():
    return {
        "Sex": {
            "type": "Enum[string]",
            "members": {
                "Male": "male",
                "Female": "female"
            }
        },
        "Member": {
            "type": "class",
            "methods": {
                "get_name": {
                    "returns": "string"
                },
                "get_sex": {
                    "returns": "Sex"
                }
            }
        },
        "Organization": {
            "type": "class",
            "methods": {
                "get_males": {
                    "returns": "List[Member]"
                },
                "add_member": {
                    "params": {
                        "member": "Member"
                    },
                    "returns": "List[Member]"
                }
            }
        }
    }
