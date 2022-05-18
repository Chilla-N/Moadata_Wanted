from utils.job import JsonCrudExcuter

# /jobs [POST]
class JobCreateViews():

    def post(self, request):
        executor = JsonCrudExcuter()
        executor.create(request.data)
        return 'Success'


# /jobs/<int:id> [R, U, D]
class JobRUDViews():

    def get(self, request, id):
        executor = JsonCrudExcuter()
        data = executor.get(id)
        return data, 'Success'

    def update(self, request, id):
        executor = JsonCrudExcuter()
        data = executor.update(id, request.data)
        return data, 'Success'

    def delete(self, request, id):
        executor = JsonCrudExcuter()
        executor.delete(id)
        return 'Success'


# jobs/<int:id>/task?task_name=read
class JobTaskViews():

    def get(self, request, id):
        task_name = request.GET('task_name', '')
        executor = JsonCrudExcuter()
        data = executor.run(id, task_name)
        return data, 'Success'
