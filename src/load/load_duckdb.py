import duckdb


def load_data_to_duckdb(root_dir: str):
    """load raw data into persistent duckdb file"""
    
    int_path = f"{root_dir}\\storage\\staging\\database.duckdb"

    # connect or create duckdb file
    conn = duckdb.connect(int_path)

    # initialize tables
    with open(f"{root_dir}\\database\\schema.sql", "r") as f:
        conn.execute(f.read())

    # load data
    # can't get sql loading to find the raw files
    # with open(f"{root_dir}\\database\\load.sql", "r") as f:
    #     conn.execute(f.read())

    # use python method for now
    conn.execute('truncate table staging.car_price_dataset;')
    conn.execute('truncate table staging.cpi_gasoline;')

    conn.execute(f"copy staging.car_price_dataset from '{root_dir}\\storage\\raw\\car-price-dataset.csv';")
    conn.execute(f"copy staging.cpi_gasoline from '{root_dir}\\storage\\raw\\cpi_gasoline.csv';")

    conn.close()


# if __name__ == "__main__":
#     load_data_to_duckdb()
#     print("data loaded to duckdb successfully")
