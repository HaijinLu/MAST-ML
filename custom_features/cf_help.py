import importlib
__author__ = "Tam Mayeshiba"

def get_custom_feature_data(class_method_str=None,
                        starting_dataframe=None,
                        param_dict=dict(),
                        addl_feature_method_kwargs=dict()):
    """Get custom feature data from a method in one of the classes
        in this subpackage.
        The class must initialize with a dataframe.
        The method must take keyword arguments and allow **kwargs
        See Testing.py for an example class (Testing) and method (subtraction).
    Args:
        class_method_str <str>: Class and method string, for example, 
                "Testing.subtraction"
        starting_dataframe <pandas dataframe>: Starting dataframe
        addl_feature_method_kwargs <dict>: Keyword dictionary to be passed
                                            to the class method
    """
    class_name = class_method_str.split(".")[0]
    module_name = "custom_features.%s" % class_name
    feature_name = class_method_str.split(".")[1]
    custom_module=importlib.import_module(module_name)
    custom_class = getattr(custom_module, class_name)
    custom_class_instance = custom_class(starting_dataframe)
    new_feature_data = getattr(custom_class_instance, feature_name)(**addl_feature_method_kwargs)
    return (feature_name, new_feature_data)
