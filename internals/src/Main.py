from utils import *

if __name__ == '__main__':
    try:
        api = Utils()

        # Examples:
        print(api.get_zipp_list())

        api.start_zipp("tor")
        api.start_zipp("wikipedia")

        api.add_zipp("brand_new_zipp")

        api.delete_zipp("other_zipp")

    except Exception as e:
        print(e)
