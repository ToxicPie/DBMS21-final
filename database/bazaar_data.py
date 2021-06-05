from hypixel_api import fetch_api
import csv


def get_product_ids(data):
    '''returns the product ids from previously fetch Hypixel API data.'''
    for row in data['products'].values():
        # if both are empty, we assume it's a deprecated or unreleased product
        if row['sell_summary'] or row['buy_summary']:
            yield row['product_id'], 1
        else:
            yield row['product_id'], 0


def main():
    bazaar_data = fetch_api('skyblock/bazaar')

    # write bazaar catalogue file
    # since there's currently no easy way to get a list of product names,
    # we only output a list of product ids and the names can be added manually
    with open('bazaar_catalogue.csv', 'w') as output_file:
        for product_id, enabled in get_product_ids(bazaar_data):
            output_file.write(f'{product_id},,{enabled}\n')


if __name__ == '__main__':
    main()
