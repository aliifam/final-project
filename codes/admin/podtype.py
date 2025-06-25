@admin_bp.route("/hotel/<hotel_id>/podtype", methods=["POST"])
@jwt_required_role([RoleEnum.ADMIN]) 
def create_pod_type_route(hotel_id):
    return create_pod_type(hotel_id)
@admin_bp.route("/hotel/<hotel_id>/podtype/<pod_type_id>", methods=["PUT"])
@jwt_required_role([RoleEnum.ADMIN])  
def update_pod_type_route(hotel_id, pod_type_id):
    return update_pod_type(hotel_id, pod_type_id)
@admin_bp.route("/hotel/<hotel_id>/podtype/<pod_type_id>", methods=["DELETE"])
@jwt_required_role([RoleEnum.ADMIN])  
def delete_pod_type_route(hotel_id, pod_type_id):
    return delete_pod_type(hotel_id, pod_type_id)
@admin_bp.route("/hotel/<hotel_id>/podtype", methods=["GET"])
@jwt_required_role([RoleEnum.ADMIN]) 
def get_pod_types_route(hotel_id):
    return get_pod_types(hotel_id)