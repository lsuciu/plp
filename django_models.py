print "**********************"


class DataType():
    STRING = 0
    INT = 1


class MyModel(object):

    def __init__(self, **kwargs):

        for key in kwargs:
            if key in self.__class__.__dict__:
                if self.__class__.__dict__[key] is DataType.STRING and type(kwargs[key]) is str:
                    self.__dict__[key] = kwargs[key]
                elif self.__class__.__dict__[key] is DataType.INT and type(kwargs[key]) is int:
                    self.__dict__[key] = kwargs[key]
                else:
                    raise Exception("type conversion error")

    def save(self):
        all_fields = [f for f in self.__class__.__dict__ if f not in ["__module__", "__doc__"]]
        for f in all_fields:
            if f not in self.__dict__:
                raise Exception("field required to update db")
        print "update table"


def model(**options):
    def _model(function):
        def inner():
            model_name = function.__name__
            data = function()
            if "name" in options:
                model_name = options["name"]
            print model_name
            t = type(model_name, (MyModel, ), data)
            globals().update({model_name: t})
        model.all[function.__name__] = inner

        return model.all[function.__name__]
    return _model
model.all = {}


@model(name="Person")
def some_function():
    return {
    "first_name": DataType.STRING,
    "last_name": DataType.STRING,
    "age": DataType.INT}


@model(name="Dude")
def asdas():
    return {
    "first_name": DataType.STRING,
    "last_name": DataType.STRING,
    "age": DataType.INT
    }
#build all models
print model.all
for k, v in model.all.iteritems():
    v()

print MyModel.__subclasses__()

a = Person(first_name="name", last_name="last", age=20)
# todo type conversion error on setters
#a.last_name = 2
a.save()
