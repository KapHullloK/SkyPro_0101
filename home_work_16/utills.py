import json


def con_tab_user(class_name):
    with open("data/users_data.json", 'r', encoding="utf-8") as f_us:
        f_user = json.load(f_us)
        result = []

        for user_data in f_user:
            result.append(class_name(
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                age=user_data["age"],
                email=user_data["email"],
                role=user_data["role"],
                phone=user_data["phone"]
            ))
        return result


def con_tab_order(class_name):
    with open("data/orders_data.json", 'r', encoding="utf-8") as f_ord:
        f_order = json.load(f_ord)
        result = []

        for order_data in f_order:
            result.append(class_name(
                name=order_data["name"],
                description=order_data["description"],
                start_date=order_data["start_date"],
                end_date=order_data["end_date"],
                address=order_data["address"],
                price=order_data["price"],
                customer_id=order_data["customer_id"],
                executor_id=order_data["executor_id"]
            ))
        return result


def con_tab_offer(class_name):
    with open("data/offers_data.json", 'r', encoding="utf-8") as f_off:
        f_offers = json.load(f_off)
        result = []

        for offer_data in f_offers:
            result.append(class_name(
                order_id=offer_data["order_id"],
                executor_id=offer_data["executor_id"]
            ))
        return result


def add_user_json(data, class_name):
    add_user = class_name(
        first_name=data["first_name"],
        last_name=data["last_name"],
        age=data["age"],
        email=data["email"],
        role=data["role"],
        phone=data["phone"]
    )
    return add_user


def add_order_json(data, class_name):
    add_order = class_name(
        name=data["name"],
        description=data["description"],
        start_date=data["start_date"],
        end_date=data["end_date"],
        address=data["address"],
        price=data["price"],
        customer_id=data["customer_id"],
        executor_id=data["executor_id"]
    )
    return add_order


def add_offer_json(data, class_name):
    add_offer = class_name(
        order_id=data["order_id"],
        executor_id=data["executor_id"]
    )
    return add_offer
